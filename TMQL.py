import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import shutil

class ImageLabeler(tk.Tk):
    def __init__(self, dataset_dir):
        super().__init__()
        self.dataset_dir = dataset_dir
        self.object_folders = ['fork', 'knife', 'spoon', 'plate', 'napkin', 'cup', 'negative']
        for folder in self.object_folders:
            os.makedirs(os.path.join(self.dataset_dir, folder), exist_ok=True)
        self.images = [f for f in os.listdir(self.dataset_dir) if os.path.isfile(os.path.join(self.dataset_dir, f)) and not f.startswith('.')]
        self.current_image_index = 0

        self.title("Image Labeler")
        self.geometry("600x500")

        self.image_panel = tk.Label(self)
        self.image_panel.pack()

        self.create_label_buttons()

        self.display_current_image()

    def create_label_buttons(self):
        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.X, pady=10)
        for label in self.object_folders:
            btn = tk.Button(button_frame, text=label, command=lambda lbl=label: self.label_image(lbl))
            btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

    def label_image(self, label):
        if label in self.object_folders:
            source_path = os.path.join(self.dataset_dir, self.images[self.current_image_index])
            target_path = os.path.join(self.dataset_dir, label, self.images[self.current_image_index])
            shutil.move(source_path, target_path)
            self.current_image_index += 1
            if self.current_image_index < len(self.images):
                self.display_current_image()
            else:
                messagebox.showinfo("Complete", "All images have been labeled.")
                self.destroy()
        else:
            messagebox.showwarning("Invalid Label", "Please enter a valid label.")

    def resize_image_to_aspect(self, image):
        """Resize images while maintaining aspect ratio to fit within 224x224."""
        original_width, original_height = image.size
        target_size = 224
        ratio = min(target_size / original_width, target_size / original_height)
        new_width = int(original_width * ratio)
        new_height = int(original_height * ratio)
        return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    def display_current_image(self):
        if self.current_image_index < len(self.images):
            image_path = os.path.join(self.dataset_dir, self.images[self.current_image_index])
            img = Image.open(image_path)
            img = self.resize_image_to_aspect(img)
            imgTk = ImageTk.PhotoImage(img)
            self.image_panel.configure(image=imgTk)
            self.image_panel.image = imgTk
        else:
            messagebox.showinfo("Complete", "All images have been labeled.")
            self.destroy()

def main():
    root = tk.Tk()
    root.withdraw()
    dataset_dir = filedialog.askdirectory(title="Select Dataset Directory")
    root.destroy()
    if dataset_dir:
        app = ImageLabeler(dataset_dir)
        app.mainloop()

if __name__ == "__main__":
    main()
# Image Labeler for Teachable Machine

## Overview
This Python script provides a graphical user interface (GUI) to facilitate the rapid labeling of images for training machine learning models with Google's Teachable Machine. It displays images from a specified directory and allows users to label them by clicking buttons corresponding to predefined categories. The script moves labeled images into subdirectories named after their labels, streamlining the preparation of training data sets.

## Features
- **Easy Navigation**: Sequentially displays images from a selected directory.
- **Quick Labeling**: Offers a set of buttons for each predefined label category, enabling fast and efficient image labeling.
- **Automatic Sorting**: Automatically moves labeled images into appropriately named subdirectories.
- **Aspect Ratio Preservation**: Resizes images to 224x224 pixels for preview while maintaining the original aspect ratio, without altering the original images.

## Installation

### Prerequisites
- Python 3.6 or higher
- Pillow library

### Setting Up
1. Ensure Python and pip are installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

2. Install the Pillow library, which is used for image processing:
   ```sh
   pip install Pillow

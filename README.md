## Table of contents



## About the project

This repository contains a simple set of script utilities for recognizing decimals with two leading zeros from images in .eps *(encapsulated postscript)* 
formatted files with an uknown monospace-like font. Solution of the problem was achieved by converting *eps* file to *png* format, preprocessing it with OpenCV  *(converting it to grayscale, denoising using [Non-local Means Denoising algorithm](http://www.ipol.im/pub/algo/bcm_non_local_means_denoising), setting a threshold for pixels and smoothing it with a custom filter)* and recognizing it with the use of open source Tesseract recognition engine.

Script in this repository achieves 98% evaluation accuracy *(only one error)* in reading from acquired dataset. Some of the evaluations are corrected manually *(such as number 7 appearing as "F" or "f")* which could be improved if a bigger dataset with the same font was to be acquired. 

All of the testing was done on Ubuntu 20.04.1 LTS with utilization of CUDA. Tesseract version used in this project is 4.1.1. I have experimented with the 4.0.0 version of the library and it has given worse results so it is highly recommended to use the newest version if possible. The included scripts should work the same on Linux, Windows and MacOS *(with and without CUDA)* however since I only use Ubuntu on my personal machines as of the moment I will only present the installation instructions for that operating system.

## Installation

This section assumes you: 
* have a Python 3.8.5 interpreter installed on your operating system
* have the alias of that interpreter set as "python3" *(default on most systems)* 
* have the alias of pip for that interpreter set as "pip3" *(default on most systems)*

If you are using an ubuntu based distribution you should be ready to begin the installation without any tweaking.

```sh
sudo apt install tesseract-ocr libtesseract-dev
python3 -m pip install --upgrade pip
pip3 install opencv-python pytesseract numpy pillow
```

## Usage example

This section contains a set of usage scenarios. It assumes that you are inside of the folder with the scripts. 

1. Recognition of text in a single eps file and printing out to terminal

```sh
python3 recognize.py -i path/to/eps_file.eps
```

2. Recognition of text in a single eps file and saving on disk *(without console output)*
```sh
python3 recognize.py -m -i path/to/eps_file.eps -o path/to/text_from_image.txt 
```

3. Convert all of the images from a selected folder and save their contents in files in the given folder
```sh
# Keep in mind that the script will not create txt_files_folder/ - you must create it beforehand
python3 recognize.py -idir path/to/eps_files_folder/ -odir path/to/txt_files_folder/
```

If you have any doubts about how something works in the program you can run `python3 recognize.py --help` for information about all flags.

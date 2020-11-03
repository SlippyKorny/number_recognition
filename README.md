## Table of contents



## About the project

This repository contains a simple set of script utilities for recognizing decimals with two leading zeros from images in .eps *(encapsulated postscript)* 
format with an uknown monospace-like font. Solution of the problem was achieved by converting eps file to png format and then preprocessing it and removing
background noise with the use of OpenCV. Then the recognition part is achieved by utilizing the open source Tesseract recognition engine. Script in this
repository achieves 98% accuracy in reading from acquired dataset. All of the testing was done on Ubuntu 20.04.1 LTS however the solution should work the same
on all GNU/Linux distributions.

## Installation

This section assumes you: 
* have Python 3.8.5 installed on your operating system
* the alias of that version of python is "python3" 
* the alias of pip for that version of python is "pip3"

If you are using an ubuntu based distribution you should be ready to begin the installation without any tweaking.

```sh
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
pip3 install opencv-python
pip3 install pytesseract
pip3 install numpy
pip3 install pillow
```

## Usage example

This section contains a set of usage scenarios. It assumes that you are inside of the folder with the scripts. 

1. Recognition of text in a single eps file and printing out to terminal

```sh
# First convert the image to png format
python3 convert.py -i path/to/image.eps -o path/to/desired/conversion/output.png
# Recognize the characters in the image and print out to the console
python3 recognize.py -i path/to/desired/conversion/output.png
```

2. Recognition of text in a single eps file and saving on disk (without console output)
```sh
# First convert the image to png format
python3 convert.py -i path/to/image.eps -o path/to/desired/conversion/output.png  
# Recognize the characters in the image and save them on disk
python3 recognize.py -i path/to/desired/conversion/output.png -o path/to/written_output.txt  -m
```

3. Convert all of the images from a selected folder and save their content in files representing each one of them
```sh
# First convert the images in a folder to png format
python3 convert.py -idir path/to/images/ -odir path/to/desired/conversion/output/  
# Recognize characters in each png file and save them in txt files in the specified folder
python3 recognize.py -idir path/to/desired/conversion/output -odir path/to/desired/log/output 
```

After running recognize.py you can always remove the no longer necessary png files with `rm -rf path/to/desired/conversion/*.png`.

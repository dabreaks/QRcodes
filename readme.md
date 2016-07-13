## Synopsis

This just a small utility script for generating QR codes for printing on A4 sized paper. 

We have field teams that want some control over the QR codes that they use in their data collection, where the most important 
component is the secondary 'hand' labeling. There were a set of free utilities and products available, but they would not 
support batch operations, or required the purchase of extra hardware/software or both. Note that this is very bare bones:

- It only has been tested with A4 sized paper
- It requires the use of someone specifying a label image, 580 x 290 pixels
- It does not match up with any sticky paper

Feel free to fork or use as a base to improve on. 

## Requirements

- built on python 2.7.11
- Pillow 3.2
- qrcode 5.1

## Description

gen_QR_sheets.py runs from any current directory, and assumes that there is some subdirectory 'PROJECT' within it that contains a label 'label.png'. See label.png included in the repo for a basic idea, and an exact size


Right now, the global variables are set to our current project's spec:
- FONT = "C:/Windows/Fonts/arial.ttf"                  font location for writing the QR code string
- A4 = (1740, 2610)                                    size of the paper to be used
- PROJECT = 'test'                                     project name
- NUM_CODES = 30                                       number of codes to be generated
- INIT_INT = 0                                         initial ID number


the script will then create a series of labeled QR codes, and order them into a sheet. The name of the QR code is put into the label. See output for an example output sheet given a project called 'test'


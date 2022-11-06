# kindle2pdf
A Python tool that converts Kindle to PDF.

# DEMO

# Features
If you place the cursor on the upper left and lower right of the e-book you want to shoot, it will automatically turn the page.

If it is an e-book that can be page turned with the left and right keys on the keyboard, it can be converted to PDF even if it is not a Kindle.

As long as you have an execution environment for Python and its libraries, it can run on any OS.

# Requirements
Pillow
img2pdf
opencv-python
pyautogui

# Installation
If you use pip:
```bash
pip install -r requirements.txt
```
If you use Anaconda:
```bash
conda create --name <env name> --file conda_requirements.txt
```

# Usage
```bash
git clone https://github.com/1plus1is3/kindle2pdf.git
cd examples
(Create virtual environment with pip or conda)
(Install the virtual environment as above)
python kindle2pdf.py
```

# Note
- By default, the pagination direction is right, so change it to left if necessary.
(capture.py lines 82-83, line 96-97)

- In current version you have to specify a path to save many images in png format before converting to PDF.
Change accordingly according to your environment.
(capture.py line 71, pdf_write.py line 33)

- In the current version, many captured images are not automatically deleted. Please clear it manually if necessary.

# Author
- Suhito Sagara
- Twitter: @1plus1is__

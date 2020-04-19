# BIFF		 

Extract text and images from highlighted pdf generated with reMarkable tablet.	

## Versions

### Version 2.2
 * Creation of an UI (Biff_UI.py) 	
 * Creation of Linux and Windows executables (see releases)

### Version 2.1
 * Add an option for two columns pdf.
 * Add an option to increase quality of cropped images.
 * Improvements on some artifacts (before the whole line was extracted when only a part of if was highlighted)
 * New Windows executable (v2)
		
## Installation and usage	
### Excecutables with User Interface	

For Windows and Linux users, you can download executables with User interface in [releases](https://github.com/soulisalmed/biff/releases/tag/v2.2).
	
### Command line    
biff requires the following modules : 		
  * opencv-python
  * pymupdf
  * numpy
  * odfpy

biff needs Python 3/pip3
```
$ git clone https://github.com/soulisalmed/biff.git					
```
Install the dependencies. It is recommended to use a virtual environment:

```
$ cd biff
$ python3 -m venv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt	
```
To run Biff :
```	
$ source <biff folder>/venv/bin/activate				
$ python -m biff my_highlighted.pdf
$ ./Biff_UI.py			
```
On the command line (cmd.exe):		
```
biff_v2.1.exe my_highlighted.pdf
```
Usage:
```
$ python -m biff -h                
usage: biff [-h] [-c] [-q QUALITY] [-o OUTPUT_FOLDER] [pdf [pdf ...]]

Extract highlighted text and framed images from PDF(s) generated with
reMarkable tablet to Openoffice text document. Highlighted text will be
exported as text. Framed areas will be cropped as images.

positional arguments:
  pdf                   PDF files

optional arguments:
  -h, --help            show this help message and exit
  -c, --two-columns     For two-columns pdf, parse columns from left to right
  -q QUALITY, --quality QUALITY
                        Quality of extracted images, default=2 higher values
                        for higher quality
  -o OUTPUT_FOLDER, --output-folder OUTPUT_FOLDER
                        Output folder for ODT files

```

## Recommandations for pdf highlighting on the reMarkable tablet	

  * On reMarkable, use the Highlighter. All the other tools will not (and should not) be detected by biff.
  * Make sure to cover all the text you want to extract. Partly covered text will not be extracted.
  * For figures, just draw a rectangle shape around it. The interior will be cropped and added as an image to the output odt.
  * Formulas will not be extracted as such, but you can export them as images (see example below).
  * The quality of the text extraction will depend on the pdf quality. Automatically generated pdf from scans will give poor results.
  * Export the PDF using the reMarkable USB web interface (for example).
  
     
    
![alt text][pdf-odt]

[pdf-odt]: https://github.com/soulisalmed/biff/blob/master/pdf-odt.png "Example"

  
Enjoy and please send some feedback.

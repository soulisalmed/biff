# BIFF		 

Extract text and images from highlighted pdf generated with reMarkable tablet.	

## Version

### Version 2
 * Add an option for two columns pdf.
 * Add an option to increase quality of cropped images.
 * Improvements on some artifacts (before the whole line was extracted when only a part of if was highlighted)
 * New Windows executable (v2)
		
## Installation and usage	

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
```
Usage:
```
usage: biff [-h] [-c] [-q QUALITY] [pdf [pdf ...]]

Extract highlighted text and framed images from PDF(s) generated with
reMarkable tablet to Openoffice text document. Highlighted text will be
exported as text. Framed areas will be cropped as images.

positional arguments:
  pdf                   PDF files

optional arguments:
  -h, --help            show this help message and exit
  -c, --two-columns     For two-columns pdf, parse colums from left to right
  -q QUALITY, --quality QUALITY
                        Quality of extracted images, default=2 higher values
                        for higher quality

```

For Windows users, you can download executables in [releases](https://github.com/soulisalmed/biff/releases/tag/v2.0).	
On the command line (cmd.exe):		
```
biff_v2.0.exe my_highlighted.pdf
```
	


The output odt file will be placed in the same directory as the pdf.	

## Recommandations for pdf highlighting on the reMarkable tablet	

  * On reMarkable, use the Highlighter. All the other tools will not (and should not) be detected by biff.
  * Make sure to cover all the text you want to extract. Partly covered text will not be extracted.
  * For figures, just draw a rectangle shape around it. The interior will be cropped and added as an image to the output odt.
  * Formulas will not be extracted as such, but you can export them as images (see example below).
  * The quality of the result will depend on the pdf quality. Automatically generated pdf from scans will give poor results.
  * Export the PDF using the reMarkable USB web interface (for example) and `./biff.py your_pdf.pdf`
  
     
    
![alt text][pdf-odt]

[pdf-odt]: https://github.com/soulisalmed/biff/blob/master/pdf-odt.png "Example"

  
Enjoy and please send some feedback.

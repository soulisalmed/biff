# BIFF		
		
Extract text and images from highlighted pdf generated with reMarkable tablet.		
		
## Installation and usage	
		
biff requires the following modules : 		
  * opencv-python
  * pymupdf
  * numpy
  * odfpy
  

"""
$ git clone <repo>
$ cd <repo>
$ pip -r requirements.txt
$ ./biff.py my_highlighted.pdf
or
$ python3 biff.py my_highlighted.pdf
"""

The output odt file will be placed in the same directory as the pdf		

## Recommandations for pdf highlight on the reMarkable				
  * On reMarkable, use the Highlighter, all the other tools will not (and should not) be detected by biff.
  * Make sure to cover all the text you want to extract. Partly covered text will not be extracted.
  * For figures, just draw a rectangle shape around it. The interior will be cropped and added as an image to the output odt.
  * Formula will not be extracted as text but you can export them as images (see above).
  * The quality of the result will depend on the pdf quality. Automatically generated pdf from scans will give poor results.
  * export the PDF using USB web interface (for example) and `./biff.py your_pdf.pdf`
  
     
    
![alt text][pdf-odt]

[pdf-odt]: https:// "PDF to ODT"

  
Enjoy and please send some feedback.

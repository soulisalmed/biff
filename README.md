# BIFF		
		
Extract text and images from highlighted pdf generated with reMarkable tablet.		
		
## Installation and usage	
		
biff requires the following modules : 		
  * opencv-python
  * pymupdf
  * numpy
  * odfpy
  

```
$ git clone https://github.com/soulisalmed/biff.git			
$ cd biff			
$ pip install -r requirements.txt			
$ ./biff.py my_highlighted.pdf			
or			
$ python3 biff.py my_highlighted.pdf			
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

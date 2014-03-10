import time
from subprocess import call
import re

def ocr(next_page_num):
    base_image_name = "full_image.jpg"
    left_page_image = "page%d.jpg" % next_page_num
    right_page_image = "page%d.jpg" % (next_page_num + 1)
    left_side_text = "page%d" % next_page_num
    right_side_text = "page%d" % (next_page_num + 1)

    ##Take an image from the RaspberryPi camera with sharpness 100(increases the readability of the text for OCR)
    # -cfx 128:128  take grayscale picture instead of colour
    # -q 100  quality setting to max
    # -t 1   move timeout before picture from default 5 seconds to 1
    # -sh 100   maximum sharpness
    # -th none   do not embed thumbail data in image
    call ("raspistill -o " + base_image_name +  " -cfx 128:128 -q 100 -t 1 -sh 100 -th none", shell=True)
    print "Image taken"

    #crop out page on left side
    call ("convert " + base_image_name + " -crop 925x1340+220+330 -depth 300 -units pixelsperinch " + left_page_image, shell=True)

    #Start the Tesseract OCR and save the text to pageXXX.txt
    call ("tesseract " + left_page_image +  " " + left_side_text, shell=True)
    print "left side OCR complete"

    #crop out page on right side
    call ("convert " + base_image_name + " -crop 900x1290+1250+350 -depth 300 -units pixelsperinch " + right_page_image, shell=True)

    #Start the Tesseract OCR and save the text to pageXXX.txt
    call ("tesseract " + right_page_image +  " " + right_side_text, shell=True)
    print "right side OCR complete"

ocr(1)

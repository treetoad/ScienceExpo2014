
# Initial Date: June 24, 2013
# Last Updated: June 24, 2013
#
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)
#
# http://www.dexterindustries.com/
# This code is for testing the BrickPi with a Lego Motor

import time
from subprocess import call
import re
from BrickPi import *   #import BrickPi.py file to use BrickPi operations


wheel_motor = PORT_B
claw_motor = PORT_D
shooty_motor = PORT_A

def initialize():
    print "* initializing BrickPi motors"
    BrickPiSetup()  # setup the serial port for communication
    BrickPi.MotorEnable[wheel_motor] = 1 #Enable the Motor A
    BrickPi.MotorEnable[claw_motor] = 1 #Enable the Motor A
    BrickPi.MotorEnable[shooty_motor] = 1


def move(motor, speed, duration):
    ot = time.time()
    BrickPi.MotorSpeed[motor] = speed
    BrickPiUpdateValues()
    while(time.time() - ot < duration):
        BrickPiUpdateValues()
        time.sleep(0.01)
    BrickPi.MotorSpeed[motor] = 0
    BrickPiUpdateValues()


def stop(motor):
    BrickPi.MotorSpeed[motor] = 0
    BrickPiUpdateValues()


def halfturn_wheel():
    move(wheel_motor, 80, 1.26) ## 0.63

def reset_claw():
    move(shooty_motor, -130, 2)
    move(claw_motor, -30, 1.5)
    ot = time.time()
    BrickPi.MotorSpeed[shooty_motor] = -125
    BrickPi.MotorSpeed[claw_motor] = -30
    BrickPiUpdateValues()
    while(time.time() - ot < 0.5):
        BrickPiUpdateValues()
        time.sleep(0.05)
    BrickPi.MotorSpeed[shooty_motor] = 0
    BrickPi.MotorSpeed[claw_motor] = 0
    BrickPiUpdateValues()
    move(claw_motor, -30, 1.5)

def position_flipper():
    print "get flipper right in front of page"
    move(claw_motor, 18, 1.4) #1.4 is sort of working

def thrust_flipper():
    print "get flipper under page to turn"
    ot = time.time()
    BrickPi.MotorSpeed[shooty_motor] = 125
    BrickPi.MotorSpeed[claw_motor] = 30
    BrickPiUpdateValues()
    while(time.time() - ot < 0.5):
        BrickPiUpdateValues()
        time.sleep(0.05)
    BrickPi.MotorSpeed[shooty_motor] = 0
    BrickPi.MotorSpeed[claw_motor] = 0
    BrickPiUpdateValues()

def flip_page():
    print "actually flip the page"
    move(claw_motor, 120, 3)


def move_claw():

    move(shooty_motor, 130, 1)
    move(claw_motor, 90, 2)
    move(claw_motor, -45, 2)
    move(shooty_motor, -130, 1)

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


initialize()

def turnpage():
	reset_claw()
	halfturn_wheel()
	position_flipper()
	thrust_flipper()
	flip_page()

def main():
  proceed = raw_input("'q' to quit, any other key to process next page :")
  if proceed == "q":
     exit()
  else:
    turnpage()
    ocr(1)
    main()

main()





##
##BrickPi.MotorEnable[PORT_A] = 1 #Enable the Motor A
##BrickPi.MotorEnable[PORT_B] = 1 #Enable the Motor B
##BrickPi.MotorEnable[PORT_C] = 1 #Enable the Motor C




##
##
##while True:
##    print "Motor 1 - Running Forward"
##    BrickPi.MotorSpeed[PORT_A] = 200  #Set the speed of MotorA (-255 to 255)
##    ot = time.time()
##    while(time.time() - ot < 3):    #running while loop for 3 seconds
##        BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
##        time.sleep(.1)              # sleep for 100 ms
##    BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
##
##    BrickPi.MotorSpeed[PORT_B] = 200  #Set the speed of MotorA (-255 to 255)
##    ot = time.time()
##    while(time.time() - ot < 3):    #running while loop for 3 seconds
##        BrickPiUpdateValues()       # Bsk BrickPi to update values for sensors/motors
##        time.sleep(.1)              # sleep for 100 ms
##    BrickPi.MotorSpeed[PORT_B] = 0
##    BrickPi.MotorSpeed[PORT_A] = 0
##    BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
##
##    BrickPi.MotorSpeed[PORT_A] = -200  #Set the speed of MotorA (-255 to 255)
##    ot = time.time()
##    while(time.time() - ot < 3):    #running while loop for 3 seconds
##        BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
##        time.sleep(.1)              # sleep for 100 ms
##    BrickPi.MotorSpeed[PORT_A] = 0
##    BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
##
##    BrickPi.MotorSpeed[PORT_B] = -200  #Set the speed of MotorA (-255 to 255)
##    ot = time.time()
##    while(time.time() - ot < 3):    #running while loop for 3 seconds
##        BrickPiUpdateValues()       # Bsk BrickPi to update values for sensors/motors
##        time.sleep(.1)              # sleep for 100 ms
##    BrickPi.MotorSpeed[PORT_B] = 0
##    BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
##

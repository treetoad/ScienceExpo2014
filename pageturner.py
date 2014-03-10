
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

def ocr():   
    #Take an image from the RaspberryPi camera with sharpness 100(increases the readability of the text for OCR)
    call ("raspistill -o j2.jpg -t 1 -sh 200", shell=True)
    print "Image taken"
    
    #Start the Tesseract OCR and save the text to out1.txt
    call ("tesseract j2.jpg out1.txt", shell=True)
    print "OCR complete"
    
    #Open the text file and split the paragraph to Sentences
    fname="out1.txt"
    f=open(fname)
    content=f.read()
    print content

##ocr()  
initialize()


reset_claw()
halfturn_wheel()
position_flipper()
thrust_flipper()
flip_page()

##5
##
##initialize()



##flip_claw()






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

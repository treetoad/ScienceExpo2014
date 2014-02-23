# Jaikrishna
# Initial Date: June 24, 2013
# Last Updated: June 24, 2013
#
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)
#
# http://www.dexterindustries.com/
# This code is for testing the BrickPi with a Lego Motor

from BrickPi import *   #import BrickPi.py file to use BrickPi operations

BrickPiSetup()  # setup the serial port for communication

wheel_motor = PORT_A
claw_motor = PORT_C
shooty_motor = PORT_B

def initialize():
    print "* initializing BrickPi motors"
    BrickPi.MotorEnable[wheel_motor] = 1 #Enable the Motor A
    BrickPi.MotorEnable[claw_motor] = 1 #Enable the Motor A
    BrickPi.MotorEnable[shooty_motor] = 1


#this moves the wheel turner and gets the page ready to be flipped def
def page_preturn():
    print "* in page_preturn"
    BrickPi.MotorSpeed[wheel_motor] = 100  #Set the speed of MotorA (-255to 255) BrickPiUpdateValues() time.sleep(4)
    
def flip_claw():
    print "*in flip_claw"
    time.sleep(3)
    c  #Set the speed of MotorA (-255 to 255)
    BrickPiUpdateValues()
   
   
    BrickPi.MotorSpeed[claw_motor] = -100
    while(time.time() - ot > 2):
        BrickPiUpdateValues()
        
def move(motor, speed, duration):
    ot = time.time()
    BrickPi.MotorSpeed[motor] = speed
    BrickPiUpdateValues()
    while(time.time() - ot < duration):
        BrickPiUpdateValues()
        time.sleep(0.1)
      
def move_claw():
    print "*moving claw"
    time.sleep(1)
    BrickPi.MotorSpeed[shooty_motor] = 100
    ot = time.time()
    ot = time.time()
    BrickPiUpdateValues()
    BrickPi.MotorSpeed[shooty_motor] = -100
    time.sleep(1)
    while(time.time() - ot < 200):
        BrickPiUpdateValues()
    
        
    
initialize()
##page_preturn()
##move_claw()
##flip_claw()

move(claw_motor, 50, 1.5)
move(shooty_motor, 100, 2)
move(shooty_motor, -100, 2)


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

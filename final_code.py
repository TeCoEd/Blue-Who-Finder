#!/usr/bin/python
import bluetooth
import time
from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
lcd = Adafruit_CharLCDPlate()

def the_check(): ###code to check for devices and compare MAC code with the stored value and return the person in or out
    lcd.clear()
    lcd.backlight(lcd.BLUE)
    print "Checking..."
    lcd.message("Checking.....")
    #find the devices and the name of the device
    devices = bluetooth.discover_devices(lookup_names = True)
    #print how many devices are found
    lcd.clear()
    print("Found %d devices" % len(devices))
    lcd.message("Found %d device/s" % len(devices))
    sleep(1)
    #print the devices and the names
    for addr, name in devices:
        print("  %s - %s" % (addr, name))
        lcd.clear()
        lcd.message(name)
        sleep(2)
      
    time.sleep(1)
    print "Check to see who is in the building"
    lcd.clear()
    lcd.message("Who is in the \nbuilding?")
    sleep(3)
    print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
    lcd.clear()
    lcd.message(time.strftime("%a, %d %b %Y \n%H:%M:%S", time.gmtime()))
    sleep(4)
    #time.sleep(1)
    if len (devices) == 0:
            lcd.backlight(lcd.RED)
            lcd.clear()
            print "No one is currently in the building"
            lcd.message("Building Empty")
            sleep(1)

#check the addresses against list to see who is near
    for person in devices:
     
       device = bluetooth.lookup_name("add your MAC code", timeout=5) #d1
       if (device != None):
           lcd.clear()
           lcd.backlight(lcd.YELLOW)
           print "TeCoEd is in"
           lcd.message("TeCoEd is in his\noffcie on GitHub")
           sleep(2)
       else:
           lcd.clear()
           lcd.backlight(lcd.RED)
           print "Tecoed is out"
           lcd.message("TeCoEd is out")
           sleep(2)
        
       time.sleep(1)    
       lcd.clear() 
       device2 = bluetooth.lookup_name('add yours', timeout=5) #d2
       if (device2 != None):
           lcd.backlight(lcd.RED)
           print "The Boss is in the building, back to work"
           lcd.message("The Boss is here \nback to work!")
           sleep(2)
       else:
           lcd.clear()
           lcd.backlight(lcd.GREEN)
           print "The Boss is still out, Facebook time!"
           lcd.message("The Boss is out!! \nsurf's up!")
           sleep(2)

       #time.sleep(1)
       lcd.clear() 
       device3 = bluetooth.lookup_name("add yours", timeout=5) #d3
       if (device3 != None):
           lcd.backlight(lcd.GREEN)
           print "Wow Sherlock is here O wise one!"
           lcd.message("Sherlock is here \nwith John?")
           sleep(2) 
       else:
           lcd.clear()
           lcd.backlight(lcd.RED)
           print "Sherlock is still out on a case"
           lcd.message("Sherlock is \nstill out!")
           sleep(2)

       time.sleep(1)

       device4 = bluetooth.lookup_name("add yours:", timeout=5) #d4
       if (device4 != None):
           lcd.clear()
           lcd.backlight(lcd.TEAL)
           print "Babbage is present in the building"
           lcd.message("Babbage is here \nat work")
           sleep(2)
       else:
           lcd.clear()
           lcd.backlight(lcd.RED)
           print "Babbage is not here"
           lcd.message("Babbage is \nnot at work!")
           sleep(2)

       device5 = bluetooth.lookup_name("add yours", timeout=5) #d5
       ## check this works
       if (device4 != None):
           lcd.clear()
           lcd.backlight(lcd.VIOLET)
           print "Ada is in the building"
           lcd.message("Ada Lovelace \nis in her office")
           sleep(2)
       else:
           lcd.clear()
           lcd.backlight(lcd.RED)
           print "Ada is currently not in the office"
           lcd.message("Ada is currently \nout on business")
           sleep(2)

####NEW LOOP
def Begin_checks():###begins the program checking for bluetooth devcies
    loop = 1
    while loop > 0:
        the_check()
        loop -=1
        print loop
        if loop == 0:
            repeat = raw_input("Do you want to check again, Y/N? ")
            repeat = repeat.upper()
            if repeat == "N":
                lcd.clear()
                lcd.backlight(lcd.BLUE)
                print "Bye Bye"
                lcd.message("Bye Bye :-)")
                sleep(3)
                lcd.noDisplay()
                lcd.backlight(lcd.OFF)
            elif repeat == "Y":
                loop = 4
            elif len(repeat)>1 or repeat not in ["yn"]:
                print "You did not make a valid selection..Closing program"
      
###introdcution
lcd.clear()
lcd.backlight(lcd.BLUE)
lcd.message("Welcome to the \nBlue-Who Finder")
sleep(3)

print "Blue-Who Finder"

Begin_checks()
        

        

    

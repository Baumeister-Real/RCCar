import RPi.GPIO as gpio
import getopt, sys
import time

time.sleep(15)

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(12, gpio.OUT)
gpio.setup(16, gpio.OUT)
gpio.setup(20, gpio.OUT)
gpio.setup(21, gpio.OUT)

argumentList = sys.argv[1:]

options = "frlbsx:"
long_options =[]

try:
    arguments, values = getopt.getopt(argumentList, options, long_options)

    for currentArgument, currentValue in arguments:
            if currentArgument in ("-f"):
                gpio.output(16, gpio.LOW)
                gpio.output(21, gpio.LOW)
                
                gpio.output(21, gpio.HIGH)
                gpio.output(12, gpio.HIGH)
            elif currentArgument in ("-r"):
                gpio.output(16, gpio.LOW)
                gpio.output(21, gpio.LOW)
                gpio.output(12, gpio.HIGH)
                gpio.output(20, gpio.HIGH)
            elif currentArgument in ("-l"):
                gpio.output(12, gpio.LOW)
                gpio.output(20, gpio.LOW)
                gpio.output(16, gpio.HIGH)
                gpio.output(21, gpio.HIGH)
            elif currentArgument in ("-b"):
                gpio.output(12, gpio.LOW)
                gpio.output(21, gpio.LOW)
                gpio.output(16, gpio.HIGH)
                gpio.output(20, gpio.HIGH)
            elif currentArgument in ("-s"):
                gpio.output(12, gpio.LOW)
                gpio.output(16, gpio.LOW)
                gpio.output(20, gpio.LOW)
                gpio.output(21, gpio.LOW)
except getopt.error as err:
    print(str(err))

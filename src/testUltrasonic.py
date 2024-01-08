#!/usr/bin/env python3

from pyfirmata import Arduino, util
import time

#remember to change the ACM to the correct number
board = Arduino('/dev/ttyACM0')

echo = board.get_pin('d:11:i')
trig = board.get_pin('d:12:o')

it = util.Iterator(board)
it.start()

trig.write(0)
time.sleep(2)

while True:
    time.sleep(0.5)

    trig.write(1)   
    time.sleep(0.00001)
    trig.write(0)
    
    print(echo.read())
    while echo.read() == False:
        start = time.time()

    while echo.read() == True:
        end = time.time()
    
    TimeElapsed = end - start
    distance = (TimeElapsed * 34300) / 2

    print("Measured Distance = {} cm".format(distance) )

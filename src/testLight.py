#!/usr/bin/env python3

from pyfirmata import Arduino, util
import time

#remember to change the ACM to the correct number
board = Arduino('/dev/ttyACM0')

it = util.Iterator(board)
it.start()

light = board.get_pin('a:0:i')

while True:

    brightness = light.read()

    if brightness == None:
        continue
    else:
        brightness = (brightness*1000)

    
    if brightness < 50:
        board.digital[13].write(1)

    else:
        board.digital[13].write(0)


    print('Brightness is ' + str(brightness))
    time.sleep(1)

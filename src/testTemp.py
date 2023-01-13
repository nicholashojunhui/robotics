#!/usr/bin/env python3

from pyfirmata import Arduino, util
import time

#remember to change the ACM to the correct number
board = Arduino('/dev/ttyACM0')

it = util.Iterator(board)
it.start()

temperature = board.get_pin('a:0:i')

while True:

    t = temperature.read()

    if t == None:
        continue
    else:
        temp = (t*1000)/2.048

    if  temp > 32:
        board.digital[13].write(1)

    else:
        board.digital[13].write(0)

    print('Temperature is ' + str(temp))
    time.sleep(1)

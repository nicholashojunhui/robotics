#!/usr/bin/env python

from pyfirmata import Arduino, util
import time

#remember to change the ACM to the correct number
board = Arduino('/dev/ttyACM1')

it = util.Iterator(board)
it.start()


while True:

    board.digital[13].write(1)

    time.sleep(1)

    board.digital[13].write(0)

    time.sleep(1)

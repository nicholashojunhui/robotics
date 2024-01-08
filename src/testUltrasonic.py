#!/usr/bin/env python3

from pyfirmata import Arduino, util
import time

#remember to change the ACM to the correct number
board = Arduino('/dev/ttyACM0')

it = util.Iterator(board)
it.start()


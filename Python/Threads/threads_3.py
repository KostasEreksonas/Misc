#!/usr/bin/env python3

import threading

class thread(threading.Thread):
    def __init(self, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID

    def run(self):
        #for i in range(0,10):
        print(str(self.thread_name) + " " + str(self.thread_ID));

if __name__ == "__main__":
    thread1 = thread("GFG", 1000)
    thread2 = thread("GeeksforGeeks", 2000)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

'''
Threading/Multithreading:

These techniques allow the programs to perform multiple tasks simultaneously/concurrently, which improves the performance.
'''

# Let's say we are waiting for a network request and we are using request package and we are to pull the github profile of 100 users. You will pull one and once done then for the other and likewise for others. But threading module can help you do it for all at once.

import threading
import time

def worker(num):
    print(f"Thread {num}: Starting...")
    time.sleep(2) # Simulating some work
    print(f"Thread {num}: Finishing...")

threads = []

for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join() # Waiting for all threads to finish
print("All threads completed.")

# Make sure that you study multi-processing in python, it has multiple processes.
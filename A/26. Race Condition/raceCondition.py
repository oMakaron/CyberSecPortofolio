import threading
import time

# shared memory resource
counter = 0

def addCounter():
    global counter

    # The whole Read-Modify-Write cycle could be written as one expression of counter += 1
    # However, I included a sleep if a race condition won't happen
    for _ in range(10000):
        # Read
        local_counter = counter

        # Modify
        local_counter += 1

        # force a race condition if you get a constant 20,000
        # let the thread sleep for a while so that OS can schedule for another threat to run
        #time.sleep(0.0001)

        # Write
        counter = local_counter

# create two separate threads
thread1 = threading.Thread(target=addCounter)
thread2 = threading.Thread(target=addCounter)

# start both threads at the same time
thread1.start()
thread2.start()

# wait for both threads to finish before printing the result
thread1.join()
thread2.join()

# expected: 20000 (10k + 10k)
print(f"counter: {counter}")


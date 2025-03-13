# we can have thread to execute in python
import multiprocessing
import threading


def task1():
    print("Task1")
def task2():
    print("Task2")

if __name__=='__main__':
    # Create process for parallel execution
    process1 = multiprocessing.Process(target=task1())
    process2 = multiprocessing.Process(target=task2())

    # Start process
    process1.start()
    process2.start()

    # Wait for all process to finish

    process1.join()
    process2.join()

    print("All task completed")


# sequential execution

task1()
task2()

def task3():
    print("Tasl3")
def task4():
    print("Task4")

#Using thread for parallel execution

thread1 = threading.Thread(target=task3())
thread2 = threading.Thread(target=task4())

# Start threads
thread1.start()
thread2.start()

# wait for all thread

thread1.join()
thread2.join()

print("all thread completed")
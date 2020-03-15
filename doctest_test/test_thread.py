import threading

NUM_ITEMS = 100000

my_dict = {}

lock1, lock2 = threading.Lock(), threading.Lock()

def thread(name):
    for _ in range(100000):
        print(name)


t1 = threading.Thread(target=thread, args=("Thread1",))
t2 = threading.Thread(target=thread, args=("Thread2",))
t1.start()
t2.start()

t1.join()
t2.join()
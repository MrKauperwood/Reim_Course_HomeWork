import threading

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        for _ in range(10000):
            print(self.name)

t1 = MyThread("Thread1")
t2 = MyThread("Thread2")
t1.start()
t2.start()
t1.join()
t2.join()
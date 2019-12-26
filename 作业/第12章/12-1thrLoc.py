import threading
import time
z=0
def func1(x, y):
    for i in range(x, y):
        queueLock.acquire()
        global z
        z=z+i
        print(z)
        queueLock.release()
        time.sleep(2)
queueLock = threading.RLock()
t1=threading.Thread(target = func1, args = (3, 6))
t2=threading.Thread(target = func1, args = (6, 9))
t3=threading.Thread(target = func1, args = (9, 12))
t1.start()
t2.start()
t3.start()


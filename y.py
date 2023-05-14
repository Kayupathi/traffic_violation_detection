from subprocess import call
import threading
import time
def g():
    time.sleep(10)
    call(["python","SpeedRadar2.py"])
def h():
    time.sleep(13)
    call(["python","redlight.py"])
def j():
    call(["python","detect.py"])
t=threading.Thread(target=g)
t1=threading.Thread(target=j)
t2=threading.Thread(target=h)
t.start()
t1.start()
t2.start()
t.join()
t1.join()
t2.join()

import threading
import time
t = time.perf_counter()
def sleep():
    time.sleep(1)
    print("done")
def g():
    print("fonction g")
    time.sleep(2)


thread1 = threading.Thread(target=sleep)
#thread2 = threading.Thread(target=sleep)
thread3 = threading.Thread(target=g)

thread1.start()
#thread2.start()
thread3.start()
thread1.join()
#thread2.join()
thread3.join()

end = time.perf_counter()
print(f"programme terminé en {end-t}")
# Multithreading :

import threading

import time
def calc_Square(num):
    print("Calculate Square")
    for i in num:
        time.sleep(.3)
        print("Square :",i*i)
def calc_Cube(num):
    print("Calculate Cube")
    for i in num:
        time.sleep(.3)
        print("Cube :", i*i*i)

ar=[2,3,4,5]
t1=threading.Thread(target=calc_Square,args=(ar,))
t2=threading.Thread(target=calc_Cube,args=(ar,))
t=time.time()
t1.start()
t2.start()
t1.join()
t2.join()

print("Time taken for execution",time.time()-t)
print("Finished execution of threads")
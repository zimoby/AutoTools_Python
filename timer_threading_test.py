import time
import threading 

def print_hello():
#   for i in range(4):
    for x in range(1, 10):
        time.sleep(3)
        print(x)
  
def print_hi(): 
    # for i in range(4): 
    #   time.sleep(0.7)
    a = input("Enter some text: ")
    if a == "stop":
        t2.kill()
    print("a")
    #   print("Hi") 

t1 = threading.Thread(target=print_hello)  
t2 = threading.Thread(target=print_hi)  
t1.start()
t2.start()




# time.sleep(5)
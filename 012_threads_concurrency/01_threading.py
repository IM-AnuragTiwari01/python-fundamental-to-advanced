import threading 
import time

def take_oreders():
    for i in range(1, 4):
        print(f"Taking order for #{ i }")
        time.sleep(1)

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai for #{ i }")
        time.sleep(2)

# create threads
order_thread = threading.Thread(target = take_oreders)
brew_thread = threading.Thread(target = brew_chai)

# invoking / start the thread

order_thread.start()
brew_thread.start()

# wait for both the thread to finish
order_thread.join()
brew_thread.join()

print(f" all orders taken and chai brewed")
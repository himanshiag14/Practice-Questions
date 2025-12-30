#Exponential Bakoffs

import time

wait_time = 1
retry = 5
attempts = 0

while attempts < retry:
    print("Attempt", attempts+1 ," Wait time ",wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1
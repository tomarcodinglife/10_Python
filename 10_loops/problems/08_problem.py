import time 

wait_time = 1
max_retries = 5
attempt = 0

while attempt < max_retries:
    print("Attempts", attempt, +1, "_wait_time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2  
    attempt += 1
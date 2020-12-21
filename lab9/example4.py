import time
def time_remain(n) :
  if n == 0 :
    print("end")
    return None
  print(f"time remains : {n}")
  time.sleep(1)
  return time_remain(n-1)
time_remain(5)
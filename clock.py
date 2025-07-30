import time

n = int(input("Enter time in seconds:"))

for i in range(n,0,-1):
    seconds= i%60
    min = int(i/60)%60
    hour  = int(i/3600)
    print(f"{hour:02}:{min:02}:{seconds:02}")
    time.sleep(1)
print("time up")
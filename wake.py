wake_h = int(input())
wake_m = int(input())
m = int(input())
n = int(input())

wake_m += wake_h*60
sleep_m = 22*60
for i in range(wake_m, sleep_m, m):
    if n < 1:
        break
    n -= 1
    print("%02d:%02d Carrot Time!"%(i//60, i%60))

if n > 0:
    print("Emergency!")

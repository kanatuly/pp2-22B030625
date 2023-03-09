import time

num = int(input())
delay = int(input())

time.sleep(delay / 1000)

print("Square root of {} after {} miliseconds is {}".format(num, delay, pow(num, 0.5)))
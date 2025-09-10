import time

my_time = int(input("Enter the time in seconds: "))

for x in reversed(range(my_time + 1)):  # Include 0 in the countdown #(range(my_time,0,-1)
    second = x % 60
    minute = int((x / 60) % 60)
    hours = int(x / 3600) 
    print(f'{hours:02}:{minute:02}:{second:02}')  # Fixed variable name
    time.sleep(1)

print("Time's UP!")


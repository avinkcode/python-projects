import time
seconds = int(input("please enter a number for your amount of seconds "))
time_going_down = int(input("please enter a number for your time going down "))
end_point = int(input("please enter a number for your countdown to stop at "))
for k in range(seconds,end_point,-time_going_down):
    print(k)
    time.sleep(1)
print("Times Up!:D")
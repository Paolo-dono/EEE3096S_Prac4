# import RPi.GPIO as GPIO
# import time
# 
# def input1(pin):
#     print("Button1 Pressed")
# 
# def input2(pin):
#     print("Button2 Pressed")
# 
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# GPIO.setup(25, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# GPIO.add_event_detect(24, GPIO.RISING, callback = input1, bouncetime = 200)
# GPIO.add_event_detect(25, GPIO.FALLING, callback = input2, bouncetime = 200)
# GPIO.setup(23, GPIO.OUT)
# GPIO.setup(23, GPIO.HIGH)
# time.sleep(4)
# GPIO.setup(23, GPIO.LOW)
# time.sleep(2)
# time.sleep(100)

x = [[5, 'a'], [4, 'b'], [3, 'c']]
x.pop(2)
print(x)
import time 
import RPi.GPIO as GPIO 
import Adafruit_ADS1x15 
 
xAxis = 22 
yAxis = 17 
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(xAxis, GPIO.OUT)
GPIO.setup(yAxis, GPIO.OUT) 
 
adc = Adafruit_ADS1x15.ADS1115() 
 
xPwm = GPIO.PWM(xAxis, 50) 
yPwm = GPIO.PWM(yAxis, 50) 
 
xPwm.start(0)
yPwm.start(0)
x_angle = 7.5
y_angle = 5.5 
 
def lightValue():
    GAIN = 1 

    while True:
        quadrant = [0] * 4
        for i in range(4):
            quadrant[i] = adc.read_adc(i, gain = GAIN) 
        time.sleep(0.5) 
  
        global x_angle
        global y_angle 
 
        if (quadrant[0] < 5000) & (quadrant[1] < 5000):
            y_angle -= 0.5
            yPwm.ChangeDutyCycle(y_angle) 
            time.sleep(0.5)
            if y_angle < 2.5: 
                y_angle = 2.5
        elif (quadrant[2] < 5000) & (quadrant[3] < 5000):
            y_angle += 0.5 
            yPwm.ChangeDutyCycle(y_angle)
            time.sleep(0.5)                   
            if y_angle > 12.5:
                y_angle = 12.5
        if (quadrant[1] < 5000) & (quadrant[2] < 5000):
            x_angle -= 0.5
            xPwm.ChangeDutyCycle(x_angle)
            time.sleep(0.5)
            if x_angle < 2.5:
                x_angle = 2.5
        elif (quadrant[0] < 5000) & (quadrant[3] < 5000):
            x_angle += 0.5
            xPwm.ChangeDutyCycle(x_angle)
            time.sleep(0.5)
            if x_angle > 12.5:
                x_angle = 12.5 
 
def destroy():
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        lightValue()
    except KeyboardInterrupt:
        destroy() 

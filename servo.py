from machine import Pin, PWM
 
 
class Servo:
 
    def __init__(self, pin: int or Pin or PWM, minVal=2500, maxVal=7500, max_angle=180, reverse=False):
        
 
        if isinstance(pin, int):
            pin = Pin(pin, Pin.OUT)
            
        if isinstance(pin, Pin):
            self.__pwm = PWM(pin)
            
        if isinstance(pin, PWM):
            self.__pwm = pin
            
        self.__pwm.freq(50)
        self.minVal = minVal
        self.maxVal = maxVal
        
        self.reverse = reverse
        
        self.angle = 'Not Defined'
        self.max_angle = max_angle
 
    def deinit(self):
        self.__pwm.deinit()
        
    def read(self):
        return self.angle
     
    def servo_map(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    def write(self, angle, smooth=False):
          
        if self.reverse:
            angle = 180 - angle
        
        if angle < 0:
            angle = 0
            
        if angle > 180:
            angle = 180
        
        self.angle = angle
        
        self.goto( round( self.servo_map(angle, 0, self.max_angle, 0, 1024) ) )
    
    def goto(self, value: int):

        if value < 0:
            value = 0
            
        elif value > 1024:
            value = 1024
            
        delta = self.maxVal-self.minVal
        
        target = int( self.minVal + ( (value / 1024) * delta) )
        
        self.__pwm.duty_u16(target)
 
    def middle(self):
        self.goto(512)
 
    def free(self):
        self.__pwm.duty_u16(0)


from servo import Servo

class EasyLimb:
    """
        A simple programming beginner friendly class for controlling generic prosthesis actuated by Servo Motors
        
        Attributes:
            prosthesis_name: A String used to name the prosthesis
            
            _servos: Dictionary used to store all servos attached to the class object
            _used_pins: List used to keep track of all pins used by servos
            
    """
    
    
    def __init__(self, prosthesis_name='Generic Prosthesis'):
        """
            Creates EasyLimb object
            
            args:
                prosthesis_name (str): Optional, a String used to name the prosthesis

        """
        
        
        self.name = prosthesis_name
        self._servos = {}
        self._used_pins = []
        
    def add_servo(self, servo_name, servo_pin, max_degrees=180, reverse_rotation=False):
        """
            Attaches new Servo to EasyLimb object
            
            args:
                servo_name (str): A String used to name the servo
                servo_pin (int or machine.Pin or machine.PWM): Either an integer denoting the number of the GPIO pin or an already constructed Pin or PWM object that is connected to the servo.
                max_degrees (int): Optional, denotes the maximum angle (in degrees) supported by the servo
                reverse_rotation (bool): Optional, denotes if the servo should rotate backwards

        """
        
        
        if servo_name in self._servos:
            print(f"There already is a servo named '{servo_name}'")
            return False
        
        if servo_pin in self._used_pins:
            print(f"There already is a servo using pin '{servo_pin}'")
            return False
        
        
        servo = Servo(servo_pin, max_angle=max_degrees, reverse=reverse_rotation)
        
        self._used_pins.append(servo_pin)
        
        self._servos[servo_name] = {
                'pin': servo_pin,
                'degrees': max_degrees,
                'reverse': reverse_rotation,
                'servo': servo
            }
        
        print(f"Servo named '{servo_name}' on pin {servo_pin} added with success!")
        
        return True
    
    def show_all_servos(self):
        
        """
            Shows all servos attached to the prosthesis

        """
        
        servos = self._servos
        print(f"\nAll servos added to '{self.name}'\n")
        for servo in servos:
            s = servos[servo]
            print(f"{servo}:\nPin: {s['pin']}\nMax Degrees: {s['degrees']}\nReverse Rotation: {s['reverse']}")
            print('\n###############\n')
    
    def rotate_servo(self, servo_name, angle_in_degrees):
        """
            Rotates specified servo by the specified amount in degrees
            
            args:
                servo_name (str): Name of the servo that should rotate
                angle_in_degrees (int): Amount in degrees to rotate the specified servo
        """
        try:
            self._servos[servo_name]['servo'].write(angle_in_degrees)
        except KeyError as e:
            print(f"'{e}' is not registered as the name of a Servo")
            return None
    
    def get_servo_angle(self, servo_name):
        """
            Returns the amount in degrees that the specified servo rotated
            
            args:
                servo_name (str): Name of the servo to retrieve rotation
        """
        try:
            angle = self._servos[servo_name]['servo'].read()
        except KeyError as e:
            print(f"'{e}' is not registered as the name of a Servo")
            return None
            
        print(f"Servo '{servo_name}' rotated {angle} degrees")
        return angle



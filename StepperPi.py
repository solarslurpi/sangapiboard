
import RPi.GPIO as GPIO

class Stepper:
    def __init__(self, number_of_steps,motor_pin_1, motor_pin_2, motor_pin_3, motor_pin_4):
        self.step_number = 0
        self.direction = 0
        self.last_time_step = 0
        self.number_of_steps = number_of_steps
        self.motor_pins = [motor_pin_1,motor_pin_2,motor_pin_3, motor_pin_4]
        # Use the RaspPi board numbers
        GPIO.setmode(GPIO.BOARD)
        # Set the four motor pins to output and initialize to 0 V (False)
        # for pin in self.motor_pins:
        #     GPIO.setup(pin,GPIO.OUT)
        #     GPIO.output(pin,False)

    def stepMotor(self,thisStep):
        # It easier to see how the motor is energized to move around if we look at
        # the half-step sequences.  A full revolution of the motor takes 8 steps.
        step_sequences = [
            [1,0,0,1],
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1]
        ]
        # for i in range(4):
        #     GPIO.output(self.motor_pins[i],step_sequences[thisStep][i])



    def version(self):
        return 0
        
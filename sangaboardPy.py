from StepperPy import Stepper
# Create the 3 Stepper motor instances.  This requires all pins defined and tested.
# Set steps remaining for each motor to 0.


class SangaboardPy:
    def __init__(self):
        self.n_motors = 3
        # x-axis stepper motor
        self.motors[0] = Stepper(8, 12, 15,11, 13)
        self.steps_remaining = [0 for _ in range(self.n_motors)]

    def stepMotor(self, motor, dx):
        self.current_pos[motor] += dx
        self.motors[motor].stepMotor(((self.current_pos[motor] % 8) + 8 ) % 8)  # If it was me, I'd just do % 8 but this is how the Arduino code handles it...
        
    def releaseMotor(self, motor):
        self.motors[motor].release()


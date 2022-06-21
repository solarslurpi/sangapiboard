from StepperPy import Stepper
# Create the 3 Stepper motor instances.  This requires all pins defined and tested.
# Set steps remaining for each motor to 0.


class SangaboardPy:
    def __init__(self):
        self.n_motors = 3
        # x-axis stepper motor
        self.motors[0] = Stepper(8, 12, 15,11, 13)
        self.steps_remaining = [0 for _ in range(self.n_motors)]
        self.min_step_delay = 

    def mrx(self, n_steps):
        axis = 0
        displacement = [0 for _ in range(self.n_motors) ]
        displacement[axis] = n_steps
        self.move_axes(displacement)

    def move_axes(self,disp):
        dir = [(1 if disp[i] > 0 else 0) for i in disp]
        displacement = [disp[i]*dir[i] for i in disp]
        max_steps = 0
        max_steps = [displacement[i] for i in displacement if displacement[i] > max_steps]
        # Scale the step delays so the move goes in a straight line, with >= 1 motor
        # running at max. speed.
        step_delay = [(max_steps/displacement[i]*min_step_delay]



    def stepMotor(self, motor, dx):
        self.current_pos[motor] += dx
        self.motors[motor].stepMotor(((self.current_pos[motor] % 8) + 8 ) % 8)  # If it was me, I'd just do % 8 but this is how the Arduino code handles it...
        

    def releaseMotor(self, motor):
        self.motors[motor].release()


import pytest
from StepperPi import Stepper


@pytest.fixture
def myStepper():
    myStepper = Stepper(8,15,18,23,24)
    return myStepper

def test_version_number(myStepper):
    # This test was run on version 0. Versions are integer numbers
    assert myStepper.version() == 0
    

def test_version_type(myStepper):
    assert isinstance(myStepper.version(),int)

def test_set_speed(myStepper):
    step_delay_at_15RPM =  60 * 1000 * 1000 /myStepper.number_of_steps / 15
    myStepper.setSpeed(15)
    assert myStepper.step_delay == step_delay_at_15RPM

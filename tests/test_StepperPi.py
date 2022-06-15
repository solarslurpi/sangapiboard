import pytest
from StepperPi import Stepper


class TestsStepperPi:
        
    def test_version(self):
        s = Stepper(8,15,18,23,24)
        # This test was run on version 0. Versions are integer numbers
        version = s.version()
        assert isinstance(s.version,int)
        assert version == 0
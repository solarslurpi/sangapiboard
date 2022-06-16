import pytest
from StepperPi import Stepper


@pytest.fixture
def version():
    s = Stepper(8,15,18,23,24)
    version = s.version()
    return version

def test_version_number(version):
    # This test was run on version 0. Versions are integer numbers
    assert version == 0
    

def test_version_type(version):
    assert isinstance(version,int)

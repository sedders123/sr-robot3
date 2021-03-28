"""sr.robot3 - Student Robotics API for Python 3."""

from astoria.common.messages.astmetad import RobotMode
from j5.boards.sr.v4 import PowerOutputPosition
from j5.components.gpio_pin import GPIOPinMode
from j5.components.motor import MotorSpecialState
from j5.components.piezo import Note

from .logging import logger_setup
from .robot import Robot, __version__

logger_setup()

COAST = MotorSpecialState.COAST
BRAKE = MotorSpecialState.BRAKE

ANALOGUE_INPUT = GPIOPinMode.ANALOGUE_INPUT
ANALOGUE_OUTPUT = GPIOPinMode.ANALOGUE_OUTPUT
INPUT = GPIOPinMode.DIGITAL_INPUT
INPUT_PULLUP = GPIOPinMode.DIGITAL_INPUT_PULLUP
INPUT_PULLDOWN = GPIOPinMode.DIGITAL_INPUT_PULLDOWN
OUTPUT = GPIOPinMode.DIGITAL_OUTPUT
PWM_OUTPUT = GPIOPinMode.PWM_OUTPUT

COMP = RobotMode.COMP
DEV = RobotMode.DEV

OUT_H0 = PowerOutputPosition.H0
OUT_H1 = PowerOutputPosition.H1
OUT_L0 = PowerOutputPosition.L0
OUT_L1 = PowerOutputPosition.L1
OUT_L2 = PowerOutputPosition.L2
OUT_L3 = PowerOutputPosition.L3

__all__ = [
    "ANALOGUE_INPUT",
    "ANALOGUE_OUTPUT",
    "BRAKE",
    "COAST",
    "COMP",
    "DEV",
    "INPUT",
    "INPUT_PULLDOWN",
    "INPUT_PULLUP",
    "Note",
    "OUTPUT",
    "OUT_H0",
    "OUT_H1",
    "OUT_L0",
    "OUT_L1",
    "OUT_L2",
    "OUT_L3",
    "PWM_OUTPUT",
    "Robot",
    "__version__",
]

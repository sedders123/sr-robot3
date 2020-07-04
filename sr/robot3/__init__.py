"""sr.robot3 - Student Robotics API for Python 3."""

from .logging import logger_setup
from .robot import Robot, __version__

logger_setup()

__all__ = [
    "__version__",
    "Robot",
]

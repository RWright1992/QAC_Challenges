'''Unable to write working test for class will come back to ammend code
'''
from programs import rectangle_area
import pytest

class Rectangle:

    def test_area(self):
        assert rectangle_area.Rectangle(2,10) ==10
    
   
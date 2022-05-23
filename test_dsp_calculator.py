# -*- coding: utf-8 -*-
"""
Created on Sat May 21 19:01:07 2022

@author: Matt
"""

from dsp_calculator import get_resources, get_components, get_dependencies
from item_library import *

#%%
"""
Test functions to validate dsp_calculator works as expected.
"""

def test_get_resources():
    """
    Tests the get_resources() funtion.
    """
    expected_output = [('ring', 1),
                       ('copper', 0.5),
                       ('ring', 1),
                       ('copper', 0.5),
                       ('ring', 0.5),
                       ('copper', 0.25)]
    
    assert get_resources((("em_ring"),2.5)) == expected_output

    
def test_get_components():
    """
    Tests the get_components() funtion.
    """
    expected_output = [('motor', 2),
                       ('em_ring', 2),
                       ('motor', 2),
                       ('em_ring', 2),
                       ('motor', 0.5),
                       ('em_ring', 0.5)]
    
    assert get_components((("em_motor"), 2.25)) == expected_output

def test_get_dependencies():
    """
    Tests the get_dependencies() funtion.
    """
    expected_output = ([('gear', 1), ('em_ring', 1), ('gear', 0.25), ('em_ring', 0.25)],
    [('iron', 2), ('iron', 0.5), ('iron', 1), ('ring', 1), ('copper', 0.5), ('iron', 0.25), ('ring', 0.25), ('copper', 0.125)])
     
    assert get_dependencies([["motor", 1.25],],[],[]) == expected_output
    


if __name__ == "__main__":
    test_get_resources()
    test_get_components()
    test_get_dependencies()
    

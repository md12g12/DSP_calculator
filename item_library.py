# -*- coding: utf-8 -*-
"""
Created on Sat May 21 18:53:19 2022

@author: Matt
"""


from dataclasses import dataclass
from collections import Counter


"""
define basic classes
"""

@dataclass
class item:
    name: str()
    
@dataclass    
class component(item):
    components: list()
    raw: list()
    crafting_time: float()
    building: str()
    byproduct: str() = None
        
@dataclass
class building(item):
    components: list()
    crafting_time: float()
    building: str()
    
"""
Adding every object in the game as a class with its dependencies

e.g.

name = component("name", (sub-components), (resources), crafting speed, production building, by-products)

sub-components and resources must be a list of tuples with the name and quantity in each tuple e.g. (("copper", 0.5), ("iron", 1)) is 1/2 copper + 1 iron
"""

gear = component("gear", None, (("iron",1),), 1.0, "assembler")
steel = component("steel", None, (("iron", 3),), 3.0, "assembler")
em_ring = component("em_ring", None, (("ring", 1), ("copper", 0.5)), 0.5, "assembler")
motor = component("motor", (("gear", 1), ("em_ring", 1)), (("iron", 2),), 2.0, "assembler")
em_motor = component("em_motor", (("motor", 2), ("em_ring", 2)), None, 0.5, "assembler")
graphite = component("graphite", None, (("coal", 2),), 0.5, "assembler")
sm_motor = component("sm_motor", (("em_motor", 2), ("graphite", 1)), (("ring", 3),), 3.0, "assembler")

circuit = component("circuit", None, (("copper", 0.5), ("iron", 1)), 0.5, "assembler")
si_circuit = component("si_circuit", None, (("copper", 1), ("silicon", 2)), 2.0, "assembler")
processor = component("processor", (("si_circuit", 2), ("circuit", 2)), None, 3.0, "assembler")
glass = component("glass", None, (("stone", 2),), 2.0, "smelter")
prism = component("prism", (("glass", 1.5),), None, 1.0, "assembler")
photon_combiner = component("photon_combiner", (("circuit", 1),), (("optical_crystal_grating", 1),),  3.0, "assembler")
graphene = component("graphere", None, (("fire_ice", 1),), 1.0, "chemical", (("hydrogen", 0.5),))
nanotube = component("nanotube", None, (("spinform", 1),), 2.0, "chemical")
titanium_glass = component("titanium_glass", (("glass", 1),), (("titanium", 1), ("water", 1)), 2.5, "assembler")
titanium_alloy = component("titanium_alloy", (("steel",1),), (("titanium", 1), ("sulphuric_acid", 2)), 3.0, "smelter")
titanium_crystal = component("titanium_crystal", None, (("titanium", 3), ("organic_crystal", 1)), 4.0, "assembler")
casmir_crystal = component("casmir_crystal", (("graphene", 2),), (("optical_crystal_grating", 4), ("hydrogen", 12)), 4.0, "assembler")
plane_filter = component("plane_filter", (("casmir_crystal", 1), ("titanium_glass", 2)), None, 12.0, "assembler")
quantum_chip = component("quantum_chip", (("plane_filter", 2), ("processor", 2)), None, 6.0, "assembler")
solar_sail = component("solar_sail", (("graphene", 0.5), ("photon_combiner", 0.5)), None, 2.0, "assembler")
frame = component("frame", (("nanotube", 4), ("titanium_alloy", 1)), (("silicon", 1),), 6.0, "assembler")
ds_component = component("ds_component", (("frame", 3), ("solar_sail", 3), ("processor", 3)), None, 8.0, "assembler")
deuterium_fuel = component("deuterium_fuel", (("titanium_alloy", 0.5), ("sm_motor", 0.5)), (("deuterium", 10),), 6.0, "assembler")
rocket = component("rocket", (("deuterium_fuel", 4), ("ds_component", 2), ("quantum_chip", 2)), None, 6.0, "assembler")

plasma = component("plasma", (("em_ring", 4), ("prism", 2)), None, 2.0, "assembler")
particle_container = component("particle_container", (("em_motor", 2),), (("copper", 2),), 4.0, "assembler")
particle_container_unipole = component("particle_container_unipole", None, (("copper", 2), ("unipole_magnet", 10)), 4.0, "assembler")
strange_matter = component("strange_matter", (("particle_container", 2),), (("iron", 2), ("deuterium", 10)), 8.0, "collider")
diamond = component("diamond", None, (("kimberlite", 0.5),), 0.75, "furnace")
graviton_lens = component("graviton_lense", (("diamond", 4), ("strange_matter", 1)), None, 6.0, "assembler")
ac_sphere = component("ac_sphere", (("strange_matter", 1), ("processor", 1)), None, 20.0, "assembler")
space_warper = component("space_warper", (("graviton_lense", 1)), None, 10.0, "replicator")
antimatter = component("antimatter", None, (("critical_photon", 1),), 1.0, "collider", (("hydrogen", 1),))
thruster = component("thruster", (("steel", 2),), (("copper", 3),), 4.0, "assembler")
logistic_drone = component("logistic_drone", (("thruster", 2), ("processor", 2)), (("iron", 5),), 4.0, "assembler")
reinforced_thruster = component("reinforced_thruster", (("titanium_alloy", 5), ("em_motor", 5)), None, 6.0, "assembler")
logistic_vessel = component("logistic_vessel", (("titanium_alloy", 10), ("processor", 10), ("reinforced_thruster", 2)), None, 6.0, "assembler")
foundation = component("foundation", (("steel", 1),), (("stone", 3),), 1.0, "assembler")
proliferator_mk1 = component("proliferator_mk1", None, (("coal", 1),), 0.5, "assembler")
proliferator_mk2 = component("proliferator_mk2", (("proliferator_mk1", 2), ("diamond", 1)), None, 1, "assembler")
proliferator_mk3 = component("proliferator_mk3", (("proliferator_mk2", 2), ("nanotube", 1)), None, 2, "assembler")
refined_oil = component("refined_oil", None, (("oil", 1),), 4.0, "refinery", (("hydrogen", 0.5),))
plastic = component("plastic", (("refined_oil", 2), ("graphite", 1)), None, 3.0, "chem")
silicon_crystal = component("silicon_crystal", None, (("fractal_silicon", 0.5),), 0.75, "smelter")
particle_broadband = component("particle_broadband", None, (("nanotube", 2), ("plastic", 1), ("silicon_crystal", 2)), 8.0, "assembler")

electromagnetic_matrix = component("electromagnetic_matrix", (("em_ring", 1), ("circuit", 1)), None, 3.0, "lab")
energy_matrix = component("energy_matrix", (("graphite", 2),), (("hydrogen", 2),), None, 6.0, "lab")
structure_matrix = component("structure_matrix", (("titanium_crystal", 1), ("diamond", 1)), None, 8.0, "lab")
information_matrix = component("information_matrix", (("processor", 2), ("particle_broadband", 1)), None, 10.0, "lab")
gravity_matrix = component("gravity_matrix", (("graviton_lens", 0.5), ("quantum_chip", 0.5)), None, 12.0, "lab")
white_matrix = component("white_matrix", (("electromagnetic_matrix", 1), ("energy_matrix", 1), ("structure_matrix", 1), ("information_matrix", 1), ("gravity_matrix", 1), ("antimatter", 1)), None, 1.0, "lab")


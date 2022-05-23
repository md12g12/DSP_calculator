# -*- coding: utf-8 -*-
"""
Created on Sun May  1 20:26:57 2022

@author: Matt
"""

from collections import Counter
from item_library import *


#%%
"""
functions for recursively finding all resources and building dependencies
"""


def get_resources(component):
    """
    Description
    ----------
    Uses recursion to find all the basic resources needed for a component. It stores resources in 
    the resource list and returns this once there are no resources left. Returns an empty list if 
    the component has no raw resources.
    
    Parameters
    ----------
    component : __main__.component
        Component from the item library that you want the base resources for building from scratch. 

    Returns
    -------
    resources : list
        Is a List of tuples, with each touple containing a resource and the quantity.

    """
    
    resources = []
    
    if globals()[component[0]].raw != None:
        
        for number in range(0, int(component[1])):
            resources.extend(globals()[component[0]].raw)
        if component[1]%1 != 0:
            for resource in globals()[component[0]].raw:
                resources.extend(((resource[0], resource[1]*(component[1]%1)),))
        return(resources)
        
    else:
        return(resources)

    
def get_components(component):
    """
    Description
    ----------
    Finds all the sub-components of for a given component and stores them in the components list 
    until there are no sub-components left.
    Returns an empty list if the component has no sub-components.
    Parameters
    ----------
    component : __main__.component
        Component from the item library that you want all the sub-components for building from scratch. 

    Returns
    -------
    components : list
        Is a List of tuples, with each touple containing a component and the quantity.
    """
    
    components = []
    
    if globals()[component[0]].components != None:
        
        for number in range(0,int(component[1])):
            components.extend(globals()[component[0]].components) 
        if component[1]%1 != 0:
            for sub_component in globals()[component[0]].components:
                components.extend(((sub_component[0], sub_component[1]*(component[1]%1)),))
        return(components)
    else:
        return(components)    
   

def get_dependencies(dependencies, components=[], resources=[]):
    """
    Description
    ----------
    Recursively calls get_components and get_resources on each component and sub-component within
    the entire crafting tree for a given item. It stores these in the componet and resources list,
    and removes an item from the dependency list once it has been exhausted all the way to raw 
    resources. If no dependencies are left it returns the list of components and resources.
    
    Parameters
    ----------
    dependencies : __main__.component
        Component from the item library that you want all the sub-components for building from scratch.
        Needs to be of the format [["item", quantity desired]].
        Must be a component and not a raw resource.

    Returns
    -------
    components : list 
        Is a List of tuples, with each touple containing a component and the quantity.
    resources : list 
        Is a List of tuples, with each touple containing a resource and the quantity.
    """

    if len(dependencies)==0:
        return(components, resources)
        
    else:
        for component in dependencies:
            components.extend(get_components(component))
            dependencies.extend(get_components(component))
            dependencies.remove(component)
            resources.extend(get_resources(component))
            return(get_dependencies(dependencies, components, resources))



#%%

if __name__ == "__main__":
    print((get_dependencies([["rocket", 1],],[],[])[0]))
    
    
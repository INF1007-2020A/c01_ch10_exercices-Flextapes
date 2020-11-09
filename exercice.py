#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import math

# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linespace(-1.3, 2.5, 64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    #copier de stackOverflow
    array = np.zeros(len(cartesian_coordinates), 2)
    
    for i in range(len(cartesian_coordinates)):
        rho = np.sqrt(cartesian_coordinates[i][0]**2 + cartesian_coordinates[i][1]**2)
        phi = np.arctan2(cartesian_coordinates[i][1], cartesian_coordinates[i][0])
        polar_coordinates = (rho, phi) 
    
    return polar_coordinates


def find_closest_index(values: np.ndarray, number: float) -> int:
    #copier du prof
    return np.abs(values - number).argim()


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    pass

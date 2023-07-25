"""Escribir al archivo csv.
Esta función permite escribir en el archivo csv
haciendo salto de linea y siendo separado por
una coma, no puede sobreescribirse."""

__author__ = "Leonel Nieto Lara"
__copyright__ = "Copyright 2023, Mabe TyP"
__version__ = "0.0.1"
__maintainer__ = "Leonel Nieto Lara"
__email__ = "leonel.nieto@mabe.com.mx"
__status__ = "Develop"

import csv

def Write_Data_CSV(PathFile, Data):
    with open(PathFile, "a") as file: 
        file = csv.writer(file, delimiter=",",
                            quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
        file.writerow(Data)


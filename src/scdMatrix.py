import enum
from constants import OMNISYNTH_PATH
import os
import numpy as np

# SCDMatrix
#
# SCDMatrix is a class that takes a flat list of SCD filenames
# and creates 2 dimensional matrix, with a max of 12 filenames
# per row and at most 4 rows total.

class SCDType(enum.Enum):
    patch = 1
    pattern = 2

def is_valid_scd_file(filename):
  return filename.endswith('.scd')

class SCDMatrix:
    MATRIX_WIDTH = 12
    MATRIX_LENGTH = 4
  
    def __init__(self, scd_type = SCDType.patch):
        self.scd_type = scd_type

    def get_matrix(self):
        files = filter(is_valid_scd_file, os.listdir(self.__get_scd_folder()))
        scd_list = filter(is_valid_scd_file, files)
        return np.array(scd_list).reshape(SCDMatrix.MATRIX_WIDTH, SCDMatrix.MATRIX_LENGTH)

    def __get_scd_folder(self):
        if self.scd_type == SCDType.patch:
            return OMNISYNTH_PATH + 'dsp/patches'
        elif self.scd_type == SCDType.pattern:
            return OMNISYNTH_PATH + 'dsp/patterns/songs/song1'
        else:
            # return patches location if scd type is invalid
            return OMNISYNTH_PATH + 'dsp/patches'
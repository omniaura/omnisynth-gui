import enum
from omniapp.constants import OMNISYNTH_PATH
import os


class SCDType(enum.Enum):
    patch = 1
    pattern = 2


def is_valid_scd_file(filename):
    return filename.endswith('.scd')


class SCDMatrix:
    """A class that takes a flat list of SCD filenames
    and creates 2 dimensional matrix, with a max of 12 filenames
    per row and at most 4 rows total.
    """

    MATRIX_WIDTH = 12
    MATRIX_LENGTH = 4

    def __init__(self, scd_type, omni_instance):
        self.scd_type = scd_type
        self.omni_instance = omni_instance

    def get_matrix(self):
        files = list(map(
            lambda fname: fname.strip('.scd'),
            list(filter(is_valid_scd_file,
                        os.listdir(self.__get_scd_folder())))))

        # dirty dirty dirty
        if self.scd_type == SCDType.patch:
            for idx, filename in enumerate(files):
                self.omni_instance.patchListIndex[filename] = idx
        else:
            for idx, filename in enumerate(files):
                self.omni_instance.patternListIndex[filename] = idx

        return [files[i:i+12] for i in range(0, len(files), 12)]

    def __get_scd_folder(self):
        if self.scd_type == SCDType.patch:
            return OMNISYNTH_PATH + 'patches'
        elif self.scd_type == SCDType.pattern:
            return OMNISYNTH_PATH + 'patterns/songs/song1'
        else:
            # return patches location if scd type is invalid
            return OMNISYNTH_PATH + 'patches'

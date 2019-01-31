"""
#############
# csvWriter #
#############
"""

# Import
import os
import fileinput #Iterate over lines from multiple input streams


# %% ____________________________________________________________________________________________________
#   ____________________________________________________________________________________________________
#   Functions

def fileWrite(path, fileName, data):
    """
    Write csv formatted data into file
    :param path: path where to create file
    :param fileName: fileName
    :param data: string to write un file
    :type path: str
    :type fileName: str
    :type data: str
    :return: return nothing
    :rtype: void
    """

    # %% Repertoire             # os.path.join(path, fileName) if needed
    os.chdir(path)

    # %% Creation et Ecriture
    f = open(fileName, 'w')
    f.writelines(data)
    f.close()

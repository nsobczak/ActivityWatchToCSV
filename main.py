"""
########
# main #
########
"""


#  ____________________________________________________________________________________________________
#  Config

# Import
import argparse
import jsonReader as jsonR
import csvWriter as csvW
import os



# %%____________________________________________________________________________________________________
#  ____________________________________________________________________________________________________
#  Initialization functions

def initVariables():
    """
    Init variable from command line
    :return: ARGS
    :rtype: list?
    """
    PARSER = argparse.ArgumentParser(description='ActivityWatch json file to csv file')
    # must
    PARSER.add_argument("pathToJsonFile", type=str, help="path where to json file is on the computer")
    # optionnal
    PARSER.add_argument("-cfp", "--csvFilePath", type=str, default="", help="path where to save the new csv file, default = where json file is")

    ARGS = PARSER.parse_args()

    # affichage des arguments rentres dans le log
    # logger.info(
    #     ":\npath to the directory where to save the downloaded website: %s\n" + \
    #     "url of the website to download: %s \npath to the configuration file of the logger: %s\n" + \
    #     "depth of the tree: %d\nmax size of a downloadable file: %d\nsize max of the directory where to download the website: %d\n",
    #     ARGS.savePath, ARGS.url, ARGS.logConf, ARGS.depth, ARGS.sizeFile, ARGS.sizeDirectory)

    return ARGS


# %%___________________________________________________________________________________________________
#  Fonctions principales

def loop(args):
    """
    Fonction principale
    :type logger: log
    :type args: list
    :return: 1
    :rtype: int
    """

    # Creation des dossiers necessaires
    jsonPath = args.pathToJsonFile

    return 1


# %%____________________________________________________________________________________________________
#  ____________________________________________________________________________________________________
def monMain():
    ARGS = initVariables()
    loop(ARGS)


if __name__ == "__main__":
    monMain()
"""
########
# main #
########
"""

#  ____________________________________________________________________________________________________
#  Config

# Import
import argparse
import jsonReadWrite as jsonR
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
    PARSER.add_argument("-cfp", "--csvFilePath", type=str, default="newGeneratedFile.csv", help="path where to save the new csv file, default = where json file is")
    PARSER.add_argument("-pj", "--printJson", type=bool, default=False, help="whether to print json content or not, default = false")
    #TODO: add printJsonFile to PARSER

    ARGS = PARSER.parse_args()

    # affichage des arguments rentres dans le log
    print(("\npath to the file to read: {} \n" + \
        "path where to save the csv file: {} \n" + \
        "printJson: {} \n").format(ARGS.pathToJsonFile, ARGS.csvFilePath, ARGS.printJson))

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
    jsonR.jsonReadWrite(args.pathToJsonFile, args.csvFilePath,  jsonR.Watcher.WINDOW, args.printJson)

    return 1


# %%____________________________________________________________________________________________________
#  ____________________________________________________________________________________________________
def monMain():
    ARGS = initVariables()
    loop(ARGS)


if __name__ == "__main__":
    monMain()
"""
##############
# jsonReader #
##############
"""

# Import
import os
import json
from platform import system
from enum import Enum


# %% ____________________________________________________________________________________________________
#   ____________________________________________________________________________________________________
#   Functions


class Watcher(Enum):
    AFK = 1
    WEB = 2
    WINDOW = 3

#TODO: group by day
def jsonRead(path, watcher, printJsonFile=False):
    """
    Write csv formatted data into file
    :param path: path where to create file
    :type path: str
    :param watcher: watcher type of the file
    :type watcher: Watcher
    :param printJsonFile: ???
    :type printJsonFile: bool
    :return: return csv formatted string
    :rtype: str
    """
    res = ""
    with open(path) as json_file:
        dataDict = json.load(json_file)

        if (system() != 'Linux' and system() != 'Windows'):
            print("{} operating system not supported".format(system()))
        else:
            print("{} operating system detected".format(system()))

        if printJsonFile:
            print(json.dumps(dataDict, indent=4))
            # # check
            # for d in dataDict:
            #     print('duration: ' + str(d['duration']))
            #     print('id: ' + str(d['id']))
            #     print('timestamp: ' + str(d['timestamp']))
            #     print('data: ' + str(d['data']))
            #     print('')


        if watcher == Watcher.AFK:
            print("watcher == Watcher.AFK")

            # duration: 956.016
            # id: 316
            # timestamp: 2019 - 01 - 28
            # T10: 28:13.770000 + 00: 00
            # data: {'status': 'not-afk'}


        elif watcher == Watcher.WEB:
            print("watcher == Watcher.WEB")

            # duration: 1.518
            # id: 3210
            # timestamp: 2019 - 01 - 31
            # T18: 01:45.794000 + 00: 00
            # data: {'title': 'New Tab', 'url': 'about:blank', 'audible': False, 'tabCount': 3, 'incognito': False}


        elif watcher == Watcher.WINDOW:
            print("watcher == Watcher.WINDOW")

            # duration: 4.017
            # id: 17
            # timestamp: 2019 - 01 - 28
            # T01: 11:55.570000 + 00: 00
            # data: {'title': 'Terminal - arch@ArchDesktop:~', 'app': 'Xfce4-terminal'} # <= app is the interesting thing


        else:
            print("failed to identify watcher type")

    return res

"""
##############
# jsonReader #
##############
"""

# Import
import json
from platform import system
from enum import Enum
from datetime import timedelta


# %% ____________________________________________________________________________________________________
#   ____________________________________________________________________________________________________
#   Functions


class Watcher(Enum):
    AFK = 1
    WEB = 2
    WINDOW = 3


def jsonReadWrite(pathToJson, pathWhereToCreateFile, watcher, printJsonFile=False):
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
    res = "file generated"
    with open(pathToJson) as json_file:
        dataDict = json.load(json_file)

        if (system() != 'Linux' and system() != 'Windows'):
            print("{} operating system not supported".format(system()))
        else:
            print("{} operating system detected".format(system()))

        if printJsonFile:
            print(json.dumps(dataDict, indent=4))

        csvFile = open(pathWhereToCreateFile, "w")  # "w" to write strings to the file

        if watcher == Watcher.AFK:
            print("watcher == Watcher.AFK")

            # duration: 956.016
            # id: 316
            # timestamp: 2019 - 01 - 28
            # T10: 28:13.770000 + 00: 00
            # data: {'status': 'not-afk'}

            res = "Watcher.AFK detected => does nothing"


        elif watcher == Watcher.WEB:
            print("watcher == Watcher.WEB")

            # duration: 1.518
            # id: 3210
            # timestamp: 2019 - 01 - 31
            # T18: 01:45.794000 + 00: 00
            # data: {'title': 'New Tab', 'url': 'about:blank', 'audible': False, 'tabCount': 3, 'incognito': False}

            res = "Watcher.WEB detected => does nothing"


        elif watcher == Watcher.WINDOW:
            print("watcher == Watcher.WINDOW")
            # duration: 4.017 # <= in seconds
            # id: 17
            # timestamp: 2019 - 01 - 28
            # T01: 11:55.570000 + 00: 00
            # data: {'title': 'Terminal - arch@ArchDesktop:~', 'app': 'Xfce4-terminal'} # <= app is the interesting thing

            # if printJsonFile:
            #     # check
            #     for d in dataDict:
            #         print('duration: ' + str(d['duration']))
            #         print('id: ' + str(d['id']))
            #         print('timestamp: ' + str(d['timestamp']))
            #         print('data: ' + str(d['data']))
            #         print('  title: ' + str(d['data']['title']))
            #         print('  app: ' + str(d['data']['app']))
            #         print('')

            handleWindowWatcher(csvFile, dataDict)


        else:
            res = "failed to identify watcher type"

    print(res)
    return res


def handleWindowWatcher(csvFile, dataDict):
    columnTitleRow = "date; app; duration(s); duration(h:m:s)\n"
    csvFile.write(columnTitleRow)

    sortedData = {}
    for d in dataDict:
        # timestamp only beginning: "2019-01-28T01:11:32.482000+00:00"
        date = str(d['timestamp'])[:10]

        if not (date in sortedData):
            sortedData[date] = {}

        app = str(d['data']['app'])
        if not (app in sortedData[date]):
            sortedData[date][app] = 0

        duration = float(d['duration'])
        sortedData[date][app] += duration

    rows = ""
    for keyDate, valueAppDict in sortedData.items():
        for keyApp, valueDuration in valueAppDict.items():
            # date
            rows += keyDate + "; "
            # app
            rows += keyApp + "; "
            # duration
            valueDurationStr = str(valueDuration)
            leftPart, righPart = valueDurationStr.split('.')
            valueDurationStr = leftPart + "," + righPart[:3]
            rows += valueDurationStr + "; "
            rows += str(timedelta(seconds=valueDuration)) + "\n"

    csvFile.write(rows)

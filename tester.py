#! /usr/bin/env python3

from src.C3PO import C3PO

EMPIRE_FOLDER = "test/empire/"
MILLENNIUM_FALCON_FOLDER = "./test/millennium-falcon/"

expectedOddsDict = {
    "empire1.json": 0,
    "empire2.json": 0.81,
    "empire3.json": 0.9,
    "empire4.json": 1,
    "empiteError.json": 1
}


if __name__ == "__main__":
        milleniumFalconJsonPath = MILLENNIUM_FALCON_FOLDER + 'millennium-falcon.json'
        try:
            testC3PO = C3PO(milleniumFalconJsonPath)
        except Exception as e:
            print(e)
            exit()

        for fileName in expectedOddsDict.keys():
            try:
                testedFilePath = EMPIRE_FOLDER + fileName
                expectedOdds = expectedOddsDict[fileName]
                odds = testC3PO.giveMeTheOdds(testedFilePath)
                if odds != expectedOdds:
                    print(f"{testedFilePath} TEST FAILED ❌: expected odds: {expectedOdds}; obtain: {odds}")
                else:
                    print(f"{testedFilePath} TEST PASSED ✅")
            except Exception as e:
                print(e)
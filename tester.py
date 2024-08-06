#! /usr/bin/env python3

from src.C3PO import C3PO

EMPIRE_FOLDER = "./test/empire/"
MILLENNIUM_FALCON_FOLDER = "./test/millennium-falcon/"

testList = [
    {
        "empireFile":"empire1.json",
        "millenniumFalconFile":"millennium-falcon1.json",
        "odds": 0
    },
    {
        "empireFile":"empire2.json",
        "millenniumFalconFile":"millennium-falcon2.json",
        "odds": 0.81
    },
    {
        "empireFile":"empire3.json",
        "millenniumFalconFile":"millennium-falcon3.json",
        "odds": 0.9
    },
    {
        "empireFile":"empire4.json",
        "millenniumFalconFile":"millennium-falcon4.json",
        "odds": 1
    },
    {
        "empireFile":"empire5.json",
        "millenniumFalconFile":"millennium-falcon5.json",
        "odds": 0.9
    },
    {
        "empireFile":"empire6.json",
        "millenniumFalconFile":"millennium-falcon6.json",
        "odds": 1
    },
    {
        "empireFile":"empire7.json",
        "millenniumFalconFile":"millennium-falcon7.json",
        "odds": 1
    },
    {
        "empireFile":"empire8.json",
        "millenniumFalconFile":"millennium-falcon8.json",
        "odds": 1
    },
    {
        "empireFile":"empire9.json",
        "millenniumFalconFile":"millennium-falcon9.json",
        "odds": 0.81
    },
    {
        "empireFile":"empireError.json",
        "millenniumFalconFile":"millennium-falcon5.json",
        "odds": 0
    },

]

def runTest(millenniumFalconJsonFileName, empireJsonFileName, expectedOutput):
        millenniumFalconJsonPath = MILLENNIUM_FALCON_FOLDER + millenniumFalconJsonFileName
        try:
            testC3PO = C3PO(millenniumFalconJsonPath)
        except Exception as e:
            print(f"{millenniumFalconJsonPath} TEST FAILED ❌: exception catched: {type(e).__name__} {e}")
            return

        try:
            testedFilePath = EMPIRE_FOLDER + empireJsonFileName
            output = testC3PO.giveMeTheOdds(testedFilePath)
            if output != expectedOutput:
                print(f"{testedFilePath} TEST FAILED ❌: expected odds: {expectedOutput}; obtained: {output}")
            else:
                print(f"{testedFilePath} TEST PASSED ✅")
        except Exception as e:
            print(f"{testedFilePath} TEST FAILED ❌: exception catched: {type(e).__name__} {e}")
            return

if __name__ == "__main__":
        for test in testList:
            millenniumFalconJsonFileName = test["millenniumFalconFile"]
            empireJsonFileName = test["empireFile"]
            expectedOutput = test["odds"]
            runTest(millenniumFalconJsonFileName, empireJsonFileName, expectedOutput)


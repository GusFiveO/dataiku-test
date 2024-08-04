import json

def loadJsonFile(jsonFilePath):
    with open(jsonFilePath, 'r') as jsonFile:
        jsonFile = json.load(jsonFile)
        return jsonFile

def computeOdds(daysOnBountyHunterPlanet):
   if daysOnBountyHunterPlanet is None:
      return 0
   odds = 1
   for i in range(daysOnBountyHunterPlanet):
      odds -= (9 ** i) / (10 ** (i + 1))
   return odds

def isBountyHuntersPresent(planet, day, bountyHuntersList):
   for bountyHunter in bountyHuntersList:
      if bountyHunter["planet"] == planet and bountyHunter["day"] == day:
         return True
   return False

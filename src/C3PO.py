from src.utils import computeOdds, isBountyHuntersPresent, loadJsonFile
from src.MillenniumFalcon import MillenniumFalcon
from copy import copy


class C3PO:
   def __init__(self, millenniumFalconJsonFilePath):
      millenniumFalconJson = loadJsonFile(millenniumFalconJsonFilePath) 

      self.routes = millenniumFalconJson["routes"]
      self.milleniumFalcon = MillenniumFalcon("Tatooine", millenniumFalconJson["autonomy"])

      self.currentDay = 0
      self.bestRouteRiskDays = None
       
   def giveMeTheOdds(self, empireJsonFilePath):
      empireJson = loadJsonFile(empireJsonFilePath)
      countdown = empireJson["countdown"]
      bountyHunters = empireJson["bounty_hunters"]

      riskDays = 0
      self.computeNextTravel(riskDays, self.milleniumFalcon, countdown, bountyHunters)
      odds = computeOdds(self.bestRouteRiskDays)
      self.bestRouteRiskDays = None
      return odds

   def updateBestRouteRiskDays(self, riskDays):
    if self.bestRouteRiskDays is None or self.bestRouteRiskDays > riskDays:
        self.bestRouteRiskDays = riskDays


   def computeNextTravel(self, riskDays, millenniumFalcon: MillenniumFalcon, countdown, bountyHuntersList):
      if self.bestRouteRiskDays is not None and riskDays > self.bestRouteRiskDays:
         return
      if millenniumFalcon.getTravelDay() > countdown:
         return
      if millenniumFalcon.getPlanet() == "Endor":
         self.updateBestRouteRiskDays(riskDays)
         return
      currentRiskDays = riskDays
      if isBountyHuntersPresent(millenniumFalcon.getPlanet(), millenniumFalcon.getTravelDay(), bountyHuntersList):
         currentRiskDays += 1
      for route in self.routes:
         millenniumFalconCopy = copy(millenniumFalcon)
         origin = route["origin"]
         destination = route["destination"]
         travelTime = route["travelTime"]
         if origin != millenniumFalconCopy.getPlanet():
            continue
         if millenniumFalconCopy.getAutonomy() < travelTime:
            millenniumFalconCopy.refuel()
            if isBountyHuntersPresent(millenniumFalconCopy.getPlanet(), millenniumFalconCopy.getTravelDay(), bountyHuntersList):
               currentRiskDays += 1
         millenniumFalconCopy.travelTo(destination, travelTime)
         self.computeNextTravel(currentRiskDays, millenniumFalconCopy, countdown, bountyHuntersList)
         millenniumFalconCopy.reset(origin, travelTime)
         while millenniumFalconCopy.getTravelDay() + travelTime < countdown:
            millenniumFalconCopy.waitOrRefuel()
            self.computeNextTravel(currentRiskDays, millenniumFalconCopy, countdown, bountyHuntersList)
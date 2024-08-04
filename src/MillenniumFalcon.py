class MillenniumFalcon:
    
    def __init__(self, startPlanet, maxAutonomy):
        self.planet = startPlanet
        self.maxAutonomy = maxAutonomy
        self.autonomy = maxAutonomy
        self.travelDay = 0

    def refuel(self):
        self.autonomy = self.maxAutonomy
        self.travelDay += 1
    
    def travelTo(self, destinationPlanet, travelTime):
        if self.autonomy >= travelTime:
            self.planet = destinationPlanet
            self.autonomy -= travelTime
            self.travelDay += travelTime
            return True
        return False

    def wait(self):
        self.travelDay += 1


    def getTravelDay(self):
        return self.travelDay

    def getPlanet(self):
        return self.planet

    def getAutonomy(self):
        return self.autonomy
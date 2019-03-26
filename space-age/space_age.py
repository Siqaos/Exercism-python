EARTH_SEC = 31557600
MERCURY = 0.2408467 
VENUS = 0.61519726
MARS = 1.8808158 
JUPITER = 11.862615 
SATURN = 29.447498 
URANUS = 84.016846 
NEPTUNE = 164.79132  


class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds
        self.earthsec = seconds / EARTH_SEC
        
    def on_mercury(self):
        return round( self.earthsec / MERCURY,2)
    def on_earth(self):
        return round(self.earthsec,2)
    def on_mars(self):
        return round(self.earthsec / MARS,2)
    def on_jupiter(self):
        return round(self.earthsec / JUPITER,2)
    def on_saturn(self):
        return round(self.earthsec / SATURN,2)
    def on_uranus(self):
        return round(self.earthsec  / URANUS,2)
    def on_neptune(self):
        return round(self.earthsec / NEPTUNE,2)
    def on_venus(self):
        return round(self.earthsec / VENUS,2)

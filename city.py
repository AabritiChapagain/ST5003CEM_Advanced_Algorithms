class City:
    """
    Represents a city used in the route planning application.
    """

    def __init__(self, name, latitude, longitude, population, distance):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.population = population
        self.distance = distance

    def __str__(self):
        return (
            f"City: {self.name}\n"
            f"Coordinates: ({self.latitude}, {self.longitude})\n"
            f"Population: {self.population}\n"
            f"Distance: {self.distance} km"
        )
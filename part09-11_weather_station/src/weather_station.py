# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, station: str):
        self.__station = station
        self.__observation: list[str] = []

    def latest_observation(self):
        if not self.__observation:
            return ""
        else:
            return self.__observation[-1]

    def number_of_observations(self):
        if not self.__observation:
            return 0
        else:
            return len(self.__observation)

    def __str__(self):
        return f"{self.__station}, {self.number_of_observations()} observations"

    def add_observation(self, observation: str):
        if observation != "":
            self.__observation.append(observation)
        else:
            raise ValueError("Empty Observation...")


if __name__ == "__main__":
    a = WeatherStation("Kumpula")
    m = a.number_of_observations()

from Plants import Plant

class Garden:
    def __init__(self, plants: [Plant]):
        """
            Initializes the garden with a list of plants.
        """
        self.plants = plants

    def __add__(self, plant: Plant):
        """
            Adds a single plant to the garden.
        """
        self.plants.append(plant)

    def add_day(self):
        """
            Simulates the passage of one day for all plants in the garden.
        """
        for plant in self.plants:
            plant.add_day()

    def get_name_plants(self):
        """
            Returns a string with the names of all plants in the garden.
        """
        result = ""
        for plant in self.plants:
            result += plant.get_name()
        print(result)

    def get_report(self):
        """
            Generates a detailed report of the garden's plants.
        """
        report = ""
        for plant in self.plants: report += f'{plant}\n\n'
        return report
from Plants import Plant

class Garden:
    def __init__(self, plants: [Plant]):
        self.plants = plants

    def __add__(self, plant: Plant):
        self.plants.append(plant)

    def add_day(self):
        for plant in self.plants:
            plant.add_day()

    def get_name_plants(self):
        result = ""
        for plant in self.plants:
            result += plant.get_name()
        print(result)


    def get_report(self):
        report = ""
        for plant in self.plants: report += f'{plant}\n\n'
        return report
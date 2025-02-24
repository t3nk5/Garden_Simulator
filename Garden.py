from Plants import Plant

class Garden:
    def __init__(self, plants: [Plant]):
        self.plants = plants


    def add_day(self):
        for plant in self.plants:
            plant.add_day()



    def get_report(self):
        report = ""
        for plant in self.plants: report += f'{plant}\n\n'

        return report
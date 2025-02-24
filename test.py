from Plants.Flower import Flower
from Plants.Tree import AppleTree
from Garden import Garden

def test():
    flower = Flower(5, 10, 5, 0.2, 50, "red")
    apple_tree = AppleTree(5, 7, 4, 0.07, 150)

    garden = Garden([flower,apple_tree])
    print(garden.get_report())

    flower.give_water(6)
    flower.change_light(8)
    flower.add_fertilizer(3)

    flower.cut_plant()
    print(garden.get_report())



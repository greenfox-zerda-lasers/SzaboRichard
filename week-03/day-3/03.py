# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class Pirate():
    v = 0

    def drink_rum(self):
        self.v += 1
        
    def hows_goin_mate(self):
        if self.v >= 5:
            return "Arrrrr!"
        else:
            return "Nothin'"

pr = Pirate()
pr.drink_rum()
pr.drink_rum()
pr.drink_rum()
pr.drink_rum()
pr.drink_rum()
pr.drink_rum()
print(pr.hows_goin_mate())

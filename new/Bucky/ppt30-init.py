class enemy:

    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = enemy(5)
bucky = enemy(10)

jason.get_energy()

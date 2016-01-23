class mario():

    def move(self):
        print('I am moving')

class shroom():

    def eat(self):
        print('Shroom shroom ')

class bigMario(mario, shroom):
    pass


bm = bigMario()
bm.eat()
bm.move()
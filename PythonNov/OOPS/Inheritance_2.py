class P1:
    def __init__(self):
        self.x = 10
        self.y = 20
        print("Class P1 called...")

    def show(self):
        print("Show called of P1...")

class P2:
    def __init__(self):
        self.x = 50
        self.y = 70
        print("Class P2 called...")

    def show(self):
        print("Show called of P2...")

class Child(P1, P2):
    def __init__(self):
        super().__init__()
        P2.__init__(self)

    # def show(self):
    #     print("Show called of Child")
    #     print(self.x, self.y)

obj = Child()
obj.show()

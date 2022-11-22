class Toto:
    def __init__(self,name) -> None:
        self.name = name
    def hello(self, b):
        print(b.name)
    def lol():
        print("lol")

u = Toto("Jean")
u.hello(u)

a = Toto("vlad")
a.hello(u)
Toto.lol()
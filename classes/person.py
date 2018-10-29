class Person:
    def __init__(self, pname, pgenre):
        self.pname = pname
        self.pgenre = pgenre
        self.probot_Owned = None

    def introduce_self(self):

        print("Hello, i'm a " + self.pgenre )

        if self.probot_Owned is None:
            print("I have no robots yet, i need one to play!!")

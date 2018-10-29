class Robot:
    def __init__(self, rname, rcolor, rweight):
        self.rname = rname
        self.rweight = rweight
        self.rcolor = rcolor

    def introduce_self(self):
        print("Hello, i'am " + self.rname)

class Developer:
    def __init__(self, name, language):
        self.name = name
        self.language = language
    
    def introduce(self):
        return f"Men {self.name}, {self.language} dasturchi"

dev = Developer("Ulugbek", "Python")
print(dev.introduce())

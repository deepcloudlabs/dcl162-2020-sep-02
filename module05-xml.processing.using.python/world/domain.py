class Country:
    def __init__(self):
        self.code = ""
        self.name = ""
        self.population = ""
        self.continent = ""
        self.surfaceArea = ""

    def __str__(self):
        return f"Country [code= {self.code}, name= {self.name}, continent= {self.continent}, population= {self.population}]"

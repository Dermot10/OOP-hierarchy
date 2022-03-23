class Nation:
    def __init__(self, country, theme, speciality):
        self.country = country
        self.theme = theme
        self.speciality = speciality

    def __repr__(self):
        print(self.__dict__)


class CO(Nation):
    def __init__(self, country, theme, speciality, commander, power, superpower, hits, misses, comrades=None, compatriots=None):
        super().__init__(country, theme, speciality)
        self.commander = commander
        self.power = power
        self.superpower = superpower
        self.hits = hits
        self.misses = misses
        self.comrades = None
        self.compatriots = None

    # dictionary represention of the object.
    def __repr__(self):
        print(self.__dict__)

    # Method to add
    def add_comrades(self, c):
        if self.comrades is None:
            self.comrades = []
            self.comrades.append(c)
        elif c not in self.comrades:
            self.comrades.append(c)
        else:
            self.comrades = comrades

    # Set data member as list
    def add_compatriots(self, a=[]):
        if self.compatriots is None:
            self.compatriots = a
        else:
            return

    def co_powers(self):
        return (f"Power: {self.power}, Superpower: {self.superpower}")

    def preferences(self):
        return (f"Hits: {self.hits}, Misses: {self.misses}")

    def compatriots(self):
        return self.compatriots

    def comrades(self):
        return self.comrades


class Commander(CO):
    def __init__(self, country, leader, theme, speciality, power, superpower, hits, misses, comrades=None, compatriots=None, subordinates=None):
        super().__init__(country, leader, theme, speciality, power,
                         superpower, hits, misses, comrades=None, compatriots=None)
        self.subordinates = None

    def __repr__(self):
        print(self.__dict__)

    # Instantiate dict and set values as list of input
    def add_subordinates(self, a=[]):
        if self.subordinates is None:
            self.subordinates = {}
            self.subordinates["Subordinates"] = a
        else:
            return


orange = Nation("Orange Star", "USA", "Direct Warefare, Frontal Assaults")
print("Nation:")
orange.__repr__()
print("")


Andy = CO("Orange Star", "USA", "Fixing Damaged Units", "Nell",
          "Hyper Repair", "Hyper Upgrade", "Mechanic", "Waking Up Early")
Andy.add_comrades('Eagle')
Andy.add_comrades('Max')
Andy.add_comrades('Hawke')
Andy.add_compatriots(["Max", "Sami", "Nell", "Rachel", "Jake", "Hachi"])
print("Commanding Officer Andy:")
Andy.__repr__()
print("")


Nell = Commander("Orange Star", "USA", "High Luck", "N/A",
                 "Lucky Star", "Lady Luck", "Willful Students", "Downtime")
Nell.add_comrades("Rachel")
Nell.add_compatriots(["Andy", "Max", "Sami", "Rachel", "Jake", "Hachi"])
Nell.add_subordinates(["Andy", "Max", "Sami", "Rachel", "Jake"])
print("Commander-in-Chief Nell:")
Nell.__repr__()

# these are the main stats some fall under the more general stats ie population and manpower:
#money, population, land_size, approval, Loyalty, Natural_reasources, manpower, importing, exporting
class KingdomStats:
    MAN_POWER_RATIO = 0.65
    EMPLOYED_RATE = 0.8
    UNEMPLOYED_RATE = 0.2
    HIGH_TAX = 0.5
    MEDIUM_TAX = 0.3
    LOW_TAX = 0.1
    MAX_APPROVAL = 100
    MIN_APPROVAL = -100

    def __init__(self, name='Barbarian', money=0, population=0, land_size=0, approval=50, loyalty=50, natural_resources=0, revolt_chance=0):
        self.name = name
        self.money = money
        self.population = population
        self.land_size = land_size
        self.approval = approval
        self.loyalty = loyalty
        self.revolt = revolt_chance

        self.manpower = int(self.population * self.MAN_POWER_RATIO)
        self.employed = int(self.manpower * self.EMPLOYED_RATE)
        self.unemployed = int(self.manpower * self.UNEMPLOYED_RATE)

        self.natural_resources = {
            'wood': natural_resources,
            'stone': natural_resources,
            'iron': 0,
            'food': natural_resources/2
        }
        self.importing = {}
        self.exporting = {}
    
    def update_population(self, amount):
        if amount <= 0:
            raise ValueError('Sorry Can"t go into negative numbers!')
        else:
            self.population += amount
            self.manpower = int(self.population * self.MAN_POWER_RATIO)
            self.employed = int(self.manpower * self.EMPLOYED_RATE)
            self.unemployed = int(self.manpower * self.UNEMPLOYED_RATE)


    def tax(self, tax_rate):
        employed_tax = int(self.employed * tax_rate)
        self.money += employed_tax
        return self.money
    
    def approval_change(self,tax_rate):
        if self.approval >= self.MAX_APPROVAL or self.approval <= self.MIN_APPROVAL:
            return "Can't go above or below cap"
        
        if tax_rate >= self.HIGH_TAX:
            self.approval -= 10
        elif tax_rate >= self.MEDIUM_TAX:
            self.approval -= 5
        elif tax_rate >= self.LOW_TAX:
            self.approval += 5
        else:
            self.approval += 10

        if self.approval <= 0:
            pass

    def _exporting(self,amount, trade_partner, resource):
        if resource not in self.natural_resources:
            raise KeyError("Can't trade resource you don't have!!!")
        
        if amount > self.natural_resources[resource]:
            raise ValueError("Don't have enough of the resource")
        
        self.natural_resources[resource] -= amount

        if trade_partner.name not in self.exporting:
            self.exporting[trade_partner.name] = {}

        current = self.exporting[trade_partner.name].get(resource, 0)
        self.exporting[trade_partner.name][resource] = current + amount


    def __str__(self):
        nr = ', '.join(f"{k}: {v}" for k, v in self.natural_resources.items())
        importing = ', '.join(f"{k}: {v}" for k, v in self.importing.items()) or "None"
        exporting = ', '.join(
            f"{partner}: {{ {', '.join(f'{r}: {amt}' for r, amt in res.items())} }}"
            for partner, res in self.exporting.items()
        ) or "None"

        return (
            f"Kingdom: {self.name}\n"
            f"Money: {self.money}\n"
            f"Population: {self.population}\n"
            f"Land size: {self.land_size}\n"
            f"Approval: {self.approval}\n"
            f"Loyalty: {self.loyalty}\n"
            f"Revolt chance: {self.revolt}\n"
            f"Manpower: {self.manpower} (employed: {self.employed}, unemployed: {self.unemployed})\n"
            f"Natural resources: {nr}\n"
            f"Importing: {importing}\n"
            f"Exporting: {exporting}\n"
        )
    
uk = KingdomStats(name='uk',natural_resources=100)
france = KingdomStats(name='france',natural_resources=100)

while uk.natural_resources['wood'] > 0 and france.natural_resources['stone'] > 0:
    uk._exporting(10,france,'wood')
    france._exporting(5,uk,'stone')
    print(uk)
    print(france)
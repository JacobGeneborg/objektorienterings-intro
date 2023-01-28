# Klasser namnges alltid med inledande stor bokstav.
class Airplane():
    '''
    En klass som håller reda på några egenskaper hos ett flygplan.
    '''
    # Metoden __init__, körs alltid då ett objekt skapas

    def __init__(self, model, wingspan, capacity):
        # Nedanstående variabler kallas för attribut.
        # Alla objekt av klassen Airplane har egna värden på dessa.
        self.model = model
        self.wingspan = wingspan
        self.capacity = capacity

    def print_info(self):
        '''
        Skriver ut information om ett flygplan (en instans av klassen Airplane).
        '''
        print(
            f"{self.model}. Wingspan: {self.wingspan}. Capacity: {self.capacity}")

    def set_wingspan(self, new_wingspan):
        self.wingspan = new_wingspan
    
    def set_capacity(self, new_capacity):
        self.capacity = new_capacity

    def get_capacity(self):
        return self.capacity
        

        



# ----------Huvudprogram----------
# Nu när klassen finns kan vi skapa objekt (variabler) med denna typ.
# Dessa objekt har också tillgång till klassens metoder (funktioner).
a_plane = Airplane("Boeing 747", 64.6, 500)
a_plane.model = 'Airbus 380'
a_plane.print_info()

b_plane = Airplane("JAS 39 Gripen", 8.4, 2)
b_plane.model = "Stritsplan"
b_plane.print_info()

c_plane = Airplane("art 72", 27, 74)
c_plane.model = 'Airbus'
c_plane.print_info()


a_plane.set_wingspan(70)
a_plane.set_capacity(400)
a_plane.print_info()

b_plane.set_wingspan(10)
b_plane.set_capacity(1)
b_plane.print_info()

the_capacity=a_plane.get_capacity()
print(the_capacity)


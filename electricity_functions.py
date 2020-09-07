#constants:
#constants:
a_electron = 1.6 * 10**-19
a_coulomb = 6.25 * 10**18
a_ampere = 6 * 10**18

#METHODS:

def electric_charge(current, time):
    Q = current * time
    return f"{Q} coulombs"

def electric_current(charge, time):
    I = charge / time
    return f"{I} amperes"

def electric_potential(work, charge):
    V = work / charge
    return f"{V} volts"

def Coulomb_to_electrons(no_of_coulombs, a_coulomb=(6.25 * 10**18)):
    electrons = no_of_coulombs * a_coulomb
    return f"{electrons} electrons"

def electrons_to_Coulombs(no_of_electron, a_coulomb=(6.25 * 10**18)):
    Coulombs = no_of_electron / a_coulomb
    return f"{Coulombs} coulombs"

def Amperes_to_electrons(no_of_amperes, a_ampere=6 * 10**18):
    electrons_a = no_of_amperes * a_ampere
    return f"{electrons_a} electrons"

def electrons_to_Amperes(no_of_electron, a_ampere=6 * 10**18):
    amperes_a = no_of_electron / a_ampere
    return f"{amperes_a} amperes"

#DOCUMENTATION (README):
# the 'electric_charge' function takes 2 arguments: current(in Amperes) and time(in Seconds) and returns charge(in Coulombs)
# the 'electric_current' function takes 2 arguments: charge(in Coulombs) and time(in Seconds) and returns current(in Amperes)
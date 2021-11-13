from enum import Enum

#ble lagd for å utelukke skrivefeil da man skal skrive disse tingene så mange ganger. Så spesielt en risiko for å skrive høyre feil
class Retning(Enum):
    HOYRE = "hoeyre"
    VENSTRE = "venstre"
    OPP = "opp"
    NED = "ned"

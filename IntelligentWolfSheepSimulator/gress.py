
class Gress:
    # fjernete et parameter da jeg ikke synes det var nødvendig å ta inn et bilde, når gresset har samme bilde hver gang
    def __init__(self, posisjon_venstre, posisjon_topp):
        self._posisjon_venstre = posisjon_venstre
        self._posisjon_topp = posisjon_topp
        self._bilde = "gress.png"
        self._er_spist = False

    def blir_spist(self):
        self._er_spist = True

    def er_spist(self):
        return self._er_spist

    def tegn(self, skjerm):
        skjerm.blit(self._bilde, (self._posisjon_venstre, self._posisjon_topp))

    def hent_posisjon_venstre(self):
        return self._posisjon_venstre

    def hent_posisjon_topp(self):
        return self._posisjon_topp

    def rute_venstre(self):
        return self._posisjon_venstre // 50

    def rute_topp(self):
        return self._posisjon_topp // 50
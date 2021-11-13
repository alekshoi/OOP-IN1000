from math import inf
from retning import Retning
import random


class Sauehjerne:
    def __init__(self, sau, spillbrett):
        self._sau = sau
        self._spillbrett = spillbrett

    def avstand_til_objekt(self, objekt):
        # henter avstanden i hvert plan, X og Y
        avstand_venstre = self._sau.rute_venstre() - objekt.rute_venstre()
        avstand_topp = self._sau.rute_topp() - objekt.rute_topp()
        # tar absoluttverdien, da avstanden er posistiv uansett
        avstand_objekt = abs(avstand_venstre) + abs(avstand_topp)
        return avstand_objekt

    def retninger_ift_objekt(self, objekt, mot):
        retninger = []
        avstand_venstre = self._sau.rute_venstre() - objekt.rute_venstre()
        avstand_topp = self._sau.rute_topp() - objekt.rute_topp()

        # flipper fortegn hvis vi vil vekk fra objekt
        """if not mot:
            avstand_venstre = -avstand_venstre
            avstand_topp = -avstand_topp
        """    
        avstand_venstre = avstand_venstre if mot else -avstand_venstre
        avstand_topp = avstand_topp if mot else -avstand_topp
        
        # legger til mulige retninger fra/mot objektet i listen retninger
        if avstand_topp > 0:
            retninger.append(Retning.OPP)
        if avstand_topp < 0:
            retninger.append(Retning.NED)
        if avstand_venstre > 0:
            retninger.append(Retning.VENSTRE)
        if avstand_venstre < 0:
            retninger.append(Retning.HOYRE)
        return retninger

    def retninger_mot_objekt(self, objekt):
        return self.retninger_ift_objekt(objekt, mot=True)

    def retninger_fra_objekt(self, objekt):
        # hvis mot er False, gjøres metoden motsatt vei
        return self.retninger_ift_objekt(objekt, mot=False)

    def naermeste_gress(self):
        # lager avstanden max stor
        naermeste_avstand = (inf)
        naermeste_gress = None
        antall_spiste_gress = 0
        for gress in self._spillbrett.hent_gress():
            if gress.er_spist():
                # hvis alle sauer er spist returnerer metoden ingenting
                antall_spiste_gress += 1
                if antall_spiste_gress >= len(self._spillbrett.hent_gress()):
                    return None
            else:
                if self.avstand_til_objekt(gress) < naermeste_avstand:
                    naermeste_avstand = self.avstand_til_objekt(gress)
                    naermeste_gress = gress
        return naermeste_gress

    def velg_retning(self):
        # denne delen returnerer den mest "populære" retningen. Retninger fra ulven teller dobbelt dersom avstanden er 6 eller mindre
        retninger = []
        naermeste_gress = self.naermeste_gress()
        retninger_mot_gress = self.retninger_mot_objekt(naermeste_gress)
        retninger.extend(retninger_mot_gress)
        ulven = self._spillbrett.ulv()
        if self.avstand_til_objekt(ulven) <= 6:
            retninger_vekk_fra_ulv = self.retninger_fra_objekt(ulven)
            retninger_vekk_fra_ulv = retninger_vekk_fra_ulv*2
            retninger.extend(retninger_vekk_fra_ulv)
        retning_med_hoyest_verdi = finn_vanligste_element_i_liste(retninger)
        valgt_retning = retning_med_hoyest_verdi

        # sjekker mot kantene. Man kan ikke gå fra ulven gjennom veggen. 
        if self._sau.rute_venstre() == 17 and retning_med_hoyest_verdi == Retning.HOYRE:
            valgt_retning = Retning.NED
        elif self._sau.rute_topp() == 0 and retning_med_hoyest_verdi == Retning.OPP:
            valgt_retning = Retning.HOYRE
        elif self._sau.rute_venstre() == 0 and retning_med_hoyest_verdi == Retning.VENSTRE:
            valgt_retning = Retning.OPP
        elif self._sau.rute_topp() == 13 and retning_med_hoyest_verdi == Retning.NED:
            valgt_retning = Retning.VENSTRE

        mulige_retninger = [Retning.NED, Retning.HOYRE,
                            Retning.OPP, Retning.VENSTRE]

        #sjekker mot steiner og veggen
        if self.stein_finnes_i_retning(valgt_retning):
            for retning in mulige_retninger:
                if not self.hinder_finnes_i_retning(retning):
                    valgt_retning = retning
        return valgt_retning

    def stein_finnes_i_retning(self, retning):
        sau_rute_venstre = self._sau.rute_venstre()
        sau_rute_topp = self._sau.rute_topp()
        differanse_topp = 0
        differanse_venstre = 0
        # går gjennom listen av steiner som vi henter fra spillbrett
        for stein in self._spillbrett.hent_steiner():
            stein_rute_venstre = stein.rute_venstre()
            stein_rute_topp = stein.rute_topp()
            differanse_venstre = sau_rute_venstre - stein_rute_venstre
            differanse_topp = sau_rute_topp - stein_rute_topp
            # steinen må være en unna i en av retningene og være på samme plan i den andre retningen og ha retning mot steinen med avstanden 1. 
            if differanse_topp == 1 and differanse_venstre == 0 and retning == Retning.OPP:
                return True
            elif differanse_topp == -1 and differanse_venstre == 0 and retning == Retning.NED:
                return True
            elif differanse_venstre == 1 and differanse_topp == 0 and retning == Retning.VENSTRE:
                return True
            elif differanse_venstre == -1 and differanse_topp == 0 and retning == Retning.HOYRE:
                return True
        # hvis vi ikke finner noen steiner som er en unna i retningen vi har fått oppgitt er det altså ingen steiner der, og vi returnerer false
        return False

    def hinder_finnes_i_retning(self, retning):
        if self.stein_finnes_i_retning(retning):
            return True

        # sjekker mot kantene
        if (self._sau.rute_venstre() == 17 and retning == Retning.HOYRE) or (self._sau.rute_topp() == 0 and retning == Retning.OPP) or (self._sau.rute_venstre() == 0 and retning == Retning.VENSTRE) or (self._sau.rute_topp() == 13 and retning == Retning.NED):
            return True
        return False


def finn_vanligste_element_i_liste(liste):
    #brukes når vi henter ut mest populære retningen i første del av funksjonen velg_retning
    teller = 0
    vanligste = liste[0]
    for element in liste:
        dennes_forekomst = liste.count(element)
        if(dennes_forekomst > teller):
            teller = dennes_forekomst
            vanligste = element
    return vanligste

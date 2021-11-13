from sauehjerne import finn_vanligste_element_i_liste
from gress import Gress
from sau import Sau
from spillbrett import Spillbrett
from retning import Retning

spillbrett = Spillbrett(1)
sau1 = Sau(400, 500, spillbrett)
gress = Gress(100, 100)
gress2 = Gress(150, 150)
sauehjerne = sau1.sauehjerne()


def test_avstand():
    assert sauehjerne.avstand_til_objekt(gress) == 14, "Avstanden er feil"
    assert sauehjerne.avstand_til_objekt(gress2) == 12


test_avstand()

spillbrettet = Spillbrett(1)
sauen = Sau(100, 100, spillbrettet)
gresset = Gress(150, 150)


def test_retning():
    retninger = sauen.sauehjerne().retninger_fra_objekt(gresset)
    assert set(retninger) == set([Retning.OPP, Retning.VENSTRE])


test_retning()


def test_finn_vanligste_element_i_liste():
    assert finn_vanligste_element_i_liste([Retning.NED, Retning.NED, Retning.OPP]) == Retning.NED
    assert finn_vanligste_element_i_liste(
        [Retning.NED, Retning.VENSTRE, Retning.OPP, Retning.VENSTRE]) == Retning.VENSTRE
    assert finn_vanligste_element_i_liste(
        [Retning.OPP, Retning.OPP, Retning.NED, Retning.NED, Retning.NED]) == Retning.NED
    assert finn_vanligste_element_i_liste([1, 2, 3, 1]) == 1


test_finn_vanligste_element_i_liste()


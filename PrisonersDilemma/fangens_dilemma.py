from typing import List


def beregn_score(valg_spiller1: str, valg_spiller2: str):
    score1, score2 = 0, 0
    if valg_spiller1 == "samarbeid":
        if valg_spiller2 == "samarbeid":
            score1 += 3
            score2 += 3
        else:
            score2 += 5
    elif valg_spiller1 == "svik":
        if valg_spiller2 == "samarbeid":
            score1 += 5
        else:
            score1 += 1
            score2 += 1

    return score1, score2


def spill_snilt(motstander_trekk: List[str]) -> str:
    svik = 0
    samarbeid = 0
    for trekk in motstander_trekk:
        if trekk == "svik":
            svik += 1
        elif trekk == "samarbeid":
            samarbeid += 1

    return "svik" if svik > samarbeid else "samarbeid"


def spill_slemt(motstander_trekk):
    return "samarbeid" if len(motstander_trekk) < 6 else "svik"


def utfor_spill():
    valgSpillerSnill, valgSpillerSlem = [], []
    scoreSpillerSnill, scoreSpillerSlem = 0, 0

    for i in range(10):
        trekkSnill = spill_snilt(valgSpillerSlem)
        trekkSlem = spill_slemt(valgSpillerSnill)

        valgSpillerSnill.append(trekkSnill)
        valgSpillerSlem.append(trekkSlem)

        score1, score2 = beregn_score(valgSpillerSnill[i], valgSpillerSlem[i])
        scoreSpillerSnill += score1
        scoreSpillerSlem += score2

    beste = "snill" if scoreSpillerSnill > scoreSpillerSlem else "slem"

    print(f"Score spiller snill: {scoreSpillerSnill}.")
    print(f"Score spiller slem: {scoreSpillerSlem}.")
    print(f"Den beste strategien var {beste}.")


def utfor_spill_uendelig():
    # Statisikk
    valgSpillerSnill, valgSpillerSlem = [], []
    scoreSpillerSnill, scoreSpillerSlem = 0, 0
    beste = ""

    fortsett = input("Skal det spilles et spill? ")
    while fortsett == "ja":

        trekkSnill = spill_snilt(valgSpillerSlem)
        trekkSlem = spill_slemt(valgSpillerSnill)

        valgSpillerSnill.append(trekkSnill)
        valgSpillerSlem.append(trekkSlem)

        score1, score2 = beregn_score(trekkSnill, trekkSlem)

        scoreSpillerSnill += score1
        scoreSpillerSlem += score2

        beste = "snill" if scoreSpillerSnill >= scoreSpillerSlem else "slem"

        print(f"Score spiller snill: {scoreSpillerSnill}.")
        print(f"Score spiller slem: {scoreSpillerSlem}.")
        print(f"Den beste strategien var {beste}.")
        fortsett = input("Skal det spilles et nytt spill? ")

    print("\nTakk for at du spilte, resultatet ble totalt:")
    print(f"  - Score spiller snill: {scoreSpillerSnill}.")
    print(f"  - Score spiller slem: {scoreSpillerSlem}.")
    print(f"  - Den beste strategien var {beste}.")


def min_strategi_alekshoi(motstanderHistorikk, minHistorikk):
    anbefaltValg = "svik"
    
    if len(motstanderHistorikk) < 2 or len(minHistorikk) < 2:
        return anbefaltValg

    if motstanderHistorikk[-1] == "svik" and motstanderHistorikk[-2] == "svik":
        anbefaltValg = "samarbeid"

    elif motstanderHistorikk[-1] == "samarbeid" and minHistorikk[-2] == "samarbeid":
        anbefaltValg = "samarbeid"

    elif motstanderHistorikk[-1] == "svik" and motstanderHistorikk[-2] == "samarbeid":
        anbefaltValg = "svik"

    return anbefaltValg



def spill_min_strategi(motstander_funksjon, num_games=20):
    historikk_strategi, historikk_motstander = [],[]
    score_strategi_total, score_motstander_total = 0, 0

    for _ in range(num_games):
        valg_strategi = min_strategi_alekshoi(historikk_motstander, historikk_strategi)
        valg_motstander = motstander_funksjon(historikk_strategi)
        score_strategi, score_motstander = beregn_score(valg_strategi, valg_motstander)

        historikk_strategi.append(valg_strategi)
        historikk_motstander.append(valg_motstander)

        score_strategi_total += score_strategi
        score_motstander_total += score_motstander

    print("Resultatet ble totalt:")
    print(f"  - Score strategi: {score_strategi_total}.")
    print(f"  - Score motstander: {score_motstander_total}.")

    print(f"Strategi gjorde trekkene: {', '.join(historikk_strategi)}")
    print(f"Motstander gjorde trekkene: {', '.join(historikk_motstander)}")




print("Spiller mot snill:")
spill_min_strategi(spill_snilt)


print("\nSpiller mot snill:")
spill_min_strategi(spill_slemt)
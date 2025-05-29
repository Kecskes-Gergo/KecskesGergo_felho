# A napi hőmérséklet diagrammját készíti el
def keszit_diagram_sort(nap_szama, homerseklet):
    csillagok_szama = int(homerseklet) # Csillagok száma egyenlő a hőmérséklettel
    csillagok = '*' * csillagok_szama # Ennyi csillagot írjon ki
    sor = f"Nap {nap_szama:2}: {csillagok} ({homerseklet}°C)" # Kiírja a napi hőmérsékletet csillagokkal egy sorba
    return sor

# Megrajzolja a heti hőmérsékletek diagrammját a keszit_diagram_sort függvénnyel
def rajzolj_diagram(homersekletek):
    print("Napi átlaghőmérséklet diagram (°C)")
    print("-" * 40)

    for i in range(len(homersekletek)): # végig megy a heti hőmérsékleteken
        nap = i + 1  # Napok számozása 1-től indul
        sor = keszit_diagram_sort(nap, homersekletek[i]) # elkészíti a sort
        print(sor) # kiírja a sort


napi_atlaghomersekletek = [12, 15, 14, 16, 13, 17, 18]

rajzolj_diagram(napi_atlaghomersekletek)



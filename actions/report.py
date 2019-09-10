def build_facility_report(arboretum):
    for river in arboretum.rivers:
        # arb_river = ['%.8s' %{river.id}]
        try:
            print(f'River [{"%.8s" % river.id}]')
        except:
            pass

    for mountain in arboretum.mountains:
        try:
            print(f'Mountain [{"%.8s" % mountain.id}]')
        except:
            pass

    for coastline in arboretum.coastlines:
        try:
            print(f'Coastline [{"%.8s" % coastline.id}]')
        except:
            pass

    for forest in arboretum.forests:
        try:
            print(f'Forest [{"%.8s" % forest.id}]')
        except:
            pass

    for grassland in arboretum.grasslands:
        try:
            print(f'Grassland [{"%.8s" % grassland.id}]')
        except:
            pass

    for swamp in arboretum.swamps:
        try:
            print(f'Swamp [{"%.8s" % swamp.id}]')
        except:
            pass

    input("\n\nPress any key to continue...")

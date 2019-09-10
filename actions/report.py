def build_facility_report(arboretum):
    for river in arboretum.rivers:
        try:
            print(f'River [{"%.8s" % river.id}]')
        except:
            pass

    for mountain in arboretum.mountains:
        try:
            print(f'Mountain [{"%.8s" % mountain.id}]')

            for plant in mountain.plants:
                print(f'  {plant.name} [{"%.8s" % plant.id}]')
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

            for plant in forest.plants:
                print(f'  {plant.name} [{"%.8s" % plant.id}]')
        except:
            pass

    for grassland in arboretum.grasslands:
        try:
            print(f'Grassland [{"%.8s" % grassland.id}]')

            for plant in grassland.plants:
                print(f'  {plant.name} [{"%.8s" % plant.id}]')
        except:
            pass

    for swamp in arboretum.swamps:
        try:
            print(f'Swamp [{"%.8s" % swamp.id}]')

            for plant in swamp.plants:
                print(f'  {plant.name} [{"%.8s" % plant.id}]')
        except:
            pass

    input("\n\nPress any key to continue...")

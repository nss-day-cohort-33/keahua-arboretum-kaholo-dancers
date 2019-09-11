def build_facility_report(arboretum):
    for river in arboretum.rivers:
        try:
            print(f'River [{"%.8s" % river.id}]')

            for plant in river.plants:
                print(f'{plant.name} [{"%.8s" % plant.id}]')

            for animal in river.animals:
                print(f'{animal.name} [{"%.8s" % animal.id}]')

        except:
            pass

    for mountain in arboretum.mountains:
        try:
            print(f'Mountain [{"%.8s" % mountain.id}]')

            for plant in mountain.plants:
                print(f'{plant.name} [{"%.8s" % plant.id}]')

            for animal in mountain.animals:
                print(f'{animal.name} [{"%.8s" % animal.id}]')
        except:
            pass

    for coastline in arboretum.coastlines:
        try:
            print(f'Coastline [{"%.8s" % coastline.id}]')

            for plant in coastline.plants:
                print(f'{plant.name} [{"%.8s" % plant.id}]')

            for animal in coastline.animals:
                print(f'{animal.name} [{"%.8s" % animal.id}]')

        except:
            pass

    for forest in arboretum.forests:
        try:
            print(f'Forest [{"%.8s" % forest.id}]')

            for plant in forest.plants:
                print(f'{plant.name} [{"%.8s" % plant.id}]')

            for animal in forest.animals:
                print(f'{animal.name} [{"%.8s" % animal.id}]')

        except:
            pass

    for grassland in arboretum.grasslands:
        try:
            print(f'Grassland [{"%.8s" % grassland.id}]')

            for plant in grassland.plants:
                print(f'{plant.name} [{"%.8s" % plant.id}]')

            for animal in grassland.animals:
                print(f'{animal.name} [{"%.8s" % animal.id}]')
        except:
            pass

    for swamp in arboretum.swamps:
        try:
            print(f'Swamp [{"%.8s" % swamp.id}]')

            for plant in swamp.plants:
                print(f'{plant.name} [{"%.8s" % plant.id}]')

            for animal in swamp.animals:
                print(f'{animal.name} [{"%.8s" % animal.id}]')
                
        except:
            pass

    input("\n\nPress any key to continue...")

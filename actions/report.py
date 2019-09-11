def build_facility_report(arboretum):
    for river in arboretum.rivers:
        try:
            print(f'River [{"%.8s" % river.id}]')
            if len(river.plants) != 0:
                print(f'  River Plants')
                for plant in river.plants:
                    print(f'    * {plant.name} [{"%.8s" % plant.id}]')
            if len(river.animals) != 0:
                print(f'  River Animals')
                for animal in river.animals:
                    print(f'    # {animal.name} ({"%.8s" % animal.id})')

        except:
            pass

    for mountain in arboretum.mountains:
        try:
            print(f'Mountain [{"%.8s" % mountain.id}]')
            if len(mountain.plants) != 0:
                print(f'  Mountain Plants:')
                for plant in mountain.plants:
                    print(f'    * {plant.name} [{"%.8s" % plant.id}]')
            if len(mountain.animals) != 0:
                print(f'  Mountain Animals:')
                for animal in mountain.animals:
                    print(f'    # {animal.name} ({"%.8s" % animal.id})')
        except:
            pass

    for coastline in arboretum.coastlines:
        try:
            print(f'Coastline [{"%.8s" % coastline.id}]')
            if len(coastline.plants) != 0:
                print(f'  Coastline Plants:')
                for plant in coastline.plants:
                    print(f'    * {plant.name} [{"%.8s" % plant.id}]')
            if len(coastline.animals) != 0:
                print(f'  Coastline Animals:')
                for animal in coastline.animals:
                    print(f'    # {animal.name} ({"%.8s" % animal.id})')

        except:
            pass

    for forest in arboretum.forests:
        try:
            print(f'Forest [{"%.8s" % forest.id}]')
            if len(forest.plants) != 0:
                print(f'  Forest Plants:')
                for plant in forest.plants:
                    print(f'    * {plant.name} [{"%.8s" % plant.id}]')
            if len(forest.animals) != 0:
                print(f'  Forest Animals:')
                for animal in forest.animals:
                    print(f'    # {animal.name} ({"%.8s" % animal.id})')

        except:
            pass

    for grassland in arboretum.grasslands:
        try:
            print(f'Grassland [{"%.8s" % grassland.id}]')
            if len(grassland.plants) != 0:
                print(f'  Grassland Plants:')
                for plant in grassland.plants:
                    print(f'    * {plant.name} [{"%.8s" % plant.id}]')
            if len(grassland.animals) != 0:
                print(f'  Grassland Animals:')
                for animal in grassland.animals:
                    print(f'    # {animal.name} ({"%.8s" % animal.id})')
        except:
            pass

    for swamp in arboretum.swamps:
        try:
            print(f'Swamp [{"%.8s" % swamp.id}]')
            if len(swamp.plants) != 0:
                print(f'  Swamp Plants:')
                for plant in swamp.plants:
                    print(f'    * {plant.name} [{"%.8s" % plant.id}]')
            if len(swamp.animals) != 0:
                print(f'  Swamp Animals:')
                for animal in swamp.animals:
                    print(f'    # {animal.name} ({"%.8s" % animal.id})')

        except:
            pass

    input("\n\nPress any key to continue...")

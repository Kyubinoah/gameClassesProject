from caracter import Caracter


def main():
    hero = Caracter(name="Roi Arture", health=100, damage=5)
    ennemy = Caracter(name="valeur", health=30, damage=2)

    while True:
        hero.attaque(ennemy)
        ennemy.attaque(hero)

        print(f"{hero.name} a attaquer {ennemy.name} et a fait {hero.damage}")
        print(f"{ennemy.name} a attaquer {hero.name} et a fait {ennemy.damage}")


if __name__ == '__main__':
    main()
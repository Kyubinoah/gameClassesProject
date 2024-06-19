from caracter import Hero, Ennemy


def main():
    hero = Hero(name="Roi Arture", health=100)
    ennemy = Ennemy(name="voleur", health=30)

    while True:
        hero.attaque(ennemy)
        ennemy.attaque(hero)

        print(f"vie de {hero.name} :{hero.health}")
        print(f"vie de {ennemy.name} :{ennemy.health}")

        input()


if __name__ == '__main__':
    main()
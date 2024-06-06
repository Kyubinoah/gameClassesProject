"""
Les fonction dans les classes sont appeler methode
et les classe on est variable local appeler attributs
"""


class Caracter:
    """
    Les varaibles déclaré en dehors du constructeur seront disponible pour toute ces instance
    Une instace est l'objet de la classe
    c'est variable sont appeler 'class-level-variables'
    """
    race = "humain"

    """
    Constructeur pour la classe 
    chaque attribut passer en paramètre sont unique au instance créé
    elle sont appeler 'Object-Level_variables'
    """
    def __init__(self, name: str, health: int, damage: int) -> None:
        """
        Construction du personnage
        :param name:
        :param health:
        :param damage:
        :return:
        """
        self.name = name
        self.health = health
        self.health_max = health
        self.damage = damage

    # création d'une méthode
    def attaque(self, target) -> None:
        """
        Création d'une methode appeler attaque
        Cette méthode permet de réduire le nombre de hp de la cible en fonction de l'atribut damage
        :param target: target est une instance de la class caracter
        :return:
        """

        # Diminution de l'atribut health de l'instance par rapport a l'atribut damage de la class
        target.hp -= self.damage
        target.hp = max(target.hp, 0)





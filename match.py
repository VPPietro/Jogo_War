from country import Country
from user import User


class Match:

    __lista_players: list = []
    __user_obj: dict = {}
    __country_obj: dict = {}

    def __init__(self, user_obj, country_obj):
        Match.__user_obj[user_obj.nome] = user_obj
        Match.__country_obj[user_obj.nome] = country_obj

    @staticmethod
    def get_lista_players() -> list:
        return Match.__lista_players

    @staticmethod
    def get_user(nome):
        return Match.__user_obj[nome]

    @staticmethod
    def get_country(nome):
        return Match.__country_obj[nome]

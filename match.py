from country import Country
from user import User


class Match:

    def __init__(self):
        self.__lista_players: list = []
        self.__user_obj: dict = {}
        self.__country_obj: dict = {}

    def grava_objs(self, user_obj: User, country_obj: Country):
        self.__user_obj[user_obj.nome] = user_obj
        self.__country_obj[user_obj.nome] = country_obj
        self.__lista_players.append(user_obj.nome)

    def get_lista_players(self) -> list:
        return self.__lista_players

    def get_user(self, nome: str) -> User:
        return self.__user_obj[nome]

    def get_country(self, nome: str) -> Country:
        return self.__country_obj[nome]

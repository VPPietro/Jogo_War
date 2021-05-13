"""
- Este programa poderia ter sido usado sem essa classe de usuário, porém foi criada em critério de aprendizagem.
- Seria mais lógico o uso dessa classe caso o user tivesse senha ou alguns outros atributos a mais além do nome.
"""


class User:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def user_obj(self):
        return self

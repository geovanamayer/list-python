class Pessoa(object):
    def _init_(self,nome,tipo,endereco):
        self.nome = nome
        self.tipo = tipo
        self.endereco = endereco
        
class Fisica(Pessoa):
    def _init_(self,nome,cpf,endereco):
        Pessoa._init_(self,nome,'fisica',endereco)
        self.__cpf = cpf
        
class Juridica(Pessoa):
    def _init_(self,nome,cnpj,endereco):
        Pessoa._init_(self,nome,'Juridica',endereco)
        self.__cnpj = cnpj
     
if _name_ == "_main_":
    pessoa1 = Fisica("João", "123.456.789-00", "Rua A")
    pessoa2 = Juridica("Empresa XYZ", "12.345.678/0001-90", "Rua B")
    pessoa3 = Juridica("Mundo Gamer", "11080921000128", "Pitanga PR")
    
    print(pessoa1.nome, pessoa1.tipo, pessoa1.endereco, pessoa1.Fisica_cpf)
    print(pessoa2.nome, pessoa2.tipo, pessoa2.endereco, pessoa2.Juridica_cnpj)
    print(pessoa3.nome, pessoa3.tipo, pessoa3.endereco, pessoa3.Juridica_cnpj)
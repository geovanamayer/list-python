class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def resumo(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

class Pai(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

    def resumo(self):
        super().resumo()
        print("Função: Pai")
        print("Filhos:")
        for filho in self.filhos:
            print(f"  - {filho.nome}")

class Mae(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

    def resumo(self):
        super().resumo()
        print("Função: Mãe")
        print("Filhos:")
        for filho in self.filhos:
            print(f"  - {filho.nome}")

class Filho(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.pai = None
        self.mae = None

    def adicionar_pais(self, pai, mae):
        self.pai = pai
        self.mae = mae

    def resumo(self):
        super().resumo()
        print("Função: Filho")
        if self.pai and self.mae:
            print(f"Pai: {self.pai.nome}")
            print(f"Mãe: {self.mae.nome}")

# Exemplo de uso
pai = Pai("Pai", 40)
mae = Mae("Mãe", 35)
filho1 = Filho("Filho 1", 10)
filho2 = Filho("Filho 2", 8)

pai.adicionar_filho(filho1)
mae.adicionar_filho(filho1)
pai.adicionar_filho(filho2)
mae.adicionar_filho(filho2)

filho1.adicionar_pais(pai, mae)
filho2.adicionar_pais(pai, mae)

# Resumo das pessoas
print("Resumo do Pai:")
pai.resumo()
print("\nResumo da Mãe:")
mae.resumo()
print("\nResumo do Filho 1:")
filho1.resumo()
print("\nResumo do Filho 2:")
filho2.resumo()

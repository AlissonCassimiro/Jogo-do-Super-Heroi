# class super heroi, nome do super poder, o super poder, força do poder do sph 1 - 100
# func que  retorna o nome do sp, func q retorna a força do sp
# main fazer um i.f se o spp > 80 ele pode usar els.e nao


class Heroi:
    def __init__(self, nome, npoder, forca):
        self.nome_class = nome
        self.Spoder = npoder
        self.forca = forca

    def nomeDH(self):
        return self.nome_class

    def Npoder(self):
        return f'e o seu Super-poder é: {self.Spoder}'

    def Fpoder(self):
        return self.forca


if __name__ == '__main__':
    # alisson = varialvel
    nome = input('Digite o nome do heroi: ')
    npoder = input('Digite o nome do poder: ')
    forca = int(input('Digite a força do heroi: '))

    alisson = Heroi(nome, npoder, forca)

    descHab = print(f"\nO Seu nome de Heroi(na) é: {alisson.nomeDH()}")
    print(f"\n{alisson.Npoder()}")
    print(f"Nivel de poder da habilidade: {alisson.Fpoder()}")

    if alisson.Fpoder() > 80:
        print(f"\nO Super-heroi ", alisson.nomeDH(), ', pode usar este poder')

    elif alisson.Fpoder() == 80:
        print(f"O(a) Super-heroi(na) ", alisson.nomeDH(), ', ultrapassou o esta com', alisson.Fpoder(), ' exigido para usar este poder')

    else:
        # niveis a serem subidos para usar o poder
        niveisRestantes = 80 - alisson.Fpoder()
        niveisRestantes = str(niveisRestantes)
        print(f"O Super-heroi ", alisson.nomeDH(), ', nao pode usar este poder pois o nivel exigido é 80 e agora ele esta com', alisson.Fpoder())
        print(f"No entanto ele precisa de mais:", niveisRestantes, "niveis, Para conseguir usar este poder!, e derrotar qualquer um!")

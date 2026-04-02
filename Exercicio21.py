import os

#declarar variaveis
nome: str = ''
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
valor_media: float = 0.0
dir: str = ''
arq: str = ''

def escreveArq(caminho, arquivo, linha_arq):
    file: str = ''
    tipo: str = ''
    enc: str = ''

    file = caminho + arquivo
    if (os.path.exists(caminho) and os.path.isdir(caminho)):
        tipo = "w"
        enc = 'utf-8'
        if (os.path.exists(file)):
            tipo = 'a'
        with open(file, tipo, encoding=enc) as file:
            file.write(linha_arq)
    else:
        print('Diretório inválido.')    

def cadastro(nm, nt1, nt2, nt3, nt4, vlr_media):
    global arq
    global dir
    linha: str = ''

    dir = '/tmp/exercicios/'
    arq = 'ex21.txt'

    linha = (nm + ';' + str(nt1) + ';' + str(nt2) + ';' + str(nt3) + ';' + str(nt4) + ';' + str(vlr_media) + '\n')

    escreveArq(dir, arq, linha)


def med(n1, n2, n3, n4):
    media: float = 0.0
    media = (n1 + n2 + n3 +n4) / 4
    return media

def entrada(cnt):
    global nome
    global nota1
    global nota2
    global nota3
    global nota4
    global valor_media

    if cnt == 1:
        nome = str(input("Digite o nome do aluno: "))
        return nome
    elif cnt == 2:
        nota1 = float(input("Digite a primeira nota: "))
        return nota1

    elif cnt == 3:
        nota2 = float(input("Digite a segunda nota: "))
        return nota2
    
    elif cnt == 4:
        nota3 = float(input("Digite a terceira nota nota: "))
        return nota3

    elif cnt == 5:
        nota4 = float(input("Digite a quarta nota: "))
        return nota4
    
    elif cnt == 6:
        valor_media = med(nota1, nota2, nota3, nota4)
        return valor_media


def main():
    global nome
    global nota1
    global nota2
    global nota3
    global nota4
    global valor_media

    contador: int = 1

    while contador <= 6:
        entrada(contador)
        contador = contador + 1
    print("O valor da média do aluno é de " , valor_media)
    
    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)



if __name__ == '__main__':
    main()


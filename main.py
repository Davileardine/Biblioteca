from Pessoa import Pessoa
from Livro import Livro
from Biblioteca import Biblioteca

if __name__ == "__main__":
  Biblioteca = Biblioteca()

  #Criando pessoas
  Davi = Pessoa('Davi', 'Vila Velha')
  Glaytin = Pessoa('Glaytin', 'Vila Velha')
  Nino = Pessoa('Nino', 'Iconha')

  #Criando livros
  Arte_da_Guerra = Livro('Arte da Guerra', 'Sun Tzu', 170)
  Principe = Livro('O Príncipe', 'Nicolau Maquiavel', 452)
  Pequeno_principe = Livro('Pequeno Príncipe', 'Antoine de Saint-Exupéry', 214)

  #Adicionando pessoas
  Biblioteca.adiciona_pessoa(Davi)
  Biblioteca.adiciona_pessoa(Glaytin)
  Biblioteca.adiciona_pessoa(Nino)
  listPessoas = Biblioteca.get_pessoas()
 
  #Adicionando livros
  Biblioteca.adiciona_livro(Arte_da_Guerra)
  Biblioteca.adiciona_livro(Principe)
  Biblioteca.adiciona_livro(Pequeno_principe)
  livros = Biblioteca.get_livros()
  while True:
    print('Bem vindo à biblioteca, qual opção deseja?')
    print('1 - Mostrar a lista de livros disponíveis')
    print('2 - Alugar um livro')
    print('3 - Devolver um livro')
    print('4 - Errei a loja, mal ai!')
    i = input()

    match i:
      case '1':
        print("-----------------------------------------------")
        print ("\nSegue a lista dos livros: ")
        print("\n".join(map(str,livros)), "\n")
        print("-----------------------------------------------")

      case '2':
        print("Já é cadastrado?")
        i = input("Y / N\n").lower()
        if i == "y":
          print("Showwww, qual o seu nome?\n")

          nm = Biblioteca.get_pessoa(input())
          if not nm:
            print("Vish, não está aqui! Vamos te cadastrar, por favor Insira seu nome e endereço, respectivamente:\n")
            nome = input('\n')
            end = input()
            new_pessoa = Pessoa(nome,end)
            Biblioteca.adiciona_pessoa(new_pessoa)
            print("Parabéns, agora você faz parte!\n")
            print(Biblioteca.get_pessoas())

          else:
            print("Beleza, achamos você.")
            print("Qual livro deseja?\n")
            print("\n".join(map(str,livros)), "\n")
            lv_i = input()
            lv= Biblioteca.get_livro(lv_i)
            if Biblioteca.emprestar_livro(lv,nm):
              print(f"O livro '{lv_i}' foi alugado com sucesso!")
            else:
              print(f"O livro '{lv_i}' não está disponível!")
     # case '3':

      case '4':
        print("Até mais!!")
        break
'''
  print(Biblioteca.get_livros())

  Biblioteca.emprestar_livro(Arte_da_Guerra, Davi)
  Biblioteca.emprestar_livro(Principe, Nino)

  print(Biblioteca.get_livros())

  print(Biblioteca.get_emprestimos())

  print('\n')
  
  Biblioteca.devolver_livro(Pequeno_principe)

  print('\n')

  print(Biblioteca.get_livros())
  print(Biblioteca.get_emprestimos())

  print('\n')

  Biblioteca.devolver_livro(Arte_da_Guerra)

  print('\n')

  print(Biblioteca.get_livros())
  print(Biblioteca.get_emprestimos())
'''
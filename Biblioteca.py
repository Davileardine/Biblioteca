from Emprestimo import Emprestimo
import datetime


class Biblioteca:

  def __init__(self):
    self.vtlivros = []
    self.vtpessoas = []
    self.vtemprestimos = []

  def adiciona_livro(self, livro):
    self.vtlivros.append(livro)

  def adiciona_pessoa(self, pessoa):
    self.vtpessoas.append(pessoa)

  #def adiciona_emprestimo(self, emprestimo):
  # self.vtemprestimos.append(emprestimo)

  def get_pessoas(self):
    vtnomes = []

    for i in range(len(self.vtpessoas)):
      vtnomes.append(self.vtpessoas[i].get_name())

    return vtnomes

  def get_pessoa(self, name):
    for i in range(len(self.vtpessoas)):
      if self.vtpessoas[i].get_name() == name:
        return self.vtpessoas[i]

      return False
      

  def get_livros(self):
    vtnomes = []

    for i in range(len(self.vtlivros)):
      vtnomes.append(self.vtlivros[i].get_name())

    return vtnomes

  def get_livro(self, name):
    for i in range(len(self.vtlivros)):
      if self.vtlivros[i].get_name() == name:
        return self.vtlivros[i]

      return False

  def get_emprestimos(self):
    vtemp = []

    for i in range(len(self.vtemprestimos)):
      vtemp.append(self.vtemprestimos[i].get_emprestimo())

    return vtemp

  def emprestar_livro(self,
                      livro,
                      pessoa,
                      data_emprestimo=datetime.date.today()):

    for i in range(len(self.vtlivros)):

      if livro == self.vtlivros[i]:

        for i in range(len(self.vtemprestimos)):
          if livro == self.vtemprestimos[i].get_livro():
            return False

        self.vtlivros.remove(self.vtlivros[i])

        #Criando emprestimo
        self.vtemprestimos.append(Emprestimo(pessoa, livro, str(data_emprestimo)))

        return True

    return False

    #print(f"O livro '{livro}' não está disponível!")

def devolver_livro(self, livro, data_devolucao=datetime.date.today()):

    if livro in self.vtlivros or livro in self.vtemprestimos:

      if livro in self.vtemprestimos:
        self.vtemprestimos.pop(self.vtemprestimos.index(livro))
        livro.set_disponivel(True)
        print(
          f"O livro '{livro.get_name()}' foi retornado com sucesso!\nData da devolução {data_devolucao}"
        )
        return

    print("Livro não encontrado!")
    return False
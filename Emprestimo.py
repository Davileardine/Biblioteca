class Emprestimo:

  def __init__(self, pessoa, livro, data):
    self.pessoa = pessoa
    self.livro = livro
    self.data = data

  def get_livro(self):
    return self.livro

  def get_pessoa(self):
    return self.pessoa

  def get_data(self):
    return self.data

  def get_emprestimo(self):
    return [self.pessoa, self.livro, self.data]
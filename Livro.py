class Livro:

  def __init__(self, nome, autor, pag):
    self.nome = nome
    self.autor = autor
    self.pag = pag

  def get_name(self):
    return self.nome
  
  def is_disponivel(self):
    return self.is_disponivel

  def set_disponivel(self, is_disponivel):
    self.is_disponivel = is_disponivel
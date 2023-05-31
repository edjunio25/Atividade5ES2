class Tarefa:
  def __init__(self, nome, data, horario, local):
    self.nome = nome
    self.dia = data[:2]  
    self.mes = data[2:4]  
    self.ano = data[4:]
    self.hora = horario[:2]
    self.minuto = horario[2:]#hhmm
    self.local = local #string

  def changeNome(self, newNome):
    self.nome = newNome

  def changeData(self, newData):
    if len(newData) >= 8:
        self.dia = newData[:2]  
        self.mes = newData[2:4]  
        self.ano = newData[4:]
    else:
        print("Erro: Nova data inválida")

  def changeHorario(self, newHorario):
    self.hora = newHorario[:2]
    self.minuto = newHorario[2:]

  def changeLocal(self, newLocal):
    self.local = newLocal
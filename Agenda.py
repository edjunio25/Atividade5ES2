from Tarefas import Tarefa
class Agenda:
  def __init__(self):
    self.listaTarefas = []
  
  def addToListaTarefas(self, tarefa):
    self.listaTarefas.append(tarefa)
    self.listaTarefas.sort(key=lambda x: (x.ano, x.mes, x.dia, x.hora, x.minuto))
    
  def removeFromListaTarefas(self, tarefaASerRemovida):
    if len(self.listaTarefas) == 0:
        print("A lista de tarefas está vazia. Nenhuma tarefa para remover.")
        return
    else:
        for i in self.listaTarefas:
            if (i.dia == tarefaASerRemovida.dia and
                i.mes == tarefaASerRemovida.mes and
                i.ano == tarefaASerRemovida.ano and
                i.hora == tarefaASerRemovida.hora and
                i.minuto == tarefaASerRemovida.minuto):
                self.listaTarefas.remove(i)
                return
        print("Tarefa não encontrada na lista.")

  def getListaTarefasDoMeseAnoDado(self, mes, ano):
    tarefasDoMes = []
    if len(self.listaTarefas) == 0:
      print("A lista de tarefas está vazia.")
      return
    for i in self.listaTarefas:
      if (i.mes == mes and i.ano == ano):
        tarefasDoMes.append(i)
    if len(tarefasDoMes) == 0:
      print("Nenhuma tarefa para o mês especificado.")
      return
    else:
      return tarefasDoMes
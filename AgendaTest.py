import unittest
from Tarefas import Tarefa
from Agenda import Agenda


class TestAgenda(unittest.TestCase):

  def setUp(self):
    self.agenda = Agenda()

  def testAddToListaTarefas(self):
    tarefa1 = Tarefa("Tarefa 1", "31052023", "0830", "Local 1")
    tarefa2 = Tarefa("Tarefa 2", "01062023", "1000", "Local 2")
    tarefa3 = Tarefa("Tarefa 3", "01062023", "0900", "Local 3")

    self.agenda.addToListaTarefas(tarefa2)
    self.agenda.addToListaTarefas(tarefa1)
    self.agenda.addToListaTarefas(tarefa3)

    self.assertEqual(len(self.agenda.listaTarefas), 3)
    self.assertEqual(self.agenda.listaTarefas[0], tarefa1)
    self.assertEqual(self.agenda.listaTarefas[1], tarefa3)
    self.assertEqual(self.agenda.listaTarefas[2], tarefa2)

  def testRemoveFromListaTarefas(self):
    tarefa1 = Tarefa("Tarefa 1", "31052023", "0830", "Local 1")
    tarefa2 = Tarefa("Tarefa 2", "01062023", "1000", "Local 2")

    self.agenda.addToListaTarefas(tarefa1)
    self.agenda.addToListaTarefas(tarefa2)

    self.agenda.removeFromListaTarefas(tarefa1)

    self.assertEqual(len(self.agenda.listaTarefas), 1)
    self.assertEqual(self.agenda.listaTarefas[0], tarefa2)

    self.agenda.removeFromListaTarefas(tarefa1)

    self.assertEqual(len(self.agenda.listaTarefas), 1)

  def testGetListaTarefasDoMeseAnoDado(self):
    tarefa1 = Tarefa("Tarefa 1", "31052023", "0830", "Local 1")
    tarefa2 = Tarefa("Tarefa 2", "01062023", "1000", "Local 2")
    tarefa3 = Tarefa("Tarefa 3", "01062023", "0900", "Local 3")

    self.agenda.addToListaTarefas(tarefa1)
    self.agenda.addToListaTarefas(tarefa2)
    self.agenda.addToListaTarefas(tarefa3)

    tarefas_junho_2023 = self.agenda.getListaTarefasDoMeseAnoDado("06", "2023")
    tarefas_maio_2023 = self.agenda.getListaTarefasDoMeseAnoDado("05", "2023")

    self.assertEqual(len(tarefas_junho_2023), 2)
    self.assertEqual(tarefas_junho_2023[0].dia, "01")
    self.assertEqual(tarefas_junho_2023[0].mes, "06")
    self.assertEqual(tarefas_junho_2023[0].ano, "2023")
    self.assertEqual(tarefas_junho_2023[0].hora, "09")
    self.assertEqual(tarefas_junho_2023[0].minuto, "00")

    self.assertEqual(len(tarefas_maio_2023), 1)
    self.assertEqual(tarefas_maio_2023[0].dia, "31")
    self.assertEqual(tarefas_maio_2023[0].mes, "05")
    self.assertEqual(tarefas_maio_2023[0].ano, "2023")
    self.assertEqual(tarefas_maio_2023[0].hora, "08")
    self.assertEqual(tarefas_maio_2023[0].minuto, "30")



if __name__ == '__main__':
  unittest.main()

tarefas = []

def adicionar_tarefa(tarefas, nome):
  tarefa = {
    "nome": nome,
    "completada": False
  }
  tarefas.append(tarefa)

  print(f"A tarefa {nome} foi adicionada com sucesso!")
  return

def ver_tarefas(tarefas):
  print("\nLista de tarefas:")
  for indice, tarefa in enumerate(tarefas, start=1):
    status = "✓" if tarefa["completada"] else " "
    nome_tarefa = tarefa['nome']

    print(f"{indice}. [{status}] {nome_tarefa}")
  return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome):
  indice_tarefa_ajustado = int(indice_tarefa) - 1
  if(indice_tarefa_ajustado >= 0  and indice_tarefa_ajustado < len(tarefas)):
    tarefas[indice_tarefa_ajustado]['nome'] = novo_nome
    print(f"Tarefa {indice_tarefa} atualizada para {novo_nome}")
    return
  else:
    print("Digite um número de tarefa válida!")
    return
  
def completar_tarefa(tarefas, indice_tarefa):
  indice_tarefa_ajustado = int(indice_tarefa) - 1

  if(indice_tarefa_ajustado >= 0  and indice_tarefa_ajustado < len(tarefas)):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    tarefas[indice_tarefa_ajustado]['completada'] = True
    print(f"Tarefa {indice_tarefa} foi completada com sucesso!")
    return
  else:
    print("Digite um número de tarefa válida!")
    return

def remover_tarefas_completadas(tarefas):
  for tarefa in tarefas:
    if(tarefa["completada"]):
      tarefas.remove(tarefa)
  
  print("Tarefas completadas foram deletadas com sucesso!")
  return  

while True:
  print("\nMenu do gerenciador de Lista de Tarefas:")
  print("1. Adicionar uma tarefa")
  print("2. Ver tarefas")
  print("3. Atualizar tarefa")
  print("4. Completar tarefa")
  print("5. Remover tarefas completadas")
  print("6. Sair")

  escolha = input("Digite a sua escolha: ")

  if(escolha == "1"):
    nome_tarefa = input("Dgite o nome da tarefa que deseja adicionar: ")
    adicionar_tarefa(tarefas, nome_tarefa)
  elif(escolha == "2"):
    ver_tarefas(tarefas)
  elif(escolha == "3"):
    ver_tarefas(tarefas)
    indice_tarefa = int(input("Digite o número da tarefa que deseja atualizar: "))
    novo_nome = input("Digite o novo nome da tarefa: ")
    atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
  elif(escolha == "4"):
    ver_tarefas(tarefas)
    indice_tarefa = int(input("Digite o número da tarefa que deseja completar: "))
    completar_tarefa(tarefas, indice_tarefa)
  elif(escolha == "5"):
    remover_tarefas_completadas(tarefas)
    ver_tarefas(tarefas)
  elif(escolha == "6"):
    break
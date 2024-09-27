def adicionar_contato(agenda, nome_contato, telefone_contato, email_contato):
    contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "fav": False}
    agenda.append(contato)
    print(f"{nome_contato} foi adicionado/a na sua agenda com sucesso!")
    return

def ver_agenda(agenda):
    print("Lista de contatos:")
    for indice, contato in enumerate(agenda, start=1):
        fav = "★" if contato["fav"] else ""
        nome_contato = contato["nome"]
        email_contato = contato["email"]
        telefone_contato = contato["telefone"]
        print(f"{indice}. {fav} {nome_contato} | email: {email_contato} | telefone: {telefone_contato} ")
    return

def editar_contato(agenda, indice_contato, type_edit):
    if indice_contato - 1 >= 0 and indice_contato - 1 < len(agenda):
        if type_edit == 1:
            new_name_contato = input("Digite o novo nome do contato: ")
            agenda[indice_contato - 1]["nome"] = new_name_contato
            print(f"{indice_contato} nome atualizado para {new_name_contato}")
        if type_edit == 2:
            new_number_contato = int(input("Digite o novo numero do contato: "))
            agenda[indice_contato - 1]["telefone"] = new_number_contato
            print(f"{indice_contato} telefone atualizado para {new_number_contato}")
        if type_edit == 3:
            new_email_contato = input("Digite o novo e-mail do contato: ")
            agenda[indice_contato - 1]["email"] = new_email_contato
            print(f"{indice_contato} email atualizado para {new_name_contato}")
        
    else:
        print("indice indisponivel")
    return

def favoritar_contato(agenda, indice_contato):
    if indice_contato - 1 >= 0 and indice_contato - 1 < len(agenda):
        agenda[indice_contato - 1]["fav"] = True
        print(f"{indice_contato} marcada como favorito")
    else:
        print("indice indisponivel")
    return

def ver_agenda_fav(agenda):
    print("Lista de contatos:")
    for indice, contato in enumerate(agenda, start=1):
        fav = "★" if contato["fav"] else ""
        nome_contato = contato["nome"]
        email_contato = contato["email"]
        telefone_contato = contato["telefone"]
        if contato["fav"]:
            print(f"{indice}. {fav} {nome_contato} | email: {email_contato} | telefone: {telefone_contato} ")
    return

def deletar_contato(agenda, nome_contato):
    for contato in agenda:
        if contato["nome"] == nome_contato:
            agenda.remove(contato)
    
    print(f"contato {nome_contato} foi removido!")
    return

agenda = []

while True:
    print("\nAgenda:")
    print("1. adicionar um contato")
    print("2. visualizar a lista de contatos cadastrados")
    print("3. editar um contato")
    print("4. marcar/desmarcar um contato como favorito")
    print("5. ver uma lista de contatos favoritos")
    print("6. apagar um contato ")
    print("7. Fechar agenda ")

    escolha = input("Digite a sua escolha:")
    if escolha == "1":
        nomeC = input("Digite o nome da pessoa que deseja adicionar: ")
        celularC = int(input("Digite o numero da pessoa que deseja adicionar: "))
        emailC = input("Digite o email da pessoa que deseja adicionar: ")
        adicionar_contato(agenda, nomeC, celularC, emailC)
        
    elif escolha == "2":
        ver_agenda(agenda)
        
    elif escolha == "3":
        ver_agenda(agenda)
        indice_contato = int(input("Digite o numero da posição do contato que queira editar: "))
        type_edit = int(input("O que você deseja editar?(Digite o numero) \n1-Nome \n2-Numero \n3-E-mail: "))
        editar_contato(agenda, indice_contato, type_edit)
        
    elif escolha == "4":
        ver_agenda(agenda)
        indice_contato = int(input("Digite o numero da posição do contato que queira favoritar: "))
        favoritar_contato(agenda, indice_contato)
        
    elif escolha == "5":
        ver_agenda_fav(agenda)
        
    elif escolha == "6":
        ver_agenda(agenda)
        name_contato = input("Digite o  nome do contato que deseja excluir: ")
        deletar_contato(agenda, name_contato)
        ver_agenda(agenda)
    else:
        break

print("Programa finalizado")
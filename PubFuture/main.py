#Programa feito com base nos meus conhecimentos atuais sobre programacao
x = 0
receita_log = "0"
despesa_log = "0"
conta_log = "0"
while x != "e":
    x = str(input("O que deseja editar(Receitas: r | Despesas: d | Contas: c | encerrar o programa: e)? "))
    if x == "r":
        if receita_log == "0":
             receita_valor = float(input("Digite o valor da receita: "))
             receita_data_recebimento = int(input("Digite a data de recebimento: "))
             receita_data_recebimento_esperado = int(input("Digite a data de recebimento esperado: "))
             receita_descricao = str(input("Digite a descricao: "))
             receita_conta = int(input("Digite a conta: "))
             receita_tipo = str(input("Digite o tipo de receita: "))
             print("valor da receita:",receita_valor,"\n data de recebimento:", receita_data_recebimento, "\n data de recebimento esperado:", receita_data_recebimento_esperado, "\n descricao:", receita_descricao, "\n conta:", receita_conta, "\n receita:", receita_tipo)
             receita_final = (" valor da receita:",receita_valor," data de recebimento:", receita_data_recebimento, " data de recebimento esperado:", receita_data_recebimento_esperado, " descricao:", receita_descricao, " conta:", receita_conta, " receita:", receita_tipo)
             receita_log = "1"
             print("CADASTRADO COM SUCESSO")
        elif receita_log == "1":
            receita_mudar = int(input("O que deseja mudar na receita:1-VALOR  2-CONTA  3-TIPO  4-MOSTRAR EXISTENTE  5-CRIAR RECEITA NOVA "))
            if receita_mudar == 1:
                temp = float(input("Digite o novo valor da receita: "))
                receita_valor = temp
                print("Alterado com sucesso")
            elif receita_mudar == 2:
                temp = int(input("Digite a nova conta: "))
                receita_conta = temp
                print("Alterado com sucesso")
            elif receita_mudar == 3:    
               temp = str(input("Digite o novo tipo de receita: "))
               receita_tipo = temp
               print("Alterado com sucesso")
            elif receita_mudar == 4:
                print(" valor da receita:",receita_valor,"\n data de recebimento:", receita_data_recebimento, "\n data de recebimento esperado:", receita_data_recebimento_esperado, "\n descricao:", receita_descricao, "\n conta:", receita_conta, "\n receita:", receita_tipo)
            elif receita_mudar == 5:
                receita_log = "0"
    elif x=="d":
        if despesa_log == "0":
             despesa_valor = float(input("Digite o valor da despesa: "))
             despesa_data_pagamento = int(input("Digite a data de pagamento: "))
             despesa_data_pagamento_esperado = int(input("Digite a data de pagamento esperado: "))
             despesa_tipo = str(input("Digite o tipo de receita: "))
             despesa_conta = int(input("Digite a conta: "))
             print("valor da despesa:",despesa_valor,"\n data de pagamento:", despesa_data_pagamento, "\n data de pagamento esperado:", despesa_data_pagamento_esperado,"\n tipo:", despesa_tipo, "\n conta:", despesa_conta)
             despesa_final = ("valor da despesa:",despesa_valor,"\n data de pagamento:", despesa_data_pagamento, "\n data de pagamento esperado:", despesa_data_pagamento_esperado,"\n tipo:", despesa_tipo, "\n conta:", despesa_conta)
             despesa_log = "1"
             print("CADASTRADO COM SUCESSO")
        elif despesa_log == "1":
            despesa_mudar = int(input("O que deseja mudar na receita:1-VALOR:  2-DATA PAGEMENTO  3-PAGAMENTO ESPERADO  4-TIPO  5-CONTA  6-MOSTRAR DESPESA EXISTENTE  7-CRIAR NOVA DESPESA: "))
            if despesa_mudar == 1:
                temp = float(input("Digite o novo valor da despesa: "))
                despesa_valor = temp
                print("Alterado com sucesso")
            elif despesa_mudar == 2:
                temp = int(input("Digite a data de pagamento: "))
                despesa_data_pagamento = temp
                print("Alterado com sucesso")
            elif despesa_mudar == 3:    
               temp = int(input("Digite a nova da de pagamento esperada: "))
               despesa_data_pagamento_esperado = temp
               print("Alterado com sucesso")
            elif despesa_mudar == 4:
                temp = str(input("Digite o novo tipo de despesa: "))
                despesa_tipo = temp
                print("Alterado com sucesso")
            elif despesa_mudar == 5:
               temp = int(input("Digite a nova conta: "))
               despesa_conta = temp
               print("Alterado com sucesso")
            elif despesa_mudar == 6:
                print("valor da despesa:",despesa_valor,"\n data de pagamento:", despesa_data_pagamento, "\n data de pagamento esperado:", despesa_data_pagamento_esperado,"\n tipo:", despesa_tipo, "\n conta:", despesa_conta)
            elif despesa_mudar == 7:
                despesa_log = "0"
    elif x=="c":
        if conta_log == "0":
            conta_saldo = float(input("Digite o saldo da conta: "))
            conta_tipo = str(input("Digite o tipo de conta: "))
            conta_instituicao = str(input("Digite a instituicao financeira: "))
            conta_final = ("Saldo da conta:", conta_saldo, "Tipo de conta:", conta_tipo, "Instituicao:", conta_instituicao)
            print(conta_final, "\nConta cadastrada com sucesso")
            conta_log = "1"
        elif conta_log == "1":
            conta_mudar = int(input("O que deseja mudar na conta: 1-SALDO  2-TIPO  3-INSTITUICAO  4-MOSTRAR CONTA ATUAL  5-CRIAR OUTRA CONTA: "))
            if conta_mudar == 1:
                temp = float(input("Digite o novo saldo da conta: "))
                conta_saldo = temp
                print("Alterado com sucesso")
            elif conta_mudar == 2:
                temp = int(input("Digite o novo tipo de conta: "))
                conta_tipo = temp
                print("Alterado com sucesso")
            elif conta_mudar == 3:    
               temp = str(input("Digite a nova instituicao: "))
               conta_instituicao = temp
               print("Alterado com sucesso")
            elif conta_mudar == 4:
                print("Saldo da conta:", conta_saldo, "Tipo de conta:", conta_tipo, "Instituicao:", conta_instituicao)
            elif conta_mudar == 5:
                conta_log = "0"
    else:
        print("Erro ao digitar")
print("Programa encerrado")
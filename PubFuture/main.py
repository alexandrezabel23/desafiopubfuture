#Programa feito com base nos meus conhecimentos atuais sobre programacao
x = 0
receita_log = "0"
while x != "e":
    x = str(input("O que deseja editar (Receitas: r, Despesas: d, Contas: c, encerrar o programa: e)? "))
    if x == "r":
        if receita_log == "0":
             receita_valor = float(input("Digite o valor da receita: "))
             receita_data_recebimento = int(input("Digite a data de recebimento: "))
             receita_data_recebimento_esperado = int(input("Digite a data de recebimento esperado: "))
             receita_descricao = str(input("Digite a descricao: "))
             receita_conta = int(input("Digite a conta: "))
             receita_tipo = str(input("Digite o tipo de receita: "))
             print("valor da receita:",receita_valor,"\n data de recebimento:", receita_data_recebimento, "\n data de recebimento esperado:", receita_data_recebimento_esperado, "\n descricao:", receita_descricao, "\n conta:", receita_conta, "\n receita:", receita_tipo)
             receita_final = ("valor da receita:",receita_valor,"\n data de recebimento:", receita_data_recebimento, "\n data de recebimento esperado:", receita_data_recebimento_esperado, "\n descricao:", receita_descricao, "\n conta:", receita_conta, "\n receita:", receita_tipo)
             receita_log = "1"
             print("CADASTRADO COM SUCESSO")
        elif receita_log == "1":
            receita_mudar = int(input("O que deseja mudar na receita: valor-1  conta-2 tipo-3 mostrar receita existente-4: "))
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
                print(receita_final)
                print("Alterado com sucesso")
    elif x=="d":
        print("o") 
    elif x=="c":
        conta_saldo = float(input("Digite o saldo da conta: "))
        conta_tipo = str(input("Digite o tipo de conta: "))
        conta_instituicao = str(input("Digite a instituicao financeira: "))
    else:
        print("Erro ao digitar")
print("Programa encerrado")
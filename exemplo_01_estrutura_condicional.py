def exemplo_if_simples():
    idade = int(input("Digite a sua idade: "))

    if idade <= 17:
        print("Menor de idade")
    elif idade <= 64:
        print("Adulto")
    else:
        print("Idoso")

    # Operadores relacionais
    # < Menor
    # <= Menor ou igual
    # > Maior
    # >= mior ou igual
    # == Igual
    # != Diferente



def exemplo_if_operador_e():

    # aplicar cupon desconto 
    #qtd 5 até 10 cupons 5%
    #qtd 50 cupum de 10%
    #qdt acima de 15%
    valor_produto = 100.00
    quantidade = int(input("Digite a quantidade de produtos: "))

    percentual_desconto = 0
    if quantidade >=5 and quantidade <= 10:
        percentual_desconto =5
    elif quantidade >= 11 and quantidade <= 50:
        percentual_desconto = 10
    elif quantidade >50:
        percentual_desconto =15

    valor_compra_sem_desconto = quantidade * valor_produto
    valor_desconto = valor_compra_sem_desconto * (percentual_desconto / 100)
    valor_total_compra = valor_compra_sem_desconto - valor_desconto
    
    print("Valor compra: ", valor_compra_sem_desconto)
    print("Percentual de desconto: ", percentual_desconto, "%")
    print("valor_desconto: ", valor_desconto)
    print("Valor total", valor_total_compra)


if __name__ == "__main__":
    # exemplo_if_operador_e()
    exemplo_if_simples()
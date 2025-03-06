def exemplo_tipos_primitivos():
    nome: str = "PS5 Pro"
    preco: float = 7000.00
    quantidade: int = 2 
    compra_realizada: boll = True
    #calcular o total da compra 

    total_compra: float = preco * quantidade

    print("Nome", nome)
    print("Preço", preco)
    print("Quantidade", quantidade)
    print("Compra realizada", compra_realizada)
    print("Total da compra", total_compra)


def exemplo_entrada_dados():
    nome: str = input("Digite o nome: ")
    sobrenome: str = input("Digite seu sobrenome: ")
    idade: int = int(input("Digite sua idade: "))

    nome_completo: str = nome +" " + sobrenome

    texto: str = "Nome Completo: " + nome_completo + " tem " + str(idade) + " anos "
    print(texto)


# Ex.1: Criar a função exercicio_paciente

# - Solicitar os campos: nome, peso, altura e e-mail
# - Calcular o IMC do paciente 
# - Apresentar IMC e seus dados

def exercicio_paciente():
    nome: str = input("Digite o nome: ")
    peso: str = int(input("Digite seu peso: "))
    altura: float = float(input("Digite sua altura: "))
    email: str = input("Digite seu E-mail: ")
    altura = altura**2
    indice_imc: float = peso/(altura**2)
    print(str(altura) + " altura ao quadrado " )
    print(str(nome) + " seu peso é " + str(peso) + " e sua altura é " + str(altura) + " isso resulta no IMC de " + str(indice_imc) + " segue uma cópia do resultado para seu e-mail " + str(email)+ ".")
    print(nome)
    print(peso)
    print(altura)
    print(email)
    print("Consulta finalizada, Volte sempre")









# - Ex.2 Criar a Função exercicio_carro 
# - Solicitar os campos: modelo do carro, quantidades parcelas, valor de cada parcela e valor da fipe.
# -  calcular o total pago no carro
# - calcular o valor total pago de juros ( total pago - valor da fipe)
# - Apresentar todos os dados do usúario
def exercicio_carro():
    modelo_carro: str = input("Digite o modelo do carro: ")
    falta_parcelas: int = input("Informe quantas parcelas faltam para pagamento: ")
    valor_parcela: float = input("Informe o valor da parcela! ")
    fip_carro: float = input("Qual o valor da tabela FIPE do veículo? ")

    total_carro: float = float(falta_parcelas) * float(valor_parcela)
    juros_carro: float = float(total_carro) - float(fip_carro)
    print("Seu carro " + str(modelo_carro) + " custou " + str(total_carro) + " e você pagou " + str(juros_carro) + " de juros. ")







if __name__ == "__main__":

    # exemplo_tipos_primitivos()
    # exemplo_entrada_dados()
    # exercicio_paciente()
    exercicio_carro()

quantidade = int(input("Digite a quantidade comprada: ")) 
preco = int(input("Digite o preço unitário: "))
5
if quantidade > 0 and preco > 0:
    print("Total a pagar: R$", quantidade * preco)
else:
    print("Quantidade e preço devem ser maiores que zero.")
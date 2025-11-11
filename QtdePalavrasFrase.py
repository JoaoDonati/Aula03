
frase=str(input("Digite uma frase: "))

nova_frase=frase.replace(",","")

palavras=nova_frase.split()

contagem_palavras={}

for palavra in palavras:
    palavra_minuscula=palavra.lower()
    if palavra_minuscula in contagem_palavras:
        contagem_palavras[palavra_minuscula] += 1
    else:
        contagem_palavras[palavra_minuscula] = 1

print(contagem_palavras)    
        
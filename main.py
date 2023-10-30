""" 
    O mercado 'Seu José' está com uma promoção de 10% para seus clientes maiores de 18 anos. Faça um programa em Phyton que pergunte a idade, o valor do total e mostre se ele pode ou não ter o desconto, qual o desconto e o valor final.
"""
idade = int(input("Digite sua idade:\n"))
total = float(input("Digite o valor total dos produtos:\n"))

if(idade>=18):
    print ("Pode ter o desconto")
    desconto = total * 0.1
    final = total - desconto
    print (f"O desconto foi de R${desconto} e o total é de R${final}")
else:
    print(f"Não tem direito ao desconto e o seu valor final é de R${total}")
    os.system('clear')
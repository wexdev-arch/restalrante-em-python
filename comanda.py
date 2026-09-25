print(" SISTEMA DE COMANDA ")

valor = float(input("Digite o valor da reffeição R$: "))
if valor <= 100:
 taxa = 0

elif valor <= 150:
 taxa = valor * 0.10

else :
 taca = valor * 0.15

taxa = 0 
desconto = 0

if valor > 200:
 desconto = valor * 0.05

total = valor + taxa - desconto

print("\n--CONSULMO DA MESA--")
print(f"valor da refeição R$ {valor:.2f}")
print (f"Taxa de serviço {taxa:.2f}")
print(f"Desconto {desconto:.2f}")
print(f"Total a pagar R$ {valor:.2f}")

#--Painel interativo
fila_espera = ["Senha 01", "Senha 02", "Senha 03","Senha 04"]
senha_atual = 0 
while senha_atual < len(fila_espera):
  print("\n===============")
  print(f"Senha Atual:{fila_espera[senha_atual - 1]}")
  if senha_atual > 0:
    print(f"Senha Anterior: {fila_espera[senha_atual] -1}")
  else: 
    print(f"Senha Anterior: Nenhuma (Primeiro Atendimento)")
print("=" * 10)
if senha_atual + 1 < len(fila_espera):
    print(f"Proximo da fila {fila_espera[senha_atual - 1]}")
else:
      print(f"Fila Vazia! Não há mais senhas.")

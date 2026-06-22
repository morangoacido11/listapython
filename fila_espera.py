#--Fila de espera--
print("----Painel de Atendimento----")
print("="*30)
fila_espera = ["Senha 01", "Senha 02", "Senha 03", "Senha 04" ]
print(f"O proximo paciente a ser atendido é: {fila_espera[0]}")
print(f"O segundo paciente a ser atendido é: {fila_espera[1]}")
print(f"Logo após o paciente {fila_espera[1]}, será o paciente {fila_espera[2]}")
print("="*30)
total = len(fila_espera)
print(f"Total de pessoas no aguardo: {total}")

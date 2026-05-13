#--Quiz-- 
#--Por Ana Gabriely 2E-DS
import time
time.sleep(1)
print("Seja bem-vindo ao quiz!ヾ(≧▽≦*)o")
time.sleep(1)
print("Tema: Astronomia!🪐")
print("Certifique-se de acertar todas!")
print("")
time.sleep(1)
#--Primeira pergunta--
print("1. Há som no espaço?🌌")
print("a. Sim, porem são ruídos baixo que um ouvido humano não pode ouvir")
print("b. O espaço não possui oxigenio para emitir som.\n c. Não há estudo científico sobre isso.")
print("*Responda com apenas uma letra que corresponde as alternativas!*")
resposta1 = input("").lower().strip()
while resposta1 == "" and not resposta1.strip():
    print("insira pelo menos um caractere!")
    resposta1 = input("").lower().strip()
while not resposta1 == "b" and not resposta1 == "a" and not resposta1 == "c":
    print("Resposta invalida. Responda com: a, b ou/e c.")
    resposta1 = input("").lower().strip()
if not resposta1 == "b":
    print("Não é muito bem isso. Você ganhou +1 erro.")
else:
    print("Parabens! Você acertou! ")
#--Segunda pergunta--
time.sleep(1)
print("2. Quantas luas tinha Saturno?🪐")
print("a. 194.\n b. 276\n c. 274\n")
resposta2 = input("").lower().strip()
while resposta2 == "" and not resposta2.strip():
    print("insira pelo menos um caractere!")
    resposta2 = input("").lower().strip()
while not resposta2 == "c" and not resposta2 == "a" and not resposta1 == "b":
    print("Resposta invalida. Responda com: a, b ou/e c.")
    resposta2 = input("").lower().strip()
if not resposta2 == "c":
    print("Não é muito bem isso. Você ganhou +1 erro.")
else:
    print("Parabens! Você acertou! ")
#---Ultima pergunta-- 
time.sleep(1)
print("3. Por que não caimos para fora da terra ja que sua circuferencia é redonda?🌍")
time.sleep(1)
print("a. Pela gravidade.\n b. A terra na verdade é plana.\n c. Temos poderes.\n")
resposta3 = input("").lower().strip()
while resposta3 == "" and not resposta3.strip():
    print("insira pelo menos um caractere!")
    resposta3 = input("").lower().strip()
while not resposta3 == "a" and not resposta3 == "b" and not resposta3 == "c":
    print("Resposta invalida. Responda com: a, b ou/e c.")
    resposta3 = input("").lower().strip()
if not resposta3 == "a":
    print("Não é muito bem isso. Você ganhou +1 erro.")
else:
    print("Parabens! Você acertou! ")
#--Conclusão-- 
time.sleep(1)
print("Você finalizou o quiz, parabens!")
total_de_erros = input("Quantas vezes você errou?: ")
while total_de_erros =="": 
    print("insira pelo menos um numero!")
    total_de_erro = input("")
while not total_de_erros == "1" and total_de_erros != "2" and total_de_erros !="3" and total_de_erros !="0": 
    print("Coloque apenas numeros!/ Coloque apenas numeros que correspondem as questões!")
    total_de_erros = input("")
if total_de_erros == "0":
    print("Parabens! Você não errou nenhuma!")
else:
    print("Poxa, não foi dessa vez!")

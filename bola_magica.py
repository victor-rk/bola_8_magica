# Programa feito para treinar os módulos nativos "random" e "time" do Python
# Desenvolvido por Victor Riki

import random
import time
import sys

respostas = [
    "Com certeza!",
    "Sem dúvidas",
    "Provavelmente sim",
    "Sim",
    "Não sei dizer, pergunte novamente mais tarde",
    "Não conte com isso",
    "Provavelmente não",
    "Com certeza não",
]

def animarTextoCarregando(texto):
    for ponto in range (1,4):
        sys.stdout.write(f"\r{texto}{"." * ponto}")
        sys.stdout.flush()
        time.sleep(0.7)
    print()

print()
print("•"*35)
print("        🔮 BOLA 8 MAGICA 🔮       ")
print("•"*35)

print("\nPara sair escreva 'Sair'\n")
print("•"*35)

while True:
    pergunta = input("\nFaça uma pergunta: ").strip()

    if pergunta.lower() == "sair":
        print()
        animarTextoCarregando("Encerrando o programa")
        break

    if not pergunta:
        print("Insira uma pergunta!")
        continue

    print()
    animarTextoCarregando("Consultando resposta")
    time.sleep(0.5)

    respostaFinal = random.choice(respostas)

    print(f"\nPergunta: {pergunta}")
    print(f"Resposta: {respostaFinal}")
    time.sleep(0.7)


    
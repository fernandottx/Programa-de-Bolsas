animais = [
    "cachorro", "gato", "elefante", "leão", "tigre",
    "girafa", "zebra", "urso", "lobo", "macaco",
    "rinoceronte", "hipopótamo", "anta", "tamanduá", "cervo",
    "coruja", "águia", "jacaré", "cobra", "pinguim"
]

animais.sort()

[print(animal) for animal in animais]

with open("Sprint-6/Exercicios/parte1-geração-e-massa-de-dados/etapa2/animais.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines([f'{animal}\n' for animal in animais])

#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# programa1.py - Primeiro programa em Python

"""
Importa o modulo random e sorteia
um numero entre 1 e 100
"""

import random
numero = random.randint(1, 100)

escolha = 0
tentativas = 0

while escolha != numero:
	escolha = input("Escolha um numero entre 1 e 100 ")
	tentativas += 1
	if escolha < numero:
		print "O numero", escolha, "eh menor que o numero escolhido"
	elif escolha > numero:
		print "O numero", escolha, "eh maior que o numero escolhido"

print "Parabens! Voce acertou em", tentativas, "tentativas"


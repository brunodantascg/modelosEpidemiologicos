# Solução problema de idetificação de parâmetros modelo SIR

import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

# (1) - INPUT
# Tamanho da população
N = 402912

# Acumulado de pessoas infectadas, em M pontos no tempo
acumuladoInfectados = [30, 50, 60]
somaAcumuladoInfectados = 0

# Acumulado de pessoas recuperadas, em M pontos no tempo
acumuladoRecuperados = [10, 20, 40]
somaAcumuladoRecuperados = 0

# Acumulado de pessoas mortas, em M pontos no tempo
acumuladoMortos = [300, 450, 600]
somaAcumuladoMortos = 0

# Soma Infectados
def somaInfectados(acumuladoInfectados, somaAcumuladoInfectados):
    for i in acumuladoInfectados:
        somaAcumuladoInfectados += i

    return somaAcumuladoInfectados

# Soma Recuperados
def somaRecuperados(acumuladoRecuperados, somaAcumuladoRecuperados):
    for i in acumuladoRecuperados:
        somaAcumuladoRecuperados += i

    return somaAcumuladoRecuperados

# Soma Mortos
def somaMortos(acumuladoMortos, somaAcumuladoMortos):
    for i in acumuladoMortos:
        somaAcumuladoMortos += i

    return somaAcumuladoMortos

I = somaInfectados(acumuladoInfectados, somaAcumuladoInfectados)
R = somaRecuperados(acumuladoRecuperados, somaAcumuladoRecuperados)
M = somaMortos(acumuladoMortos, somaAcumuladoMortos)

# (2) - Step 1 (Processar os dados de entrada de acordo com (7))

Rj = R + M
Ij = I - R
Sj = N - Ij - Rj

# (3) - Step 2 (Resolva o problema de identificação de parâmetro inverso discreto no tempo)

print(Rj)
print(Ij)
print(Sj)

# (4) - Output

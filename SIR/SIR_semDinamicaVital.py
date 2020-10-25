# SIR sem dinâmica vital

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# N = população total
N = 1000

# Número Inicial de Indivíduos Infectados
I0 = 1

# Número de Indivíduos Recuperados
R0 = 0

# S0 = Suscetíveis à infecção inicialmente
S0 = N - I0 - R0

# Taxa de contato (beta)
beta = 0.2

# Taxa média de recuperação (gama)
gama = 1/10

# Tempos em dias
tempo = np.linspace(0, 365, 365)

# Equações diferenciais do modelo
def equacoesSIR(y, tempo, N, beta, gama):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gama * I
    dRdt = gama * I
    return dS, dI, dR

# Vetor de condições iniciais
y0 = S0, I0, R0

# Integração das equações SIR no tempo
i = odeint(equacoesSIR, y0, tempo, args=(N, beta, gama))
S, I, R = i.T

# Visualização dos dados em três curvas variavel x tempofig
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#C1FFEC', axisbelow=True) # Tamanho e Cor de fundo
ax.plot(tempo, S/1000, 'b', alpha=0.9, lw=2, label='Suscetíveis')
ax.plot(tempo, I/1000, 'r', alpha=0.9, lw=2, label='Infectados')
ax.plot(tempo, R/1000, 'g', alpha=0.9, lw=2, label='Recuperados')
ax.set_xlabel('Tempo (dias)')
ax.set_ylabel('Número de')
ax.set_ylim(0,1.2)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()

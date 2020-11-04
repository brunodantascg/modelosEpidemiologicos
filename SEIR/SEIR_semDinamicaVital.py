# SEIR sem dinâmica vital

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# N = população total
N = 10000

# Número Inicial de Indivíduos Infectados
I0 = 1

# Número de Indivíduos Recuperados
R0 = 0

# S0 = Suscetíveis à infecção inicialmente
S0 = N - I0 - R0

# População Exposta
E = 200
E0 = 200

# Taxa de incubação (sigma)
sigma = 0.3

# Taxa de contato/infecção (beta)
beta = 0.2

# Taxa média de recuperação (gama)
dias = 10
gama = 1/dias

# Tempos em dias
tempo = np.linspace(0, 365, 365)

# Equações diferenciais do modelo
def equacoesSEIRs(y, tempo, N, E, sigma, beta, gama):
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gama * I
    dRdt = gama * I
    return dSdt, dEdt, dIdt, dRdt

# Vetor de condições iniciais
y0 = S0, E0, I0, R0

# Integração das equações SIR no tempo
i = odeint(equacoesSEIRs, y0, tempo, args=(N, E, sigma, beta, gama))
S, E, I, R = i.T

# Visualização dos dados em três curvas variavel x tempofig
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#C1FFEC', axisbelow=True) # Tamanho e Cor de fundo
ax.plot(tempo, S/1000, 'b', alpha=0.9, lw=2, label='Suscetíveis')
ax.plot(tempo, I/1000, 'r', alpha=0.9, lw=2, label='Infectados')
ax.plot(tempo, R/1000, 'g', alpha=0.9, lw=2, label='Recuperados')
ax.plot(tempo, E/1000, 'y', alpha=0.9, lw=2, label='Exposto')
ax.set_xlabel('Tempo (dias)')
ax.set_ylabel('Número de')
ax.set_ylim(0,10.2)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()

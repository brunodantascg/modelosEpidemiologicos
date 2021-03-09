# SIRS com dinâmica vital

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# N = população total
N = 402912

# Número Inicial de Indivíduos Infectados
I0 = 1

# Número de Indivíduos Recuperados
R0 = 0

# S0 = Suscetíveis à infecção inicialmente
S0 = N - I0

# Taxa de contato/infecção (beta)
beta = 1.64

# Taxa média de recuperação (gama)
dias = 15
gama = 1/dias

# Taxa de mortalidade (mi)
mi = 0.1
# Taxa de natalidade (ni)
ni = 0.2
# Taxa de incubação (sigma)
Csi = 0.3

# Tempos em dias
tempo = np.linspace(0, 40, 40)

# Equações diferenciais (ODE) do modelo SIRS com dinâmica vital 
def equacoesSIRSc(y, tempo, N, beta, mi, ni):
    S, I, R = y
    dSdt = mi * N - beta * S * I / N + Csi * R - ni * S
    dIdt = beta * S * I / N - gama * I - ni * I
    dRdt = gama * I - Csi * R - mi * R
    return dSdt, dIdt, dRdt

# Vetor de condições iniciais
y0 = S0, I0, R0

# Integração das equações SIRS no tempo
i = odeint(equacoesSIRSc, y0, tempo, args=(N, beta, gama, Csi))
S, I, R = i.T

# Visualização dos dados em três curvas variavel x tempofig
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#C1FFEC', axisbelow=True) # Tamanho e Cor de fundo
ax.plot(tempo, S/100000, 'b', alpha=0.9, lw=2, label='Suscetíveis')
ax.plot(tempo, I/100000, 'r', alpha=0.9, lw=2, label='Infectados')
ax.plot(tempo, R/100000, 'g', alpha=0.9, lw=2, label='Recuperados')
ax.plot(tempo, S/100000, 'y', alpha=0.9, lw=2, label='População em declínio')
ax.set_xlabel('Tempo (dias)')
ax.set_ylabel('Número População (100000)')
ax.set_ylim(0,4.2)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()

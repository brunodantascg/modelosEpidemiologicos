# Modelos Epidemiológicos (Python) 

S = Susceptível

I = Infeccioso

R = Recuperado

S = Susceptível

# SIR (Susceptível - Infeccioso - Recuperado)

O modelo SIR assume que as pessoas carregam imunidade vitalícia a uma doença após a recuperação; este é o caso de uma variedade de doenças.

SIR = S, I e R representam o número de indivíduos suscetíveis, infectados e recuperados, e N = S + I + R é a população total.

  SIR - em uma população fechada sem dinâmica vital: Se o curso da infecção for curto (surto emergente) em comparação com a vida de um indivíduo e a doença não for fatal, a dinâmica vital (nascimento e morte) pode ser ignorada. Na forma determinística, o modelo SIR pode ser escrito como a seguinte equação diferencial ordinária (ODE).
  Logo,
  
  dS = -beta * S * I / N
  
  dI = beta * S * I - gama * I
  
  dR = gama * I
  
  Onde N=S+I+R é a população total.
  
  SIR - em uma população com dinâmica vital: os novos nascimentos podem proporcionar indivíduos mais suscetíveis à população, sustentando uma epidemia ou permitindo que novas introduções se espalhem pela população. Em uma população realista como essa, a dinâmica da doença atingirá um estado estacionário.
  Onde,
  
  ni = natalidade
  
  mi = mortalidade
  
  Logo,
  
  dS = mi * N - beta * S * I - ni * S
  
  dI = beta * S * I - gama * I - ni * I
  
  dR = gama * I - ni * R

  Onde N=S+I+R é a população total.

# SIRS (Susceptível - Infeccioso - Recuperado - Susceptível)

O modelo SIRS é usado para permitir que os indivíduos recuperados retornem ao estado suscetível.

  SIRS - em uma população fechada sem dinâmica vita: Se houver influxo suficiente para a população suscetível, no equilíbrio a dinâmica estará em um estado endêmico com oscilação amortecida. Logo,
  
  dS = -beta * S * I + Csi * R
  
  dI = beta * S * I - gama * I
  
  dR = gama * I - Csi * R
  
  Onde N=S+I+R é a população total.
  
  SIRS - em uma população com dinâmica vital:

# SEIR ()

# SEIRS ()

# SI ()

# SIS ()

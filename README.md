# Modelos Epidemiológicos (Python) 

S = Susceptível

I = Infeccioso

R = Recuperado

S = Susceptível

# SIR (Susceptível - Infeccioso - Recuperado)

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


  SIRS sem dinâmica vital
  
  SIRS com dinâmica vital

# SEIR ()

# SEIRS ()

# SI ()

# SIS ()

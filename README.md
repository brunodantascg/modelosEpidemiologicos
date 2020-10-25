# Modelos Epidemiológicos (Python) 

S = Susceptível

I = Infeccioso

R = Recuperado

S = Susceptível

# SIR (Susceptível - Infeccioso - Recuperado)

SIR = S, I e R representam o número de indivíduos suscetíveis, infectados e recuperados, e N = S + I + R é a população total.

  SIR sem dinâmica vital: Se o curso da infecção for curto (surto emergente) em comparação com a vida de um indivíduo e a doença não for fatal, a dinâmica vital (nascimento e morte) pode ser ignorada. Na forma determinística, o modelo SIR pode ser escrito como a seguinte equação diferencial ordinária (ODE).
  Logo,
  dS = -beta * S * I / N
  dI = beta * S * I - gama * I
  dR = gama * I
  
  Onde N=S+I+R é a população total.
  
  SIR com dinâmica vital

# SIRS (Susceptível - Infeccioso - Recuperado - Susceptível)


  SIRS sem dinâmica vital
  
  SIRS com dinâmica vital

# SEIR ()

# SEIRS ()

# SI ()

# SIS ()

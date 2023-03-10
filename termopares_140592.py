# Trabalho sobre termopares. Marina Zanotta Rocha 140592

import numpy as np    #bibliote matematica
import matplotlib.pylab as plt  #biblioteca p/ grafico

# definicao dos coeficientes de cada tipo de termopar

c_B = (0, -0.246508183460e-3, 0.590404211710e-5,     -0.132579316360e-8, 0.156682919010e-11, -0.169445292400e-14, 0.629903470940e-18)
c_E = (0, 0.586655087100e-1,     0.450322755820e-4, 0.289084072120e-7, -0.330568966520e-9, 0.650244032700e-12, -0.191974955040e-15, -0.125366004970e-17, 0.214892175690e-20, -0.143880417820e-23, 0.359608994810e-27)
c_J = (0, 0.503811878150e-1,     0.304758369300e-4, -0.856810657200e-7, 0.132281952950e-9, -0.170529583370e-12, 0.209480906970e-15, -0.125383953360e-18, 0.156317256970e-22)
c_K = (-0.176004136860e-1,   0.389212049750e-1,  0.185587700320e-4, -0.994575928740e-7, 0.318409457190e-9, -0.560728448890e-12, 0.560750590590e-15, -0.320207200030e-18, 0.971511471520e-22, -0.121047212750e-25)
c_N = (0, 0.259293946010e-1,     0.157101418800e-4, 0.438256272370e-7, -0.252611697940e-9, 0.643118193390e-12, -0.100634715190e-14, 0.997453389920e-18, -0.608632456070e-21, 0.208492293390e-24, -0.306821961510e-28)
c_R = (0, 0.528961729765e-2,     0.139166589782e-4, -0.238855693017e-7, 0.356916001063e-10, -0.462347666298e-13, 0.5007774410340e-16, -0.373105886191e-19, 0.157716482367e-22, -0.281038625251e-26)
c_S = (0, 0.540313308631e-2,     0.125934289740e-4, -0.232477968689e-7, 0.322028823036e-10, -0.331465196389e-13, 0.255744251786e-16, -0.125068871393e-19, 0.271443176145e-23)
c_T = (0, 0.387481063640e-1,     0.332922278800e-4, 0.206182434040e-6, -0.2188225684603e-8, 0.109968809280e-10, -0.308157587720e-13, 0.454791352900e-16, -0.275129016730e-19)

#definicao dos outros parametros do tipo K

a0 = 0.118597600000
a1 = -0.118343200000e-3
a2 = 0.126968600000e3

# funcao para cada tipo de termopar

def B_type(x):
  y = 0.0
  for i in range (7):  # 8 coeficientes, a contagem inicia do 0
    y += c_B[i]*x**i   #polinomio que descreve a curva
  return y             # retorna o valor da tensao (eixo y)
  
def E_type(x):
  y = 0.0
  for i in range (10):
    y += c_E[i]*x**i
  return y

def J_type(x):
  y = 0.0
  for i in range (5):
    y += c_J[i]*x**i
  return y

def K_type(x):
  y = 0.0
  for i in range (9):
    y += c_K[i]*x**i + a0*np.exp(a1*((x-a2)**2))
  return y

def N_type(x):
  y = 0.0
  for i in range (10):
    y += c_N[i]*x**i
  return y

def R_type(x):
  y = 0.0
  for i in range (4):
    y += c_R[i]*x**i
  return y

def T_type(x):
  y = 0.0
  for i in range (8):
    y += c_T[i]*x**i
  return y
  
def S_type(x):
  y = 0.0
  for i in range (8):
    y += c_S[i]*x**i
  return y

# valor da tensao para cada tipo
e_B = []
e_E = []
e_J = []
e_K = []
e_N = []
e_T = []
e_S = []
t = np.linspace(0,300,601)
#variacao da temperatura de 0 a 300 graus celsius com o passo de 0,5 graus
for x in t:
  e_B.append(B_type(x))
  e_E.append(E_type(x))
  e_J.append(J_type(x))
  e_K.append(K_type(x))
  e_N.append(N_type(x))
  e_T.append(T_type(x))
  e_S.append(S_type(x))
  
#plotar curva de cada tipo de termopar
plt.plot(t, e_B, label = 'Type B')  
plt.plot(t, e_E, label = 'Type E')
plt.plot(t, e_J, label = 'Type J')
plt.plot(t, e_K, label = 'Type K')
plt.plot(t, e_N, label = 'Type N')
plt.plot(t, e_T, label = 'Type T')
plt.plot(t, e_S, label = 'Type S')
plt.legend(framealpha=1, frameon=True);
plt.xlabel('Temperature (??C)')  #legendas
plt.ylabel('E(t) (mV)')
plt.show()

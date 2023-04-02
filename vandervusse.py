# Este código implementa uma solução numérica para o sistema de equações diferenciais
# que descrevem a cinética química da reação de van der Vusse em um reator químico. A
# reação química é dada por:
# 2 A --> B
# B + C --> 2 C
# A --> D
# O código utiliza a solução numérica por diferenças finitas para calcular as 
# concentrações dos reagentes e produtos em função do tempo. As constantes cinéticas 
# da reação e outras propriedades do sistema são definidas no início do código, 
# juntamente com as condições iniciais para as concentrações e o volume do reator.
# O resultado final é um gráfico da evolução das concentrações de cada espécie química 
# em função do tempo, usando a biblioteca matplotlib para visualização de dados. 
# As concentrações são plotadas em diferentes cores para facilitar a distinção.

import matplotlib.pyplot as plt

import pandas as pd

plt.style.use('seaborn-poster')

#Constantes
k1 = 10
k2 = 1
k3 = 0.5
A = 5
Cv = 7 

Ca0 = 0.6
Cb0 = 0
Cc0 = 0 
Cd0 = 0 

#Vasão volumétrica
Fvol0 = 0.00278 #m^3/s

#Isotermico e isobarico
T = 550
P = 1

#nivel do reator 
h0 = 0.5 

#definição dos passos
ts = 0.001
te = 10

tf = 8000
V = []
h = []
Ca = []
Cb = []
Cc = []
Cd = []
time = []

V.append(h0*A)
h.append(h0)
Ca.append(Ca0)
Cb.append(Cb0)
Cc.append(Cc0)
Cd.append(Cd0)
time.append(0)

#Equacoes
for t in range(tf-1):
    Ca.append(Ca[t] + ts*((Fvol0*Ca0)/V[t] - (Fvol0*Ca[t])/V[t] - k1*Ca[t] - (2*k3*(Ca[t])**2)))
    Cb.append(Cb[t] + ts*((Fvol0*Cb0)/V[t] - (Fvol0*Cb[t])/V[t] + (k1*Ca[t]) - (k2*Cb[t])))
    Cc.append(Cc[t] + ts*((Fvol0*Cc0)/V[t] - (Fvol0*Cc[t])/V[t] + (k2*Cb[t])))
    Cd.append(Cd[t] + ts*((Fvol0*Cd0)/V[t] - (Fvol0*Cd[t])/V[t] + (k3*Ca[t]**2)))
    h.append(h[t] + ts*(Fvol0/A - Cv*(h[t])**1.5/A))
    V.append(h[t]*A)
    time.append(time[t] + ts)
    
plt.figure(figsize = (12, 8))
plt.plot(time, Ca, 'bo--', label='Approximate', color = 'green')
plt.plot(time, Cb, 'bo--', label='Approximate', color = 'purple')
plt.plot(time, Cc, 'bo--', label='Approximate', color = 'blue')
plt.plot(time, Cd, 'bo--', label='Approximate', color = 'orange')
plt.show()

#Criar dataframe com as variáveis de interesse
df = pd.DataFrame({'time': time, 'Ca': Ca, 'Cb': Cb, 'Cc': Cc, 'Cd': Cd})

#Salvar dataframe em um arquivo CSV
df.to_csv('registros.csv', index=False)

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
t = []

V.append(h0*A)
h.append(h0)
Ca.append(Ca0)
Cb.append(Cb0)
Cc.append(Cc0)
Cd.append(Cd0)
t.append(0)

#Equacoes
for i in range(tf-1):
    Ca.append(Ca[i] + ts*((Fvol0*Ca0)/V[i] - (Fvol0*Ca[i])/V[i] - k1*Ca[i] - (2*k3*(Ca[i])**2)))
    Cb.append(Cb[i] + ts*((Fvol0*Cb0)/V[i] - (Fvol0*Cb[i])/V[i] + (k1*Ca[i]) - (k2*Cb[i])))
    Cc.append(Cc[i] + ts*((Fvol0*Cc0)/V[i] - (Fvol0*Cc[i])/V[i] + (k2*Cb[i])))
    Cd.append(Cd[i] + ts*((Fvol0*Cd0)/V[i] - (Fvol0*Cd[i])/V[i] + (k3*Ca[i]**2)))
    h.append(h[i] + ts*(Fvol0/A - Cv*(h[i])**1.5/A))
    V.append(h[i]*A)
    t.append(t[i] + ts)
    
plt.figure(figsize = (12, 8))
plt.plot(t, Ca, 'bo--', label='Approximate', color = 'green')
plt.plot(t, Cb, 'bo--', label='Approximate', color = 'red')
plt.plot(t, Cc, 'bo--', label='Approximate', color = 'blue')
plt.plot(t, Cd, 'bo--', label='Approximate', color = 'yellow')
plt.show()

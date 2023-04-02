# van der Vusse ReactorAI
Este repositório contém o código-fonte e os dados necessários para treinar uma inteligência artificial capaz de prever a taxa de conversão, bem como a concentração dos reagentes e produtos ao longo do tempo, em reatores químicos contínuos utilizando o modelo de Van de Vusse.

# Reação de Van der Vusse

A reação de Van der Vusse é um modelo de reação química que envolve a conversão de um reagente em um produto por meio de uma série de reações intermediárias. Essas reações ocorrem em um reator químico, que é um sistema fechado onde as condições de temperatura, pressão e concentração são controladas para garantir que a reação ocorra de maneira eficiente.

O modelo da reação de Van der Vusse é composto por quatro equações diferenciais que descrevem as taxas de conversão dos reagentes em produtos ao longo do tempo. Essas equações levam em consideração as concentrações dos reagentes e produtos, a temperatura e a pressão no reator, bem como a taxa de fluxo volumétrico de entrada e saída do reagente.

O modelo é amplamente utilizado na indústria química para projetar e otimizar reatores químicos, bem como para entender a cinética da reação. Ele também é usado em laboratórios de pesquisa para estudar reações químicas específicas e para entender a influência das diferentes variáveis ​​na reação.

A implementação do modelo de Van der Vusse pode ser realizada por meio de simulações numéricas em Python ou outras linguagens de programação. É uma técnica poderosa para prever o comportamento de uma reação química em diferentes condições e para otimizar o processo de produção.


$\begin{aligned}
\text{Balanço de massa volumétrico global: } \frac{dV}{dt} = F_{in} - F_{out} \\
\text{Equação da válvula: } F_{out} = C_v \sqrt{h} \\
\text{Balanço para o componente A: } \theta \frac{dC_A}{dt} &= C_{A,in} - C_{A,out} - \theta r_1 - 2\theta r_3 \\
\text{Balanço para o componente B: } \theta \frac{dC_B}{dt} &= C_{B,in} - C_{B,out} + \theta r_1 - \theta r_2 \\
\text{Balanço para o componente C: } \theta \frac{dC_C}{dt} &= C_{C,in} - C_{C,out} + \theta r_2 \\
\text{Balanço para o componente D: } \theta \frac{dC_D}{dt} &= C_{D,in} - C_{D,out} + \theta r_3
\end{aligned}$


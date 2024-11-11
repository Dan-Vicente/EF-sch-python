# Simulador de Equação de Schrödinger Fracionária

Este projeto implementa um simulador de equações de Schrödinger com derivadas fracionárias, tanto no formalismo de Caputo quanto no de Riemann-Liouville. O simulador calcula e plota a evolução temporal da função de onda de uma partícula quântica sob diferentes condições de derivada fracionária.

## Objetivo

O objetivo do projeto é calcular a evolução temporal de uma função de onda `ψ(x,t)` usando as derivadas fracionárias de Caputo e Riemann-Liouville, aplicadas à equação de Schrödinger. A principal aplicação disso é em sistemas quânticos com dinâmica não clássica, onde as derivadas fracionárias podem modelar efeitos de memória e dissipação.

## Estrutura do Projeto

### Funcionalidades Implementadas

1. **Derivada Fracionária de Riemann-Liouville**: Esta derivada fracionária é uma extensão da derivada clássica, utilizando uma integral com um kernel de ordem fracionária.
2. **Derivada Fracionária de Caputo**: Esta derivada é mais utilizada em contextos de modelagem de sistemas com memória, modificando o modo como a função de onda evolui no tempo.
3. **Simulação da Evolução Temporal**: Calcula a função de onda `ψ(x,t)` para diferentes valores de tempo `t` e plota a densidade de probabilidade `|ψ(x,t)|²` para visualização.
4. **Interface Gráfica**: Uma interface simples usando `Tkinter` que permite ao usuário ajustar a ordem da derivada fracionária `α` e escolher o tipo de derivada (Caputo ou Riemann-Liouville).

## Ferramentas Necessárias

O código foi desenvolvido e testado com as seguintes ferramentas:

- **Python 3.12**: A versão do Python utilizada.
- **Bibliotecas Python**:
  - **NumPy**: Para cálculos numéricos e manipulação de arrays.
  - **Matplotlib**: Para visualização dos resultados (gráficos).
  - **SciPy**: Para funções matemáticas avançadas, como a função `gamma`.
  - **SymPy**: Para o cálculo simbólico das derivadas fracionárias e integrais.
  - **Tkinter**: Para a interface gráfica simples de usuário.

Você pode instalar as dependências utilizando o seguinte comando:

```bash
pip install numpy matplotlib scipy sympy tk

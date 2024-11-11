import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import I, symbols, diff, Function
from matplotlib.offsetbox import AnchoredText

# Configuração de constantes e variáveis simbólicas
hbar, m, alpha = symbols('hbar m alpha', real=True, positive=True)
x, t = symbols('x t')
psi = Function('psi')(x, t)

# Definindo a Equação de Schrödinger Clássica
lhs_classical = I * hbar * diff(psi, t)
rhs_classical = -(hbar**2 / (2 * m)) * diff(psi, x, x)
schrodinger_classical = sp.Eq(lhs_classical, rhs_classical)

# Exibindo a Equação de Schrödinger Clássica
print("Equação de Schrödinger Clássica:")
sp.pprint(schrodinger_classical)

# Configurando o matplotlib para mostrar LaTeX
plt.rcParams.update({"text.usetex": True, "font.size": 12})

# Visualização da Equação Clássica
fig, ax = plt.subplots(figsize=(8, 2))
textstr = r"Equação de Schrödinger Clássica: $i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m} \frac{\partial^2 \psi}{\partial x^2}$"
anchored_text = AnchoredText(textstr, loc='center', frameon=False, pad=0)
ax.add_artist(anchored_text)
ax.axis('off')
plt.show()

# Conversão para a Equação de Schrödinger Fracionária
# Derivada fracionária de ordem alpha em relação ao tempo
lhs_fractional = I * hbar * sp.diff(psi, t, alpha)
rhs_fractional = -(hbar**2 / (2 * m)) * sp.diff(psi, x, 2)
schrodinger_fractional = sp.Eq(lhs_fractional, rhs_fractional)

# Exibindo a Equação de Schrödinger Fracionária
print("Equação de Schrödinger Fracionária:")
sp.pprint(schrodinger_fractional)

# Visualização da Equação Fracionária
fig, ax = plt.subplots(figsize=(8, 2))
textstr_fractional = r"Equação de Schrödinger Fracionária: $i\hbar \frac{\partial^\alpha \psi}{\partial t^\alpha} = -\frac{\hbar^2}{2m} \frac{\partial^2 \psi}{\partial x^2}$"
anchored_text_fractional = AnchoredText(textstr_fractional, loc='center', frameon=False, pad=0)
ax.add_artist(anchored_text_fractional)
ax.axis('off')
plt.show()

# Parâmetros numéricos e função de onda inicial para a simulação
hbar_value = 1  # Valor numérico para hbar
m_value = 1     # Valor numérico para m
alpha_value = 0.5  # Ordem fracionária desejada para a derivada no tempo

# Valores de x e t para avaliação numérica
x_values = np.linspace(-5, 5, 100)
t_values = np.linspace(0, 5, 50)

# Estado inicial psi_0 e cálculo numérico
psi_0 = sp.exp(-x**2)
psi_fractional = psi_0 * sp.exp(-I * (hbar_value / (2 * m_value)) * t * x**2)
psi_func = sp.lambdify((x, t), psi_fractional, 'numpy')

# Cálculo da função de onda fracionária ao longo do tempo
psi_values = np.zeros((len(t_values), len(x_values)), dtype=complex)
for i, t_val in enumerate(t_values):
    psi_values[i, :] = psi_func(x_values, t_val)

# Plotagem da evolução da função de onda fracionária
plt.figure(figsize=(10, 6))
for i in range(0, len(t_values), 10):  # Intervalo espaçado para visualização no tempo
    plt.plot(x_values, np.abs(psi_values[i, :])**2, label=f't = {t_values[i]:.1f}')

plt.xlabel("Posição x")
plt.ylabel("|psi(x, t)|^2")
plt.title("Evolução Temporal da Função de Onda Fracionária")
plt.legend()
plt.show()

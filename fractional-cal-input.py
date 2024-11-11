import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
from sympy import symbols, Function, I, integrate
from sympy.abc import t, x
from tkinter import *
from tkinter import ttk
import sympy as sp

# Configurações iniciais para Schrödinger Fracionária
hbar = 1  # Constante reduzida de Planck
m = 1     # Massa da partícula
alpha = 0.5  # Ordem fracionária inicial


# Funções de derivada fracionária de Caputo e Riemann-Liouville com conversão de limites
def caputo_fractional_derivative(f, t_symbol, alpha):
    # Converter t para um símbolo compatível com SymPy
    integral = integrate((t_symbol - t)**(alpha - 1) * sp.diff(f, t_symbol), (t_symbol, 0, t_symbol))
    return 1 / gamma(1 - alpha) * integral

def riemann_liouville_fractional_derivative(f, t_symbol, alpha):
    # Converter t para um símbolo compatível com SymPy
    integral = integrate(f / (t_symbol - t)**(1 - alpha), (t_symbol, 0, t_symbol))
    return 1 / gamma(alpha) * integral

# Interface gráfica
def run_simulation():
    global alpha, deriv_type
    alpha = float(alpha_var.get())  # Obtém a ordem fracionária do campo de entrada
    deriv_type = deriv_var.get()  # Obtém o tipo de derivada selecionado

    # Define a função de onda inicial
    x_vals = np.linspace(-10, 10, 200)  # Valores de x (posição)
    psi_0 = np.exp(-x_vals**2)  # Função de onda inicial gaussiana
    psi_evolution = []

    # Evolução da função de onda ao longo do tempo
    for t_val in np.linspace(0, 5, 100):  # Valores de tempo
        t_sym = sp.Symbol('t')
        
        # Calcula a derivada fracionária com base no tipo selecionado
        if deriv_type == "Caputo":
            fractional_term = caputo_fractional_derivative(psi_0, t_sym, alpha)
        elif deriv_type == "Riemann-Liouville":
            fractional_term = riemann_liouville_fractional_derivative(psi_0, t_sym, alpha)
        else:
            # Caso de derivada clássica (segunda derivada espacial)
            fractional_term = -hbar**2 / (2 * m) * np.gradient(np.gradient(psi_0, x_vals), x_vals)
        
        # Converter o termo fracionário para um valor numérico
        fractional_term_num = fractional_term.evalf(subs={t_sym: t_val})
        
        # Verificar se o termo fracionário é um número válido (não é NaN nem inf)
        try:
            # Garantir que o valor é um número real
            fractional_term_num = float(fractional_term_num)  # Converte para número real
            if np.isnan(fractional_term_num) or np.isinf(fractional_term_num):
                print(f"Valor inválido para o termo fracionário: {fractional_term_num} em t = {t_val}")
                fractional_term_num = 0  # Se for inválido, definir como zero
        except Exception as e:
            print(f"Erro ao tentar converter o termo fracionário para número: {e}")
            fractional_term_num = 0  # Caso de erro na conversão, define como zero
        
        # Depuração - Mostra o valor do termo fracionário
        print(f"Termo fracionário em t={t_val}: {fractional_term_num}")
        
        # Calcular a evolução temporal de psi
        try:
            # Verifique a exponencial antes de calcular psi_t
            if isinstance(fractional_term_num, (int, float)) and not np.isnan(fractional_term_num) and not np.isinf(fractional_term_num):
                if fractional_term_num == 0:
                    # Se o termo fracionário for zero, a exponencial será 1
                    psi_t = psi_0  # A evolução é apenas a função de onda inicial
                else:
                    psi_t = psi_0 * np.exp(-I * fractional_term_num * t_val)
            else:
                print(f"Valor inválido para exponenciação: {fractional_term_num}")
                psi_t = np.zeros_like(psi_0)  # Em caso de erro, definir como vetor de zeros
        except Exception as e:
            print(f"Erro ao calcular psi_t para t={t_val}: {e}")
            psi_t = np.zeros_like(psi_0)  # Em caso de erro, definir como vetor de zeros
        
        psi_evolution.append(np.abs(psi_t)**2)  # Armazena a densidade de probabilidade (|ψ(x,t)|²)
    
    # Exibir a evolução da função de onda
    plt.figure(figsize=(10, 6))
    for i, psi_t in enumerate(psi_evolution[::10]):  # Exibe uma fatia da evolução no tempo
        plt.plot(x_vals, psi_t, label=f't={i * 0.5:.2f}')  # Plota a densidade de probabilidade para alguns tempos
    plt.xlabel("Posição x")
    plt.ylabel("|ψ(x, t)|²")
    plt.title(f"Evolução Temporal com Derivada {deriv_type} de Ordem {alpha}")
    plt.legend()
    plt.show()

# Configurações da interface gráfica
root = Tk()
root.title("Simulador de Equação de Schrödinger Fracionária")

# Campo de entrada para a ordem fracionária α
alpha_label = Label(root, text="Ordem Fracionária (α):")
alpha_label.grid(row=0, column=0, padx=10, pady=5)
alpha_var = StringVar(root)
alpha_var.set("0.5")  # Valor padrão
alpha_entry = Entry(root, textvariable=alpha_var)
alpha_entry.grid(row=0, column=1, padx=10, pady=5)

# Menu de seleção do tipo de derivada
deriv_label = Label(root, text="Tipo de Derivada:")
deriv_label.grid(row=1, column=0, padx=10, pady=5)
deriv_var = StringVar(root)
deriv_var.set("Caputo")  # Valor padrão
deriv_menu = ttk.Combobox(root, textvariable=deriv_var, values=["Caputo", "Riemann-Liouville"])
deriv_menu.grid(row=1, column=1, padx=10, pady=5)

# Botão para executar a simulação
run_button = Button(root, text="Executar Simulação", command=run_simulation)
run_button.grid(row=2, columnspan=2, pady=10)

# Inicialização da interface gráfica
root.mainloop()

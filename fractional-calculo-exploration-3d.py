import numpy as np
import matplotlib.pyplot as plt

# Função de onda inicial (exemplo)
psi_0 = 1 + 0j  # psi_0 pode ser um valor complexo, por exemplo

# Ordem fracionária (α)
alpha = 0.5  # Modifique este valor conforme necessário

# Tempo e parâmetros
t_values = np.linspace(0, 10, 100)  # Valores de tempo (ajuste conforme necessário)
x_values = np.linspace(-10, 10, 100)  # Posições (ajuste conforme necessário)

# Defina a unidade imaginária
I = 1j

# Função para calcular o termo fracionário (exemplo simples)
def calculate_fractional_term(alpha, t_val):
    # Simples exemplo de cálculo de termo fracionário (ajuste conforme necessário)
    # A fórmula pode variar dependendo da definição da derivada fracionária
    fractional_term = alpha * t_val ** (alpha - 1)  # Exemplo de comportamento com α
    return fractional_term

# Função para simular a evolução da função de onda
def run_simulation():
    global psi_0
    global alpha
    global I
    
    # Vamos criar uma lista para armazenar os valores de psi para cada t
    psi_values = []

    # Loop sobre os valores de tempo
    for t_val in t_values:
        # Verifique se t_val é um valor válido
        if np.isnan(t_val) or np.isinf(t_val):
            print(f"Erro: t_val é inválido: {t_val}")
            continue  # Pula o cálculo se t_val for inválido

        # Calcule o termo fracionário para o tempo t_val
        fractional_term = calculate_fractional_term(alpha, t_val)

        # Verifique se o termo fracionário é válido
        if np.isnan(fractional_term) or np.isinf(fractional_term):
            print(f"Erro: fractional_term é inválido para t_val={t_val}")
            continue  # Pula o cálculo se fractional_term for inválido

        # Exibição para depuração
        print(f"Calculando para t = {t_val}, termo fracionário = {fractional_term}")

        # Agora calculamos psi_t para cada valor de x
        psi_t_values = []
        for x_val in x_values:
            # Calcule a evolução da função de onda com base no termo fracionário
            try:
                psi_t = psi_0 * np.exp(-I * fractional_term * t_val) * np.exp(-I * x_val)  # Exemplo de evolução com x
                psi_t_values.append(np.real(psi_t))  # Adiciona a parte real de psi_t
            except Exception as e:
                print(f"Erro ao calcular psi_t para t_val={t_val} e x_val={x_val}: {e}")
                continue

        # Armazene os valores de psi_t para cada t
        psi_values.append(psi_t_values)
    
    # Agora vamos plotar os gráficos para diferentes tempos
    plt.figure(figsize=(10, 6))
    
    # Plotando a evolução para alguns tempos
    for i, t_val in enumerate(t_values[::20]):  # Pega um valor de tempo a cada 20 valores
        plt.plot(x_values, psi_values[i], label=f'Tempo = {t_val:.2f}')
    
    plt.title('Evolução da Função de Onda ao Longo do Tempo')
    plt.xlabel('Posição (x)')
    plt.ylabel('Re(ψ(x, t))')
    plt.legend()
    plt.grid(True)
    plt.show()

# Execute a simulação
run_simulation()

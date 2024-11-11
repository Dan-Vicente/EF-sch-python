<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projeto: Solução Fracionária da Equação de Schrödinger</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            line-height: 1.6;
            margin: 20px;
        }

        h1 {
            text-align: center;
            color: #4CAF50;
        }

        h2 {
            color: #333;
        }

        h3 {
            color: #666;
        }

        p {
            margin-bottom: 10px;
        }

        code {
            background-color: #f4f4f4;
            padding: 2px 5px;
            font-size: 1rem;
            color: #d9534f;
        }

        ul {
            list-style-type: square;
        }

        .section {
            margin-bottom: 30px;
        }

        .highlight {
            background-color: #e7f3e7;
            padding: 10px;
            border-left: 4px solid #4CAF50;
        }

        .code-block {
            background-color: #f4f4f4;
            border: 1px solid #ccc;
            padding: 15px;
            white-space: pre-wrap;
            word-wrap: break-word;
            font-family: monospace;
        }

        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>

<body>

    <h1>Projeto: Solução Fracionária da Equação de Schrödinger</h1>

    <div class="section">
        <h2>Visão Geral</h2>
        <p>Este projeto explora a conversão da <strong>Equação de Schrödinger Clássica</strong> para uma forma <strong>fracionária</strong>. Além de mostrar a derivação simbólica, o código simula a evolução da função de onda ao longo do tempo e apresenta os cálculos intermediários. Cada passo é acompanhado de uma explicação visual usando LaTeX, facilitando o entendimento da transição da versão clássica para a fracionária.</p>
    </div>

    <div class="section">
        <h2>Estrutura do Projeto</h2>
        <h3>Principais Componentes</h3>
        <ul>
            <li><strong>Equação de Schrödinger Clássica</strong>: A versão clássica da equação de Schrödinger é definida como:</li>
            <pre class="code-block">
iℏ ∂ψ/∂t = -ℏ²/(2m) ∂²ψ/∂x²
            </pre>
            <li><strong>Conversão para a Forma Fracionária</strong>: A equação clássica é então adaptada para incluir uma <strong>derivada fracionária de ordem α</strong> com relação ao tempo:</li>
            <pre class="code-block">
iℏ ∂^αψ/∂t^α = -ℏ²/(2m) ∂²ψ/∂x²
            </pre>
            <li><strong>Simulação e Evolução Temporal da Função de Onda</strong>: Uma função de onda inicial é definida simbolicamente, e a evolução da função de onda fracionária ao longo do tempo é simulada numericamente para um conjunto de valores de t.</li>
        </ul>
    </div>

    <div class="section">
        <h2>Etapas e Visualizações</h2>
        <p>Para cada uma das etapas, o código gera uma explicação visual em LaTeX para ilustrar a transformação da equação clássica para a fracionária:</p>
        <ul>
            <li><strong>Equação de Schrödinger Clássica:</strong> A forma clássica da equação é exibida para referência.</li>
            <li><strong>Introdução da Derivada Fracionária:</strong> Substituição da derivada temporal clássica por uma derivada de ordem α, detalhando o novo termo de ordem α.</li>
            <li><strong>Operadores Diferenciais Fracionários:</strong> Explicação do uso de operadores fracionários diferenciais, introduzindo o fator de decaimento t^(-α) com relação à derivada no tempo.</li>
        </ul>
    </div>

    <div class="section">
        <h2>Requisitos</h2>
        <p>Para executar o código, você precisará dos seguintes pacotes Python:</p>
        <ul>
            <li><code>numpy</code></li>
            <li><code>matplotlib</code> (com suporte a LaTeX instalado)</li>
            <li><code>sympy</code></li>
        </ul>
        <p>Caso algum desses pacotes não esteja instalado, use o seguinte comando:</p>
        <pre class="code-block">
pip install numpy matplotlib sympy
        </pre>
        <p>Certifique-se de que o suporte a LaTeX está configurado corretamente para que o Matplotlib consiga renderizar as equações em LaTeX.</p>
    </div>

    <div class="section">
        <h2>Execução</h2>
        <p>Para rodar o projeto, basta executar o código Python:</p>
        <pre class="code-block">
python schrodinger_fractional.py
        </pre>
        <p>O código exibirá os cálculos intermediários e a evolução da função de onda ao longo do tempo.</p>
    </div>

    <div class="section">
        <h2>Resultados Esperados</h2>
        <ul>
            <li><strong>Equações:</strong> Visualizações das formas clássica e fracionária da equação de Schrödinger, com as etapas intermediárias de cálculo.</li>
            <li><strong>Simulação Gráfica:</strong> Gráficos que mostram a probabilidade <code>|ψ(x, t)|²</code> em função da posição <code>x</code> ao longo do tempo <code>t</code>, ilustrando a evolução da função de onda fracionária.</li>
        </ul>
        <p>Este projeto oferece uma introdução visual e numérica ao conceito de derivadas fracionárias na mecânica quântica, com o foco na equação de Schrödinger.</p>
    </div>

</body>

</html>

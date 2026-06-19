# 🐍 Análise de Dados Industriais com Python

## Sobre o Projeto

Análise exploratória de dados de produção industrial utilizando Python, Pandas e
Matplotlib. O projeto replica análises reais realizadas em Power BI, aplicando
Python para manipulação de dados, cálculo de KPIs e geração de visualizações.

---

## 🏭 Contexto

Os dados analisados representam um setor de injeção plástica com:
- **19 injetoras** monitoradas
- **Múltiplos operadores** por turno
- **Meta de OEE: 65%**
- **Meta de % Perda: 12%**

---

## 📊 Análises Realizadas

| # | Análise | Descrição |
|---|---------|-----------|
| 1 | OEE por Injetora | Ranking de eficiência global por máquina com linha de meta |
| 2 | Evolução Semanal de Perdas | % de perda semana a semana com destaque de desvio |
| 3 | Ranking de Operadores | OEE individual por operador com linha de meta |
| 4 | Heatmap de Correlação | Correlação entre disponibilidade, performance, aproveitamento e perdas |

---

## 🔍 Conceitos Utilizados

- Manipulação de dados com **Pandas** (`groupby`, `agg`, `assign`, `merge`)
- Visualizações com **Matplotlib** e **Seaborn**
- Cálculo de **OEE** — Disponibilidade × Performance × Aproveitamento
- **Heatmap de correlação** entre indicadores industriais
- Gráficos de barras horizontais com formatação condicional por meta
- Séries temporais com área de desvio destacada

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white)

---

## ▶️ Como Executar

```bash
# Clone o repositório
git clone https://github.com/rjpanisson/analise-dados-python

# Instale as dependências
pip install pandas matplotlib seaborn

# Execute a análise
python analise_producao.py
```

---

## 📁 Arquivos Gerados

Após executar o script, os seguintes gráficos são salvos automaticamente:
- `oee_por_injetora.png`
- `evolucao_perda_semanal.png`
- `oee_por_operador.png`
- `correlacao_indicadores.png`

---

## 👤 Autor

**Jhonathan Panisson**
Analista de Dados em Transição | Power BI · SQL · Python
[GitHub](https://github.com/rjpanisson) | [LinkedIn](https://linkedin.com/in/jhonathan-panisson)

# ============================================================
# ANÁLISE EXPLORATÓRIA DE DADOS DE PRODUÇÃO INDUSTRIAL
# Autor: Jhonathan Panisson
# Descrição: Análise de OEE, perdas e eficiência produtiva
#            usando Python, Pandas e Matplotlib
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

# Configuração visual
sns.set_theme(style="darkgrid")
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["font.family"] = "sans-serif"

# ============================================================
# 1. CARREGAMENTO E LIMPEZA DOS DADOS
# ============================================================

# Simulação de dados reais de produção
dados = pd.DataFrame({
    "data":         pd.date_range(start="2025-01-01", periods=90, freq="D"),
    "injetora":     ["Injetora_1", "Injetora_2", "Injetora_3"] * 30,
    "operador":     ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"] * 18,
    "producao_real":    [450, 380, 420, 390, 410, 360, 430] * 12 + [450, 380, 420],
    "producao_teorica": [500] * 90,
    "pecas_perdidas":   [30, 45, 25, 50, 35, 60, 20] * 12 + [30, 45, 25],
    "horas_parada":     [1.5, 2.0, 0.5, 3.0, 1.0, 2.5, 0.8] * 12 + [1.5, 2.0, 0.5],
    "disponibilidade":  [0.85, 0.80, 0.92, 0.75, 0.88, 0.78, 0.90] * 12 + [0.85, 0.80, 0.92],
    "performance":      [0.90, 0.76, 0.84, 0.78, 0.82, 0.72, 0.86] * 12 + [0.90, 0.76, 0.84],
    "aproveitamento":   [0.94, 0.88, 0.96, 0.87, 0.92, 0.85, 0.95] * 12 + [0.94, 0.88, 0.96],
})

# Calcular OEE
dados["oee"] = dados["disponibilidade"] * dados["performance"] * dados["aproveitamento"]
dados["pct_perda"] = dados["pecas_perdidas"] / dados["producao_teorica"] * 100
dados["mes"] = dados["data"].dt.to_period("M")
dados["semana"] = dados["data"].dt.isocalendar().week

print("=" * 50)
print("RESUMO GERAL DOS DADOS")
print("=" * 50)
print(f"Período analisado: {dados['data'].min().date()} a {dados['data'].max().date()}")
print(f"Total de registros: {len(dados)}")
print(f"OEE médio geral: {dados['oee'].mean() * 100:.1f}%")
print(f"% de perda média: {dados['pct_perda'].mean():.1f}%")
print(f"Total de peças perdidas: {dados['pecas_perdidas'].sum():,}")


# ============================================================
# 2. OEE POR INJETORA
# ============================================================

oee_injetora = (
    dados.groupby("injetora")[["disponibilidade", "performance", "aproveitamento", "oee"]]
    .mean()
    .mul(100)
    .round(2)
    .reset_index()
    .sort_values("oee", ascending=False)
)

print("\n" + "=" * 50)
print("OEE POR INJETORA")
print("=" * 50)
print(oee_injetora.to_string(index=False))

fig, ax = plt.subplots()
bars = ax.barh(oee_injetora["injetora"], oee_injetora["oee"],
               color=["#2C5F9E" if v >= 65 else "#E74C3C" for v in oee_injetora["oee"]])
ax.axvline(65, color="orange", linestyle="--", linewidth=1.5, label="Meta OEE (65%)")
ax.set_xlabel("OEE (%)")
ax.set_title("OEE por Injetora", fontsize=13, fontweight="bold")
ax.legend()
for bar, val in zip(bars, oee_injetora["oee"]):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
            f"{val:.1f}%", va="center",

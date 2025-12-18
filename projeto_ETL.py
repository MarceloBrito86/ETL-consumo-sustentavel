import pandas as pd

# Criando dados fictícios
dados = {
    "usuario": [1, 2, 3, 4, 5],
    "produtos_sustentaveis": [5, 2, 7, 0, 3],
    "total_produtos": [10, 4, 12, 5, 6],
    "regiao": ["Norte", "Sul", "Sudeste", "Nordeste", "Centro-Oeste"]
}

# Transformando em DataFrame
consumo = pd.DataFrame(dados)

print(consumo)

# Criar índice de sustentabilidade
consumo["indice_sustentavel"] = consumo["produtos_sustentaveis"] / consumo["total_produtos"]

# Tratar possíveis divisões por zero
consumo["indice_sustentavel"] = consumo["indice_sustentavel"].fillna(0)

print(consumo)

consumo.to_csv("consumo_transformado.csv", index=False)

import matplotlib.pyplot as plt

# Índice médio por região
media_regiao = consumo.groupby("regiao")["indice_sustentavel"].mean()

# Gráfico de barras
media_regiao.plot(kind="bar", color="green", alpha=0.7)
plt.title("Índice médio de sustentabilidade por região")
plt.ylabel("Índice Sustentável")
plt.xlabel("Região")
plt.show()

# Gráfico de pizza
consumo["produtos_sustentaveis"].sum()
consumo["total_produtos"].sum()

plt.pie(
    [consumo["produtos_sustentaveis"].sum(), consumo["total_produtos"].sum() - consumo["produtos_sustentaveis"].sum()],
    labels=["Sustentáveis", "Não Sustentáveis"],
    autopct="%1.1f%%",
    colors=["green", "gray"]
)
plt.title("Proporção de produtos sustentáveis")
plt.show()

# Gráfico de linha - Exemplo fictício de coluna de mês
consumo["mes"] = ["Jan", "Fev", "Mar", "Abr", "Mai"]

consumo.groupby("mes")["indice_sustentavel"].mean().plot(kind="line", marker="o", color="blue")
plt.title("Tendência do índice de sustentabilidade ao longo dos meses")
plt.ylabel("Índice Sustentável")
plt.xlabel("Mês")
plt.show()
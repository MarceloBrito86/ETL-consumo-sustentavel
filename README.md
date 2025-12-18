# 🌱 Projeto ETL: Consumo Sustentável no Brasil

Este projeto demonstra um pipeline ETL completo em Python, aplicado ao domínio de sustentabilidade e hábitos de consumo consciente. Utilizamos dados simulados para representar o comportamento de consumidores em diferentes regiões do Brasil, com foco na proporção de produtos sustentáveis adquiridos.

---

## ⚙️ Pipeline ETL

### 🔹 1. Extração
Os dados foram criados manualmente e armazenados em um arquivo CSV (`consumo_transformado.csv`), contendo:
- Número total de produtos comprados
- Quantidade de produtos sustentáveis
- Região geográfica

### 🔹 2. Transformação
Foi calculado o **índice de sustentabilidade** para cada usuário:
```python
indice_sustentavel = produtos_sustentaveis / total_produtos
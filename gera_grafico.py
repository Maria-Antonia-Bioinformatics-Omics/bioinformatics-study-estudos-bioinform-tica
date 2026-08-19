import matplotlib.pyplot as plt

# Dados simulados coletados do nosso pipeline
impactos = ["MODERATE", "HIGH", "LOW"]
quantidades = [1, 0, 0]  # No nosso VCF tivemos 1 moderada

plt.figure(figsize=(6, 4))
plt.bar(impactos, quantidades, color=["orange", "red", "green"])
plt.title("Resumo de Impacto das Variantes Genéticas")
plt.xlabel("Impacto")
plt.ylabel("Quantidade de Mutações")
plt.savefig("grafico_mutacoes.png")
print("Gráfico gerado e salvo com sucesso como grafico_mutacoes.png!")

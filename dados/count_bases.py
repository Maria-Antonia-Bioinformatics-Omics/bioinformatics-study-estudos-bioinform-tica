# Lê o arquivo fasta e conta as bases
nome_arquivo = "sequencia.fasta"

total_a = 0
total_t = 0
total_c = 0
total_g = 0

with open(nome_arquivo, "r") as arquivo:
    for linha in arquivo:
        # Pula as linhas de cabeçalho que começam com '>'
        if linha.startswith(">"):
            continue
        
        # Transforma a linha em maiúsculas e remove espaços vazios
        sequencia = linha.strip().upper()
        
        # Conta cada letra na linha
        total_a += sequencia.count("A")
        total_t += sequencia.count("T")
        total_c += sequencia.count("C")
        total_g += sequencia.count("G")

print("--- Resultado da contagem ---")
print(f"Adenina (A): {total_a}")
print(f"Timina (T): {total_t}")
print(f"Citosina (C): {total_c}")
print(f"Guanina (G): {total_g}")
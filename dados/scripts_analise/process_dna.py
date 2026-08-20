from Bio import SeqIO

# Lê o arquivo FASTA real que acabamos de baixar
arquivo_fasta = "gene_real.fasta"

print("--- Processando sequencias reais com BioPython ---")

# Itera sobre cada registro do arquivo FASTA usando o BioPython
for registro in SeqIO.parse(arquivo_fasta, "fasta"):
    print(f"ID: {registro.id}")
    print(f"Tamanho da sequencia: {len(registro.seq)} bases")
    print(f"Primeiros 20 nucleotideos: {registro.seq[:20]}")
    print("-" * 40)
from Bio import Entrez, Align, SeqIO

Entrez.email = "maria.antonia.bioinformatics@gmail.com"

ids = ["J01859.1", "X70346.1"]
sequences = []

print("Fetching and aligning...")
for seq_id in ids:
    handle = Entrez.efetch(db="nucleotide", id=seq_id, rettype="fasta", retmode="text")
    sequences.append(SeqIO.read(handle, "fasta").seq)
    handle.close()

aligner = Align.PairwiseAligner()
aligner.mode = 'local'  # Muda para alinhamento local (acha a melhor região em comum)
alignments = aligner.align(sequences[0], sequences[1])
best_alignment = alignments[0]

# Calculate identity percentage safely
score = best_alignment.score
max_len = max(len(sequences[0]), len(sequences[1]))
approx_identity = (score / max_len) * 100

print(f"\n--- Alignment Report ---")
print(f"Comparison: {ids[0]} vs {ids[1]}")
print(f"Alignment Score: {score}")
print(f"Approx. Identity: {approx_identity:.2f}%")
print(f"------------------------")
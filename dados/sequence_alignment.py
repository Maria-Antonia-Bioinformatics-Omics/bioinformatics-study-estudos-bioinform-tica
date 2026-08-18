from Bio import Entrez, SeqIO
from Bio import Align

Entrez.email = "maria.antonia.bioinformatics@gmail.com"

# IDs of the sequences we want to compare
ids = ["J01859.1", "X70346.1"]
sequences = []

print("Fetching sequences for alignment...")
for seq_id in ids:
    handle = Entrez.efetch(db="nucleotide", id=seq_id, rettype="fasta", retmode="text")
    sequences.append(SeqIO.read(handle, "fasta").seq)
    handle.close()

# Perform global alignment
aligner = Align.PairwiseAligner()
alignments = aligner.align(sequences[0], sequences[1])

print(f"\nAlignment score: {alignments[0].score}")
print("Alignment preview:")
print(alignments[0])
#!/usr/bin/env python

#This script uses python version: 3.6.7, Biopython 1.79

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


spacer = Seq("")

for seq_record in SeqIO.parse("TriTrypDB-61_EmonterogeiiLV88_Genome.fasta", "fasta"):
    if seq_record.id == "EmoLV88_10":
        # print(seq_record.id + "LAP102")
        # print(seq_record.seq[50923:54470])
        gene_dna_seqs = [Seq(seq_record.seq[:52141]), Seq(seq_record.seq[52142:])]
        
        gene_dna = SeqRecord(
            Seq(spacer.join(gene_dna_seqs)),
            id = "updated_EmoLV88_10")

new_seq = SeqRecord(Seq(gene_dna.seq[50923:54469]),
id = "EmontLAP102")

print("\n")
print(new_seq.id)
print(new_seq.seq)

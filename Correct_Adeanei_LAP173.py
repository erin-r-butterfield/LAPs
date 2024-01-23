#!/usr/bin/env python

#This script uses python version: 3.6.7, Biopython 1.79


from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


spacer = Seq("")

for seq_record in SeqIO.parse("TriTrypDB-60_AdeanaiCavalhoATCCPRA-265_Genome.fasta", "fasta"):
    if seq_record.id == "LR877162":
        gene_dna_seqs = [Seq(seq_record.seq[:97187]), Seq("T"), Seq(seq_record.seq[97187:98386]), Seq(seq_record.seq[98388:98642]), Seq("A"), Seq(seq_record.seq[98642:100293]), Seq(seq_record.seq[100294:])]
        
        gene_dna = SeqRecord(
            Seq(spacer.join(gene_dna_seqs)),
            id = "updated_LR877162")

new_seq = SeqRecord(Seq(gene_dna.seq[95899:106000]),
id = "AdLAP173_w_utr")

print("\n")
print(new_seq.id)
print(new_seq.seq)
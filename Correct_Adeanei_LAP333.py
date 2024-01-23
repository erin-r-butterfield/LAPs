#!/usr/bin/env python

#This script uses python version: 3.6.7, Biopython 1.79


from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


spacer = Seq("")

for seq_record in SeqIO.parse("TriTrypDB-60_AdeanaiCavalhoATCCPRA-265_Genome.fasta", "fasta"):
    if seq_record.id == "LR877166":
        gene_dna_seqs = [Seq(seq_record.seq[:368652]), Seq("C"), Seq(seq_record.seq[368652:370227]), Seq("G"), Seq(seq_record.seq[370227:370235]), Seq(seq_record.seq[370236:370238]), Seq(seq_record.seq[370239:370248]), Seq(seq_record.seq[370250:370256]), Seq(seq_record.seq[370258:370304]), Seq(seq_record.seq[370306:370880]),Seq("T"), Seq(seq_record.seq[370880:])]
        
        gene_dna = SeqRecord(
            Seq(spacer.join(gene_dna_seqs)),
            id = "updated_LR877166")

new_seq = SeqRecord(Seq(gene_dna.seq[360000:380000]),
id = "AdLAP333_w_utr")

print("\n")
print(new_seq.id)
print(new_seq.seq)
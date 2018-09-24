#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 00:05:13 2018

@author: MOOSE
"""

from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
with open("cbb_assembled.fasta", "rU") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        print(record.id)

first_record = SeqIO.parse("cbb_assembled.fasta", "fasta").next()

records = list(SeqIO.parse("cbb_assembled.fasta", "fasta"))
print(records[0].id)  # first record
print(records[-1].id

#E value Threshold
eval_threshold = 0.05


for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < eval_threshold:
            print('****Alignment****')
            print('sequence:', alignment.title)
            print('length:', alignment.length)
            print('e value:', hsp.expect)
            print(hsp.query[0:75] + '...')
            print(hsp.match[0:75] + '...')
            print(hsp.sbjct[0:75] + '...')


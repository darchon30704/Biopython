from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqUtils import GC
seqRec1 = SeqIO.read(open('ecogene.fasta'), 'fasta')
print(seqRec1)
print(seqRec1.seq)
print len((seqRec1.seq))
record = SeqIO.read("ecogene.gbk", "genbank")
record.description

for seq_record in SeqIO.parse('ecogene.fasta', 'fasta'):
    print(seq_record.id)
    print(repr(seq_record.seq))

my_seqlist = []

for seq_record in SeqIO.parse('ecogene.fasta', 'fasta'):
	my_seqlist.append(seq_record)
my_seqlist[0]





from Bio import SeqIO
from Bio.SeqUtils import GC

fa = open('cbbtx.fa', 'r')
out = open('cb300.fa', 'w')

bases = 0
seqlist = list(SeqIO.parse(fa, "fasta"))

for temp in seqlist:
	x =  len(temp.seq)
	bases += x
print(bases)

list300=[]
for temp in seqlist:
	if  len(temp) > = 300:
		list300.append(temp)
SeqIO.write(list300, "cb300.fa", "fasta")

GC=[]
 temp in seqlist:
	if  len(temp) > = 300:
		list300.append(temp)
SeqIO.write(list300, "cb300.fa", "fasta")
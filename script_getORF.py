#!/usr/bin/env python3
import sys
import re

#ffile = sys.argv[1]

#Criando um dicionário com o multi fasta, a partir daqui tenho um dicionário onde a head line é a key e a sequência é o valor associado. O dicionário criado com o multifasta foi fastaDict.

infile=sys.argv[1]
fastaDict={}
seqName=''
newData=''
with open(infile,"r") as file_object:
	for line in file_object:
		line = line.rstrip()
		if re.search(r'^>',line):
			seqName=line.split(' ')[0]
			seqName=seqName.replace('>','')
			newData=''
		else:
			newData += line.upper()
			fastaDict[seqName] = newData

for gene in fastaDict:
	seq = fastaDict[gene]
	revseq = seq[::-1]
	c1 = [seq[i:i+3] for i in range(0, len(seq), 3)]
	f1 = ''.join(c1)
	c2 = [seq[i:i+3] for i in range(1, len(seq), 3)]
	f2 = ''.join(c2)
	c3 = [seq[i:i+3] for i in range(2, len(seq), 3)]
	f3 = ''.join(c3)
	c4 = [seq[i:i+3] for i in range(0, len(revseq), 3)]
	f4 = ''.join(c4)
	c5 = [seq[i:i+3] for i in range(1, len(revseq), 3)]
	f5 = ''.join(c5)
	c6 = [seq[i:i+3] for i in range(2, len(revseq), 3)]
	f6 = ''.join(c6)
	found1 = re.findall(r'ATG.*T[AG][GA]', f1)
	found2 = re.findall(r'ATG.*T[AG][GA]', f2)
	found3 = re.findall(r'ATG.*T[AG][GA]', f3)
	found4 = re.findall(r'ATG.*T[AG][GA]', f4)
	found5 = re.findall(r'ATG.*T[AG][GA]', f5)
	found6 = re.findall(r'ATG.*T[AG][GA]', f6)
#	found1 = re.findall(r'ATG.*(TGA|TAA|TAG)', f1)
#	found2 = re.findall(r'ATG.*(TGA|TAA|TAG)', f2)
#	found3 = re.findall(r'ATG.*(TGA|TAA|TAG)', f3)
#	found4 = re.findall(r'ATG.*(TGA|TAA|TAG)', f4)
#	found5 = re.findall(r'ATG.*(TGA|TAA|TAG)', f5)
#	found6 = re.findall(r'ATG.*(TGA|TAA|TAG)', f6)
	print(found1)
	print(found2)
	print(found3)
	print(found4)
	print(found5)
	print(found6)






	
	

#for gene in fastaDict:
#	seq = fastaDict[gene]
#	revseq = seq[::-1]
#	print(revseq)
#
#fastaDict[f'rev{gene}'] = revseq

#print(fastaDict)

#for gene in fastaDict:
#	seq = fastaDict[gene]
#	found = re.findall(r'ATG.*T[AG][GA]', seq)
#	found2 = re.search(r'ATG.*T[AG][GA]', seq)
#	print(found)
#	print(found2)








#	c1 = [seq[i:i+3] for i in range(0, len(seq), 3)]
#	f1 = ''.join(c1)
#	c2 = [seq[i:i+3] for i in range(1, len(seq), 3)]
#	f2 = ''.join(c2)
#	c3 = [seq[i:i+3] for i in range(2, len(seq), 3)]
#	f3 = ''.join(c3)
#	c4 = [seq[i:i+3] for i in range(3, len(seq), 3)]
#	f4 = ''.join(c4)
#	c5 = [seq[i:i+3] for i in range(4, len(seq), 3)]
#	f5 = ''.join(c5)
#	c6 = [seq[i:i+3] for i in range(5, len(seq), 3)]
#	f6 = ''.join(c6)
#	f = [f1, f2, f3, f4, f5, f6]

#for gene in fastaDict:
#	seq_t = [Translate(i) for i in fastaDict[gene]]

#value = 0
#seq_frame = []
#for i in seq_t:
#	frame = f(seq_t[valeu])
#	value += 1
#	seq_frame.append(frame)
#print(seq_frame)


#	found = re.findall(r'ATG.*T[AG][GA]', seq)
#	found2 = re.search(r'ATG.*T[AG][GA]', seq)
#	print(found)
#	print(found2)



#composition={}
#for seqId in fastaDict.keys():
#    if seqId not in composition.keys():
#        composition[seqId]={}
#    for nt in set(fastaDict[seqId]):
#        if nt not in composition[seqId].keys():
#            composition[seqId][nt]=0
#        composition[seqId][nt] = fastaDict[seqId].count(nt)

#for seqId in composition.keys():
#    print(f'{seqId}\t{composition[seqId]["A"]}\t{composition[seqId]["T"]}\t{composition[seqId]["G"]}\t{composition[seqId]["C"]}')

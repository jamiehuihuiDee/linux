
### 用于分割silva原始数据的信息，把它拆分为taxonomy和fasta 
## silva file names is something like SILVA_138_SSURef_Nr99_tax_silva.fasta
## and the tax_silva for seperating labels

##### split by jinhui
from __future__ import print_function
import re,sys,os

tax = open('SILVA_138_SSURef_Nr99_tax.txt', 'w')
seq = open('SILVA_138_SSURef_Nr99_seq.fasta', 'w')

with open('SILVA_138_SSURef_Nr99_tax_silva.fasta') as infile:
    for i in infile:
        if re.match('>',i):
            first = ''.join(i.rstrip().split('>')).split(' ',1)
            second = first[1].rstrip().replace(' ','-')
            zero = i.rstrip().split(' ')
            out_tax = "%s\t%s\n" % (first[0],second)
            out_seq = "%s\n" % (zero[0])
            tax.write(out_tax)
            seq.write(out_seq)
        else:
            dna = i.rstrip().replace("U","T")
            out_seq = "%s\n" %(dna)
            seq.write(out_seq)

# after circle, add one more line apart
tax.close()
seq.close()  


   

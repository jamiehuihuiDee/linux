#### for double strains, make manifest and metadata as well,python3
#### usage: python /home/jhtang/mytest/code/process_16S/manifest_paired.py -s .R -m _S -d current 
from __future__ import print_function
import glob,os,re,argparse


def manifest_make(seperator,metaSeperator):
    Counter=0
    for i in file_names:
        if re.search(seperator+'1',i):
            istrip = i.rstrip().split(seperator)
            i_name = istrip[0]
            i_meta_name = i.rstrip().split(metaSeperator)[0]
            i_len = len(i_name)
            suffix = istrip[1][1:]
            forward_name = i_name + seperator + '1'+ suffix
            reverse_name = i_name + seperator +'2'+ suffix
            #put in the \n			
            #Counter+=1
            ID = "sample%s" % (i_meta_name)
            out_str = "%s\t%s/%s\t%s/%s\n"  % (ID,cwd,forward_name,cwd,reverse_name)
            out_str_meta="%s\t%s\n" % (ID,i_meta_name)

            manifest.write(out_str)
            metadata.write(out_str_meta)

    manifest.close()
    metadata.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--seperator', dest='seperator', type=str, required=False,default='.R',
                        help="the seperator for seperate the file name,default is .R for L.326.R1.fq.gz")
    parser.add_argument('-m', '--metaSeperator', dest='metaSeperator', type=str, required=False,default='.fastq.gz',
                        help="the seperator for seperate the file name,default is .fastq.gz for A75.fastq.gz")
    parser.add_argument('-d', '--data', dest='data', type=str, required=False,default='current',
                        help="the path of the data folder")
    args = parser.parse_args()
    print('Usage example with parameters: python /home/jhtang/mytest/code/process_16S/manifest_paired.py -s _R -m _S -d /home/jhtang ,\
     for  sample full name like 10_S10_L001_R2_001.fastq.gz')
    seperator = args.seperator
    metaSeperator = args.metaSeperator
    data = args.data


    
    manifest = open('manifest.txt', 'w')
    metadata = open('metadata.txt','w')

    manifest.write('#SampleID\tforward-absolute-filepath\treverse-absolute-filepath\n')
    metadata.write('#SampleID\tFileName\n')
    cwd = os.getcwd()
    file_names = os.listdir()
    if data=='current':
        file_names = os.listdir()
    else:
        file_names = os.listdir(data)
        cwd=data
    manifest_make(seperator,metaSeperator)

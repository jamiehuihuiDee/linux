
## 一般流程
- HISAT2 + StringTie + ballgown (assembly)
- HISAT2 + htseq/featureCounts（更快）+DESeq2 （推荐）
- STAR + htseq/featureCounts（更快）+DESeq2 （已有文献较多）

## HISAT2
- http://ccb.jhu.edu/software/hisat2/manual.shtml#building-from-source 下载安装包，解压zip文件，并在添加路径到.bashrc
- 索引构建,需要下载gtf文件(见gtf下载)
- 从参考文件gtf提取外显子或者片段
```
extract_exons.py /home/jhtang/miniconda3/bin/stringtie/reference/Mus_musculus.GRCm38.99.gtf  >Mus_GRCm38_99.exon

extract_splice_sites.py /home/jhtang/miniconda3/bin/stringtie/reference/Mus_musculus.GRCm38.99.gtf >Mus_GRCm38_99.ss
```
- 根据gtf提取信息建立fasta索引库，ss输入splice文件，exon对应外显子，接着是参考fasta文件（多个fasta用逗号隔开），最后为生成文件名
```
hisat2-build --ss Mus_GRCm38_99.ss --exon Mus_GRCm38_99.exon mm10.fa Mus_GRCm38_99_tran
```
- hisat2 官网索引，hisat2 官网建立好的索引https://daehwankimlab.github.io/hisat2/download/ （建议根据自己需要重新建立）
- hisat2 运行
```
# -x 输入索引文件，代表reference， -1，-2 分别输入双端序列，如果只有一个sample直接用-U  -s是输出文件
hisat2 -p 8 --dta -x chrX_data/indexes/chrX_tran -1 chrX_data/samples/ERR188044_chrX_1.fastq.gz -2 chrX_data/samples/ERR188044_chrX_2.fastq.gz 
-S ERR188044_chrX.sam 

hisat2 -p 8 --dta -x chrX_data/indexes/chrX_tran --sra-acc SRR3137739 –S ERR188245_chrX.sam  
```

## STAR 
- 安装 https://github.com/alexdobin/STAR
- https://chagall.med.cornell.edu/RNASEQcourse/STARmanual.pdf

```
tar -xzf 2.7.4a.tar.gz
cd STAR-2.7.4a
cd source
make STAR
export path=
```
- 建索引
```
## Dir是索引保存位置,使用gtf文件，以及对应fasta
/home/jhtang/miniconda3/bin/STAR-2.5.3a/bin/Linux_x86_64/STAR --runThreadN 4 \
--runMode genomeGenerate \ 
--genomeDir /home/jhtang/miniconda3/bin/STAR-2.5.3a/reference  \
--sjdbGTFfile /home/jhtang/miniconda3/bin/stringtie/reference/ncbi/mrna/GCF_000001635.26_GRCm38.p6_genomic.gtf \
--genomeFastaFiles /home/jhtang/miniconda3/bin/stringtie/reference/ncbi/mrna/GCF_000001635.26_GRCm38.p6_genomic_rna.fna

## 比对prefix名字前缀,limitGenomeGenerateRAM 要给大点，如果基因组太大的话，默认的有点小
### 如果是 压缩文件，就用filesconmmand
###--quantMode GeneCounts  可以直接用STAR统计reads数量
/home/jhtang/miniconda3/bin/STAR-2.5.3a/bin/Linux_x86_64/STAR \
 --genomeDir /home/jhtang/miniconda3/bin/STAR-2.5.3a/reference  \
--readFilesIn file_R1.fq file_R2.fq  \
--runThreadN 6  \
--limitGenomeGenerateRAM  160263683456  \
--outFileNamePrefix  sample_name_prefix \
--readFilesCommand zcat 
```

## samtools
- 安装 conda install -c bioconda samtools
samtools （1.3版本以上比较好，可以直接把sam转换为bam，在stringtie里面也有安装，版本比较低）
- 目录下install
```
cd samtools-1.x    
./configure --prefix= /home/jhtang/path
make
make install
export PATH="/home/jhtang/miniconda3/bin/samtools-1.10:$PATH"
```
- samtools序列重新排列
```
# Sort and convert the SAM files to BAM:  （双端需要把它们排序，单端最好也排序）
# -@ 运算核，-o 输出文件
samtools sort -@ 8 -o ERR188044_chrX.bam ERR188044_chrX.sam 
```

## Stringtie
- http://ccb.jhu.edu/software/stringtie/ 下载安装包，解压gzip文件，并在添加路径到.bashrc
```
tar xvfz ~/Downloads/stringtie-VER.tar.gz
cd stringtie-VER
make release
export PATH="/home/jhtang/miniconda3/bin/stringtie:$PATH" 
```
- stringtie 拼接比对
```
# p运算核，G 参考文件 , l是设置label,标记输出文件前缀,o 生成文件
stringtie ERR188044_chrX.bam -p 8 -G chrX_data/genes/chrX.gtf -l ERR188044 -o ERR188044_chrX.gtf  

# Merge transcripts from all samples，txt包含merge各个sample顺序的信息，重新merge调整标记id号，确保所有sample一致
stringtie --merge -p 8 -G chrX_data/genes/chrX.gtf -o stringtie_merged.gtf chrX_data/mergelist.txt  

# do the transcript merge again by using a new merge list
stringtie --merge -p 8 -G chrX_data/genes/chrX.gtf -o stringtie_merged.gtf chrX_data/mergelist1.txt

# Estimate transcript abundances and create table counts for Ballgown: 重新预测，各sample整合对应gtf比较完善
stringtie ERR188044_chrX.bam -p 8 -G stringtie_merged.gtf -o ballgown/ERR188044/ERR188044_chrX.gtf -e -B
```

## gtf文件与对应fasta文件下载
- gtf文件在ensembl与ncbi，genecode稍有不同，主要在Rik 标注的基因名上。
```
EMSEMBL
ftp://ftp.ensembl.org/pub/release-99/fasta/mus_musculus/dna_index/
ftp://ftp.ensembl.org/pub/release-99/gtf/mus_musculus/Mus_musculus.GRCm38.99.gtf.gz  下载小鼠参考库

NCBI
ftp://ftp.ncbi.nlm.nih.gov/genomes/Mus_musculus/GFF/                    下面是GFF文件，也有gtf文件，最好用gtf文件
ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/635/GCF_000001635.26_GRCm38.p6/GCF_000001635.26_GRCm38.p6_genomic.gff.gz

GENCODE   gencodegenes.org/mouse/   尽量用gencode，有对应的fasta与annotation，annotation选择推荐版本就好

https://hgdownload.soe.ucsc.edu/goldenPath/mm10/bigZips/ 



## raw reads统计，可以用sam或者bam，最好还是samtools排序处理一下
## htseq
-安装 conda install htseq
- https://pypi.org/project/HTSeq/0.9.1/
-htseq 统计运行，输出结果是sam文件加上标注
```
## 用于sam文件,输入gtf文件（参考文件要跟hisat2或者STAR使用一样的gtf文件），-o 输出文件，-s 序列方向，-i 统计基因名gene_name，如果比对有问题可以调整方向在gff文件可能是gene,需要查看gff文件对应在哪个位置
htseq-count  C_Ce2.sam \
 /home/jhtang/miniconda3/bin/stringtie/reference/ncbi/GCF_000001635.26_GRCm38.p6_genomic.gtf \
-s reverse -o C_Ce2_count.sam -i gene_name 

## 用于bam文件，运行更慢，建议还是用sam格式，
htseq-count  C_Ce2.bam  -f bam\
 /home/jhtang/miniconda3/bin/stringtie/reference/ncbi/GCF_000001635.26_GRCm38.p6_genomic.gtf \
-s reverse -o C_Ce2_count.sam -i gene_name 
```

## featureCounts
- 在subread安装包里面， https://sourceforge.net/projects/subread/
- 解压了就可以，不需要make
- featureCounts 统计
```
+ -p 统计 fragment双端，-T 运算核，-t统计按照exon类别的reads数量，
-g指定从gtf文件中挑选的注释信息gene_id，ensembl的gtf用gene_name，ncbi的gff或者gtf用gene，ncib的gtf也可以用gene_id,可以看相应文件是否存在gene_name
-a 参考文件要跟hisat2或者STAR使用一样的gtf文件
-M 是计算multimapped，默认不计算，-o 输出文件

featureCounts -p -T 4   -t exon -g gene_name -a /home/jhtang/miniconda3/bin/stringtie/reference/hisat2_grcm38_snp_tran/Mus_musculus.GRCm38.99.gtf \
 -o C_Str1_count.txt C_Str1.sam
```

## cufflinks 安装  
- http://cole-trapnell-lab.github.io/cufflinks/install/
- 可以转换gff和gtf文件，但是最好用官网的gtf文件
```
/home/jhtang/miniconda3/bin/cufflinks-2.2.1.Linux_x86_64/gffread test.gff -T -o test.gtf
```


## 差异基因分析
## ballgown
```
BiocManager::install(c("Rsamtools","DESeq2",
"GenomicFeatures","pheatmap","GenomicAlignments","BiocParallel"))
```

## DESeq2

#6-1、 根据参考库生成一个新的qza数据集 ，参考文库建立
 ```
 https://www.arb-silva.de/download/archive/
 https://www.arb-silva.de/no_cache/download/archive/current/Exports/
 ```
 
 #silva 参考库
#######fasta只有序号和序列,一定要解压gz  gzip -d **.gz   Nr100的制作，导入fasta格式

qiime tools import \
  --type 'FeatureData[Sequence]' \
  --input-path SILVA_132_SSURef_seq.fasta \   ## change the name and the output
  --output-path SILVA_132_SSURef_seq.qza 

##########3taxonomy需要有一个标头，即列名。包含序号以及对应的taxonomy  Nr100的制作   
##只能有两列，tab隔开，不然报错，taxonomy名字也不能有多余空格

### 导入数据，taxonomy 与 fasta分别导入
qiime tools import \
  --type 'FeatureData[Taxonomy]' \
  --input-format HeaderlessTSVTaxonomyFormat \ 
  --input-path SILVA_132_SSURef_tax.txt \     ## change the name and the output
  --output-path ref-taxonomy_all.qza 
  
  qiime tools import \
  --input-path sequences.fna \
  --output-path sequences.qza \
  --type 'FeatureData[Sequence]'
  
  #### classifier 训练
  
  qiime feature-classifier extract-reads \
  --i-sequences SILVA_138_SSURef_Nr99_seq.qza \
  --p-f-primer GTGCCAGCMGCCGCGGTAA \
  --p-r-primer GGACTACHVGGGTWTCTAAT \  # 改为自己的primer，最大长度一般比该区域稍微大一点，V4区对应100-400，V3-V4 大概选了100-500
  --p-trunc-len 253 \
  --p-min-length 100 \
  --p-max-length 400 \
  --o-reads ref-seqs_Nr99_515_806.qza   ## classifier的名字自己改好，最好史用引物命名，前面的Nr就是数据库是否有99%相似合并，100%的太多

##train the classifier
qiime feature-classifier fit-classifier-naive-bayes \
  --i-reference-reads ref-seqs_Nr99_515_806.qza \
  --i-reference-taxonomy ref-taxonomy_Nr99.qza \
  --o-classifier classifier_taxonomy_slv_138_Nr99_515_806.qza  
  

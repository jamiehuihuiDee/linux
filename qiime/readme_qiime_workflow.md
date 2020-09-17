## run python to make a manifest.txt file
```
python /home/jhtang/mytest/code/process_16S/manifest_paired.py -s .R -m .R \
-d /home/LDlab/wangying/DXX/fourth_batch_16S_20200527/fourth_batch_2
```

## run classifier make to make a classifer with the primer used for sequencing
### download database from silva and run the file reshaping script
```
python test.py -i SILVA_138_SSURef_Nr99_tax_silva.fasta

```

### Then make a classifier
运行classifier_make 文件的脚本，修改信息，再打包运行bash


## 文件名字对应好了就可以直接运行
bash run_qiime.sh



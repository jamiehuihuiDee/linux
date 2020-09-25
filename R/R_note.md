### linux系统 
- 进入某一个版本的R，conda activate R*,  package install **
#### R脚本的运行
```
- R脚本内参数传递 
args <- commandArgs(TRUE)
sample_name <- args[[1]]
- R running
R CMD BATCH --args file.R
Rscript file.R input1 input2  ## Rscript 具体路径，input参数按顺序空格隔开
```
#### R 包安装
```
- 最简单直接安装
1、 install.packages("devtools", dependencies = T) # 安装依赖包
2、 conda安装R包，激活R环境载安装，最好不要更新包
conda install r-stringr
conda uninstall r-stringr
3、 生信相关包
通过BiocManager，BiocManager::install("***")
4、 github下载
devtools::install_github("thomasp85/patchwork")
install_github(repo="rBiopaxParser", username="frankkramer")
5、其它
install.packages("installr")
installr::install.ImageMagick("http://www.imagemagick.org/script/download.php")

- 安装报错可能

1、某些包需要更新，如cli包，本地电脑需要remove.packages，再重新安装。
2、缺乏C++等，conda install gxx_linux-64 等
x86_64-conda_cos6-linux-gnu-c++
x86_64-conda_cos6-linux-gnu-gfortran
conda install x86_64-conda_cos6-linux-gnu-cc
3、某些包只能在某些版本安装，如stringr只能在r-base 3.6.1安装

- 运行包报错可能
1、某些包内置函数名字一样，有冲突，最好使用R包名加函数 phyloseq::distance， 尽量不要加载太多包
2、程序包内的例子不能运行，卸载包重新安装
3、更新S4Vector, 某些报不能导入自己定义的class
4、某个包如果不能运行object，可能是因为其它包更新，直接把相关的包都更新一遍 
BiocManager::install("ballgown", update = TRUE, ask = FALSE)

- R包信息
man文件用来生成R执行的Rd文件
src文件 里面有基于C++的函数，再R中不可见


```
#### R 包学习使用
```
根据manual pdf查看
可以直接看源代码，再报下载地址可以找到
https://cran.r-project.org/web/packages/stringr/index.html  -> package source
1、 加载与卸载
library（**）
detach(package:ggtern,unload = TRUE)
2、版本
packageVersion()
3、帮助信息
- 普通函数
？classifify
page() 查看源代码
- 泛函数（函数运行的具体代码不显示）
showMethods("upsetplot") ，获取多种数据类型的展示方法，再通过下面一步找到某一种数据类型的函数使用方法
ChIPseeker:::upsetplot.csAnno

```

#### R 包路径
```
- 查看路径 
.libPaths() #一般包含该包的文件在~/lib/R/etc/Renviron，多个路径默认使用第一个 R_LIBS_SITE
参考路径 /home/jhtang/miniconda3/envs/R/lib/R/library

```
#### 环境清空
```
 rm(list = ls(all. names = TRUE))
```




#### 注意事项
- 字符格式，中英文逗号要分清


###错误检查
```
1、函数是否改变了（建议每一次作图单独保存一个运行脚本，一个函数脚本，避免修改了函数导致前面的脚本不能运行，并且尽量把运行的图用pdf保存下来）
2、数据类型检查，dataframe选择一列容易变成vector，需要特别注意
3、NA值，某些运算可能出现NA值，可能是factor设置了，也可嗯那个是别的原因。
4、merge前受否存在重复行，会导致多次重复合并
5、变量名字最好不要跟函数一样

```

### 数据读取
```
- 文件目录内容读取
1、 xlsx
rawdata <- read_xlsx("explore.xlsx",col_names = TRUE,sheet = 1)
2、 csv
read.csv("metadata_all.csv",header = T,row.names=1,na.strings = "",fill = TRUE,stringsAsFactors = FALSE) # na.strings处理空白值，它们不是NA
3、 other
read.table("R_data mining.data", header=F, sep=" ",fill = TRUE) # fill 列数不一样自动补全
如果文件数据包含#号，默认是注释不读取，可以取消。
read.table("test.txt",sep = "\t",comment.char = "",quote = "")

-- 数据读取最好采用csv格式

- 当前路径下目录读取
list.files(pattern=".csv")


```

### 数据类型转换
```
- list
1、 转为data.frame
-- data.frame(matrix(unlist(gene_length2),nrow = length(gene_length2),byrow = TRUE))
-- h <- sapply(filt_seq, strsplit,split="")
h_all <- do.call(rbind,h)


```

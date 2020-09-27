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

### 数据类型与转换
```
- list （在数据使用过程中，最好把常用的数据打包成list，防止重复删改）
1、 list操作
-- length 读取长度
-- list 字符分割
+ hh <-t(as.data.frame(str_split(tax0[1:nrow(tax0),col],"_",n=4)))[,4] %>% as.data.frame() #需要转置并且在n设置固定返回值，防止NA值
+  str_split(h[i,"KEGG.GENES"]," ",n=10,simplify = TRUE) #simplify 返回vector， 或者list

-- list数据选择
+ purrr::map(list,1),选择每个list 的第一个值
+ 提取长度大于1，去除null
h@ends[lapply(h@ends,length )>0]

-- list转为data.frame
+ data.frame(matrix(unlist(gene_length2),nrow = length(gene_length2),byrow = TRUE))
+ h <- sapply(filt_seq, strsplit,split="")
h_all <- do.call(rbind,h)

-- dataframe 转为list
+ 短的行最后用长的行填充 
o <- t(tax0)%>% as.data.frame()
h <- split(o,rownames(o))
+ 组装两个dataframe成为list
 c <- list(frame1,frame2) # 用于函数输出结果
+ as.list

-- 命名
+ list本身没有名字，即便是1，2，3，需要自己重新命名为数字
names(ends_data)  <- seq(1,length(ends_data))


```
```
- factor
-- dataframe factor 全部转为character
data.frame(as.matrix(unique_pos),stringsAsFactors = FALSE)
+ 字符串修改，需要改为character才能操作字符串分割或者重新赋值
+ 判断的时候也需要转化为字符串
-- factor转数值
as.numeric(as.matrix())
factor直接转化为numeric只会根据level进行1到100的标记，先转为matrix再转为numeric
-- 再次factor重新定义水平
factor(.,levels=c("B","A","C"),labels = c("1","2","3"))
+ 多个数值对应一个level，直接再labels改为同名
factor(as.numeric(as.matrix(meta$Day)),levels=c(0,8,10,31),labels = c(0,8,8,31))

-- 其它
+ summary，只能统计数值或者factor，字符串无用， summary默认统计100个不同水平
```
```
- dataframe

-- 创建
+ data.frame(stringsAsFactors = FALSE) #取消factor自动转化
+  规定行数
a <- matrix("0",nrow=1,seq_max) %>% as.data.frame() #

-- 行名问题
+ 行名不能以中括号[开头，否则自动处理为X. ，减号也自动处理为点. ，但是输出显示行名还是正常，如果要选择数据就会出错。
+ 相同名字的行名自动在末尾添加点以及序号.1，但输出行名也会把后缀去掉与matrix不同，matrix行名都是一样，只是为了标明区别才加上后缀的
+ 最好把行名设定在一个新列,否则降维的时候容易丢失行名

-- 列名问题
+ 可以有重复名，但提取的时候只会选取第一个，其余重复的值不会被提取

-- 数据选择与合并问题
+ matrix只有一列可以直接用a[1:10]查找，但只有一列的dataframe一定要指定列名
+ cbind: 如果想要将数字数据框与字符串加在一起，数值型的放在开头，否则全都显示为NA，当然可以先将数值型数据转化为字符串


```

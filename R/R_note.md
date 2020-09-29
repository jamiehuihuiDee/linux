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

#### 文件路径与文件名操作
```
- 文件路径
list.files
- 文件名操作
basename 提取路径最后的文件夹名字
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
+ 取消factor自动转化
data.frame(stringsAsFactors = FALSE) 
+  规定行数，通过matrix转化
a <- matrix("0",nrow=1,seq_max) %>% as.data.frame() 
+ 逐个变量设定
data.frame(name=,,,.value=....）
+ 列名获取
data[0,]

-- 行名问题
+ 行名不能以中括号[开头，否则自动处理为X. ，减号也自动处理为点. ，但是输出显示行名还是正常，如果要选择数据就会出错。
+ 相同名字的行名自动在末尾添加点以及序号.1，但输出行名也会把后缀去掉与matrix不同，matrix行名都是一样，只是为了标明区别才加上后缀的
+ 最好把行名设定在一个新列,否则降维的时候容易丢失行名

-- 列名问题
+ 可以有重复名，但提取的时候只会选取第一个，其余重复的值不会被提取

-- 数据选择与合并问题
+ matrix只有一列可以直接用a[1:10]查找，但只有一列的dataframe一定要指定列名
+ cbind: 如果想要将数字数据框与字符串加在一起，数值型的放在开头，否则全都显示为NA，当然可以先将数值型数据转化为字符串
+ 数据选择最好选择两列，选一列辉自动变成array
+ 数据添加新行
df["asdfa",]=0 # 但是matrix不可以

```
```
- matrix
-- 行列名
+ 列名可以重复，不会自动检测出来，通过getUniques查出重名。

-- 数据类型转换
+ 字符串转为数值型 
apply(observed2, 2, as.numeric) %>% as.data.frame
+ dist距离矩阵可以转化为matrix，下三角或上三角缺失部分自动补充完整，才可以添加行列名

-- 特殊使用
+ 检查整个矩阵每一个元素是否满足条件并重新赋值
data[data>0]=1
+ 名字加数值的类型
names（data） 读取行名



```
### 函数
```
- 函数输入
-- 已有函数
+ 对于函数中输入的是变量名而不能是格式化变量，需要使用间接输入方式
 pca_data1 <- subset(pca_data, donor2acceptor %in% var1_sub) ## 直接使用dataframe 中的变量名
 pca_data1 <- subset(pca_data, pca_data[,var1] %in% var1_sub) # 通过中括号选择格式化名字
 
 - 函数中使用函数，一般apply类型较多
 blank[-which(apply(blank, 1, function(x) all(is.na(x)))),]

- 自写函数
-- 参数名字尽量不要有下划线， 选择项参数用大括号代替
plot_pcoa = function(data, meta, column, metric, trefile={},treatmentTime)
-- 参数顺序，必填项，选择默认项，前后关联的参数放在一起
distance_minus=function(Data=dis_melt,mouse_id,var1,var1_sub,var2_sub,value="value")

-- 输出用return
+ 输出多个，可以放在list
  h <- list(data_ord,pcoa,Distance)
  return(h)
-- 函数问题
+ 更新函数有时候需要把函数卸载删除再重新loading

-- 循环问题
+ 循环开头
for (i in 1:(i+5))冒号后面也要加括号
+ 循环体
for(){}
else if (){}
 else{} 
 
+ 简单循环
otu1<- ifelse(otu1>1/10000,1,0)
+ 逻辑判断
isTRUE(average)
is.na(str_match(meta$label[i],"FMT"))==FALSE
is.na(str_match(tax0[i,j],"[uU]n"))==FALSE

+ 循环跳出
++ 跳出一层循环 break
++ 跳过某个循环值 next   
if(class(dis1)=="numeric")
     next
     
     
+ 循环检查
++ 小循环到大循环
++ 数据代入查看
++ 数据选择有空值，没有选上
++ 函数参数名字改了但循环内没修改
—++ 循环体的 if else 是否对齐了
```

## 数据处理
```
- 行重复
h[rep(1,2),] # 重复第一行两次

- NA 处理
-- 数值型na 
is.na() #检查
-- 字符型NA
h[i,j]=="NA" 检查
-- na行清除
blank[-which(apply(blank, 1, function(x) all(is.na(x)))),] 
meta1 <- meta[which(!is.na(str_match(substr(meta$Title,2,2),"1"))),]

- apply 类型函数
-- sapply
+ 对数据列，变量执行[操作（相当于分离，对list的分离），并选择第二部分
sapply(str_split(colnames(otu[i]),'_'),'[',2)
+ sapply执行函数多个变量用c包含
sapply(data,function,metric)

-- tapply
+ 根据向量计算不同水平的统计值
tapply(sscore,sclass,mean) 
+ 不同列复制不同次数
data.frame(lapply(blank,rep,times=c(seqs_count)))

-- apply
+ apply，函数部分多个参数用逗号隔开
counts0_mad <- data.frame(id=rownames(counts0),mad_value=apply(counts0, 1, mad,constant=1, low=TRUE))


- 数据框重整
-- as.matrix
+ 数据框重整为一列
 part1_data <- as.matrix(data[,part1]) %>% matrix(.,ncol=1)

-- melt
+ 对于otu里面的数据，根据id以及treatment进行合并，把前面的变量合并成一个变量，确保前面变量数据为数值，并且属性一致，比如都是细菌变量，后面变量将会单独列出，并且根根前面数据扩增，melt后factor发生改变，需要重新factor
melt(otu_df_rel,id.vars = c( "id",'treatment_time'))

--dcast
+ 左边x是unique，否则需要指定是否要mean，如果是时间有多行，可以选择在事件后增加后缀，右边y，value用于填充,默认自动猜测填充value所在列，可以自己设定value所在列
dcast(data = observed_data1[,c("treatment_time","value","label_id")], treatment_time ~ label_id)
dcast(asv[,c(1,4,5)],id ~ batch,value.var = "zero")

-- merge
+ 注意事项
如果是factor不能merge，一定要把它改为非factor，部分情况可以
小心重复的行

+ 根据行名合并
pcoaPoint <- merge(pcoa_point,meta1,by = "row.names")
+ 两个数据框用不同的列名合并
annotation_col1 <- merge(annotation_col,h,by.x = "row.names",by.y = "Rowname")
+ 多个数据框合并，生成一个list再处理
ls_df <- list(data.frame(a = 1:10, b = 1:10),
              data.frame(a = 5:14, c = 11:20),
              data.frame(a = sample(20, 10), d = runif(10)))
merge(ls_df, by = "a", all = TRUE)

-- full_join (数据库类型的连接)
+ 不设置by自动把名字相同的列合并
full_join(tax_melt1[tax_melt1$variable=="P_Firmicutes",
                              c("sampleId","donor2acceptor","label_id","timeFMT","value")],
                tax_melt1[tax_melt1$variable=="P_Bacteroidota",
                          c("sampleId","donor2acceptor","label_id","timeFMT","value")],
                by=c("sampleId","donor2acceptor","label_id","timeFMT"))

-- anti_join (一个数据框中减去某一部分)
 anti_join(dis_melt,dis1)

- 名字修改
-- 列名修改
names(df)[names(df) == 'old.var.name'] <- 'new.var.name' # 具体到某一个名字
colnames(norm)[grep("taxonomy",colnames(norm))] <- tax_Name  # 选择某一列名对应的列序号

- 日期
-- 选择某一个日可以比较大小
summary(week_clo[week_clo$date < '2018-02-01' & week_clo$weekday == '星期四' ,])

- 符合条件的列
-- subset
+ 按照行名选择
h <- subset(rawdata,select = c(1:10))
h <- subset(rawdata,select = c(1:length(rawdata)))
h <- subset(rawdata,select = c(seq(from=10, to = 50, by = 10))
subset(tx,cpgOverlaps >10 )
+ 直接选择某些值
h<- subset(rawdata,select = c("RA","RPR"))
subset(cpg,seqnames %in% c("chr1","chr2"))
+ 去除某些列
top15_newFrame <- subset(newFrame[1:15,],select= -all)  
+ factor设置再删除空值
h <- factor(tax_melt$variable,levels = c(rownames(top_all),"other"),labels = c(rownames(top_all),"other"))
h[is.na(h)] <- "other"
levels(h)

-- 选择数据尽量不选择NA，可以修改为0或者其它


-集合处理
-- 交集 intersect
-- 并集 union
-- 选择交集不重叠部分 ,找出x不同于y
setdiff(x,y)


- 数据运算
-- sweep
+ 对行进行sum并且行的每个数除以sum，注意分母为零，1是行
sweep(otu_df_all,1,rowSums(otu_df_all),'/')
-- aggregate
+ 按照某列对行操作，一般用于多行数据或同一行之内相加第一个为要相加的数值，第二个是分组
otu_tax3 <- aggregate(.~taxonomy,data = otu_tax2,sum) # 公式右边表示按照的某列
-- group_by (类似于mysql)
+ 作为后续运算的基准，没有改变数据框格式，统计使用summarise进行操作
by_cyl <- mtcars %>% group_by(cyl)
%>% summarise(
  disp = mean(disp),
  hp = mean(hp)
)

-- 行统计
+ rowSums
+ rowsum 按照某列对行操作，一般用于多行数据或同一行之内相加第一个为要相加的数值，第二个是分组，数值变量才能放在第一个位置，一般根据行水平对同一列内的不同行进行加和
rowsum(hCount$C_Ce2,group = hCount$gene_id)

+ rowMean
+ rowsum

-- 数值统计
+ tabulate
 tabulate(as.matrix(read_qual))
+ summary 统计不同factor或者数值的个数并且返回相应的名字，默认只统计100中，
 summary(as.factor(otu_1$sample1784>0)，maxsum=Inf)
+ mean均值
mean(c(A,B,B))
+ sd 方差，自由度减去1

-- 排序 
+ sort 按照排序重新排列dataframe
rawdata[sort(rawdata$LCS,decreasing = TRUE,index.return = TRUE)$ix,]  # ix是排序位置信息
+ order
idx<- order(rowMeans(norm), decreasing = T)
norm = norm[idx,]
+ arrange
results_transcripts = arrange(results_transcripts,pval)，根据pval由小到大


-- S4 数据显示
structure(bg)$trans
+ 一般使用@获取信息
+ 获取名字
names(h@var1) 
+ 某些信息只能通过S4的函数才能调用，像fasta，需要把它调用出来再转换
seqs<-  ShortRead::readFasta("rep_seqs.fasta")
reads <- sread(seqs) 
 id(seqs)
 h <- data.frame(id=id(seqs),reads=sread(seqs))

## 正则表达式字符串
```
可以用于某些行的选择
- 匹配
+ 字母匹配
++ [:alpha:]
++ [A-Z]

+ *代表中括号内出现零次或多次，可以匹配Dag8，Dag8opt
str_match(colnames(newFrame),"Dag8[opt]*")

+ 多次匹配，+号
str_extract(rownames(meta),"[0-9]+")

+   .表示除空格的所有字符，选择整个字符
str_match(colnames(newFrame),".*Dag8[opt]*")

+ 匹配选行，用竖杆作为或选择，或者中括号加逗号
res2[which(is.na(str_match(res2$id,".*Rik|Gm.*|.*-ps.*"))==TRUE),]
str_match(colnames(trans_all),"C_[Hip,Str].*") # 两个字符串之间选择一个，[abc,cdf]，中括号代表中间的任何一个符合要求都可以

+ 小括号包含需要完整匹配的字符串
str_split(colnames(pathway1),"(\\.R1)?_")

+ 选择第几个到几个字母
substr((meta$treatment[1]),1,1)

+ "^>"表示开头是>的字符串，如果放在[]里面，表示开头不是>的字符串
grep(pattern="^>[A-Z]",x=FF,value=TRUE)   # value输出值
+ $ 匹配末尾 
+ 匹配特殊符号，反斜杠
grep('\\[',h3$V2)


- 分割
+ 确保分割后有四个
str_split(tax0[1:nrow(tax0),col],"_",n=4，simplify=TRUE)

+ "[" 分离，特殊符号
sapply(str_split(colnames(otu[i]),'_'),'[',2)

+ 切割后多部份组合
paste(paste(strsplit(x, " ")[[1]][1:min(length(strsplit(x," ")[[1]]), n_word)],
                           collapse=" "), "...", sep="")
                           
+ 分割单词为字母
 strsplit(filt_seq,""）

+ paste 拼接字符
++ 公式的制作可以用collapse，用于array里面的合并，sep用于array之间的合并
 paste("y ~ ",paste(selected,collapse="+"),"+", unselected[i], sep="")) ,# selected里面字符通过collapse设定分离的符号，用于公式输入


+ 换行操作
cat("asdb\nsadf ")


```

### 数据保存
```
- list类型数据保存为.RData
save(trainingSet,file="traingingSet.RData")


```























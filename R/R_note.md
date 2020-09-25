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
- install.packages("devtools", dependencies = T) # 安装依赖包
- conda安装R包，激活R环境载安装，最好不要更新包
conda install r-stringr
conda uninstall r-stringr
- 报错可能

1、某些包需要更新，如cli包，本地电脑需要remove.packages，再重新安装。
2、缺乏C++等，conda install gxx_linux-64 等
x86_64-conda_cos6-linux-gnu-c++
x86_64-conda_cos6-linux-gnu-gfortran
conda install x86_64-conda_cos6-linux-gnu-cc
3、某些包只能在某些版本安装，如stringr只能在r-base 3.6.1安装

```
#### R 包路径
```
- 查看路径
.libPaths() #一般包含该包的文件在~/lib/R/etc/Renviron，多个路径默认使用第一个 R_LIBS_SITE

 
- 报错可能

1、某些包需要更新，如cli包，本地电脑需要remove.packages，再重新安装。
2、缺乏C++等，conda install gxx_linux-64 等
x86_64-conda_cos6-linux-gnu-c++
x86_64-conda_cos6-linux-gnu-gfortran
conda install x86_64-conda_cos6-linux-gnu-cc
3、某些包只能在某些版本安装，如stringr只能在r-base 3.6.1安装

```





#### 注意事项
- 字符格式，中英文逗号要分清

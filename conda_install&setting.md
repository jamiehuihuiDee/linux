# conda installation
minconda3 安装
https://docs.conda.io/en/latest/miniconda.html
bash Miniconda3-latest-Linux-x86_64.sh
+ conda update conda ## to updata conda 

## some setting of the conda
+ change the channels , remove "the default"  line
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
+ some connections take a long time, you might wish to prolong the waiting time
conda config --set remote_connect_timeout_secs 40
conda config --set remote_read_timeout_secs 100
+ see what have changed in the settings
cat ~/.condarc



- it's better to install software under different environment of conda. And conda could install the dependencies. Sometimes the website is in poor connection which may interupt the installation

# conda new environment
conda create -n picrust2 -c bioconda -c conda-forge picrust2=2.2.0_b
+ -c refers to channel
+ picrust2=2.2.0_b, software could be specified a version
+ if want to install more software in the same environment, source activate the envs, and conda install everything you like 
+ conda list    to get the information of the installed envs

## some path of the software 
+ every environment could be found in the path ./minconda3/envs/
+ some data would be held in the path ./minconda3/pkgs

# remove the conda envs
+ conda remove -n picrust2 --all





### 跨服务器传递数据 
+ scp <source> <destination>
  
To copy a file from B to A while logged into B:

```shell
scp /path/to/file username@a:/path/to/destination
```


To copy a directory:

```shell
scp -r username@example.com:/remote/path/to/directory  /local/path
scp -r /local/directory/path username@example:/remote/directory/path
```

---
###
+ rename , last for filenames, fist part is the primary position needed  to be replace, second part is the replacing content
```
rename 's/\_1.fq.gz/_R1.fq.gz/' *_1.fq.gz
rename 's/\_2.fq.gz/_R2.fq.gz/' *_2.fq.gz
```
+ 将当前路径下的各文件下面的gz目录转移到当前目录
``` shell
dir -w 1 -d *-1r > all_data.txt
cat all_data.txt| while read rawfile  
do
#echo ${rawfile}
mv ${rawfile}/*gz .
done 
```

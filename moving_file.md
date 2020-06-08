# 跨服务器传递数据 
scp <source> <destination>
  
To copy a file from B to A while logged into B:

scp /path/to/file username@a:/path/to/destination

To copy a directory:

scp -r username@example.com:/remote/path/to/directory  /local/path

scp -r /local/directory/path username@example:/remote/directory/path


---
+ 将当前路径下的各文件下面的gz目录转移到当前目录
`dir -w 1 -d *-1r > all_data.txt
cat all_data.txt| while read rawfile  
do
#echo ${rawfile}
mv ${rawfile}/*gz .
done `

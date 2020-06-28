### basic structure
- read in file and read each line
- the if condition should be put with enough space
- the most useful string split is to set it to arrray and get from 0 to end
```
count=0
cat manifest.txt |  while read  i
do
if [ $count -eq 1 ]
then
array=($i)
first=`echo ${array[0]}`
second=`echo ${array[1]}`
third=`echo ${array[2]}`

echo running file $prefix

rgi bwt --read_one $second \
--read_two $third \
--aligner bowtie2 --output_file $array \
--threads 10 --include_wildcard 

rm *.temp.*
rm *.bam*


else
count=$((count+1))
fi
done
```
### time take note
```
echo begin time is `date` 
echo end time is `date` 
```
- in parallel, add joblog in the front is OK
```
"parallel --joblog jobs.txt -j %s 'humann2 --threads %s --input {} --output humann2_out/{/.}' ::: cat_reads/*fastq"
```



- skip the first line
```
cat manifest.txt | awk 'NR > 1'
echo $i
```
- echo string with only $, or it will work out to be command
```
echo $prefix
```

## the basic structure
```{r}
ggplot(data,aes(x=x,y=y)) +
geom_bar()

aes 设置参考vignette("ggplot2-specs")
```


### aes
+ if the aes setting in the ggplot, 全局设定，以后的图层都将基于该设定，在x轴，y轴用不同的数据
+ 如果想要在某个图层修改数据，可以在geom_line(aes())里面设定，设定的参数只适用于该图层
+ aes也叫作mapping，输入的color，shape等参数需要是1或者与data长度一样
+ labs 针对的是aes里面设定的变量名修改，aes之外的不会显示。
+ aes里面的变量不需要加引号，但是为了选择方便，使用```tax2[,time]```的方式比较方便
+ guides 可以取消labs标签，特别是color
+ 图层有先后顺序，后面的信息在最上层
```{r}
  ggplot(tax2_sig,aes(x = tax2[,time], y = 100 * value, group = tax2[,group])) +
    geom_line(aes(y=100* mean,color=tax2[,group]),size=2)+
    geom_point(aes(color=tax2[,group]),size=1,position = position_dodge2(width = 0.2))+
    geom_text(aes(y=100*(mean+mean_delta ),label=label),size=10,color=tax2_sig[,"label_color"]) +
    labs(x = 'treatment_time', y = 'Relative Abundance(%)', color = group,
         title = paste(variable_name,"top",topNum,sep = "--"))+ 
     guides(fill= "none")
```
#### aes fill
-  用于填充图，柱状图等，柱状图的分组设置，用于将同一变量不同水平的数据通过不同颜色展示
```{r}
 ggplot(tax2_sig,aes(x = mix,y=value, fill = tax2_sig[,group])) +
      geom_boxplot(position = position_dodge(0.8))
```

#### aes group
- 用于折线图按组连线,
```{r]
  ggplot(tax2_sig,aes(x = tax2[,time], y = 100 * value, group = tax2[,group])) +
    geom_line(aes(y=100* mean,color=tax2[,group]),size=2)
```


#### aes shape
+ 对应的数据需要是factor，提前转换好



#### 画布格子清除，保留坐标轴黑线
```{r}
   theme( panel.grid.minor = element_blank(),
             panel.background = element_blank(),panel.border = element_blank(),axis.line = element_line(colour = "black"),
             panel.grid.major=element_line(colour=NA),axis.text.x=element_text(angle=0,hjust=0.5,size = 8))

```
#### text
- theme 里面设置不同位置的参数，通过element_text指定,axis.line 设置图上的线条
```    通用
    theme(panel.grid = element_blank(), 
        legend.text = element_text(size = 15),legend.title = element_text(size=20),# for legend
               axis.text=element_text(size=15),axis.title = element_text(size=15), # for axis and its title
               strip.text=element_text(size=15))  # for facet label
               
   ## 三元相图，可以将内部的线条都删除，major何minor都需要            
    theme(panel.grid = element_blank(), panel.grid.major=element_line(colour=NA),
          panel.grid.minor =element_line(colour=NA),
          legend.text = element_text(size = 20),legend.title = element_text(size=20),# for legend
          axis.text=element_text(size=20),axis.title = element_text(size=20), # for axis and its title
          strip.text=element_text(size=20))  
          
    ### 字体倾斜
    theme(axis.text.x=element_text(angle=0,hjust=0.5,size = 8))
```
#### text annotation
    annotate("text",x = sub_data_ord$pc1, y =  sub_data_ord$pc2,
              label=sub_data_ord[,text],size=3)+

#### facet 分面
- 固定scale,nrow设置分面行数，scale=“free”用于自由调整scale
```
facet_wrap(~p1$data$treatment,scale="fix",nrow=2)
```


#### color  
- 颜色设定最好通过scale_fill_manual 等，可以灵活的调节颜色参数，颜色在value 中设置的时候保证输入的为字符串，不能是factor
- fill用于填充颜色,barplot，colour用于边框颜色line , point，对于shape，只用空心的才能填充fill，实心的只能用colour，它全部都是边框的意思
- gradient 渐变色，hsv用单色、饱和度以及亮度定义颜色

```{r}
scale_colour_manual(values = scale_color)
scale_colour_manual
scale_fill_manual 
scale_fill_gradient(low=hsv(1,.1,.7),high=hsv(1,1,1))

geom_point(aes(fill =sub_data_ord[,  color],size=sub_data_ord[,size]),color="black",shape =  21) ## color for boarder
```
- scale 只能设置一次，所以如果多个图层使用不同的颜色需要用不同形状，对应不同scale，空心的用fill调整gradient颜色，实心的用color调整,shape=16 为实心
```{r}
    ggplot(sub_data_ord, aes( pc1, pc2)) +
      geom_point(data=sub_data_ord[sub_data_ord[,color]=="Y2",],
                 aes(fill =sub_data_ord[sub_data_ord[,color]=="Y2",size],
                     size=sub_data_ord[sub_data_ord[,color]=="Y2",size]),color="black",shape=21) +
      scale_size_continuous(range=c(5,12))+
      scale_fill_gradient(low=hsv(1,.1,.7),high=hsv(1,1,1))+
      geom_point(data=sub_data_ord[sub_data_ord[,color]=="O2",],
                 aes(color =sub_data_ord[sub_data_ord[,color]=="O2",size],
                     size=sub_data_ord[sub_data_ord[,color]=="O2",size]),shape=16) +
      scale_color_gradient(low=hsv(.5,.1,.7),high=hsv(.5,1,1))
```
#### size
- size 都是数值型，一般设定的range根据数值型的范围进行调整,range(5,9)按照距离分配在-25，0，7三个数值之间，用gif作图比较方便
```{r}
pcoa_plot_size(data_ord,pcoa,metric=metric,title_name = "day -25 to day 7 ",size="timeDSS",
               var1 = "timeDSS",var1_sub = c(-25,0,7),
               color = "donor2acceptor",shape = "donor2acceptor",text="timeDSS")+
  # scale_fill_manual(values = c("blue","red",hsv(.1,1,1),hsv(.5,1,1),"purple"))+
  scale_size_continuous(range=c(5,9))+
  coord_cartesian(xlim=range(-0.3,0.4),ylim=range(-0.5,0.35)) 
```
#### linetype
- The different line types available in R software are : “blank”, “solid”, “dashed”, “dotted”, “dotdash”, “longdash”, “twodash”.
```{r}
ggplot(df2, aes(x=time, y=bill, group=sex)) +
  geom_line(aes(linetype=sex))+
  geom_point()+
  scale_linetype_manual(values=c("twodash", "dotted"))+
  theme(legend.position="top")
```

#### axis 范围
```{r}
ylim(0,NA) ### 设定最小值
```


#### ggplot对象生成后额外添加修改，字体等需要重新定义
```
line_plot2(tax_melt = dis_melt,group = "donor2acceptor",time="variable",mad=FALSE,
           scale_color = c("red","blue","green","brown"))+
  labs(y="distance to baseline(%)",title="FMT+DSS-- distance to DSS day0")+ ## change the labs and the theme needed to change as well
  theme(panel.grid = element_blank(),
        legend.text = element_text(size = 20),legend.title = element_text(size=20),
        axis.text=element_text(size=20),axis.title = element_text(size=20))
```


#### save figure
```
ggsave('pcoa_all.png', p, width = 6, height = 5)
```

### variable ploting 
#### 条形图
- x轴需要是factor或者数字
- 条形堆叠，堆叠顺序与factor有关,可以调整factor改变位置
```{r}
ggplot(rawdata[1:10,],aes(x=Country,y=Recs)) +
  geom_bar(stat= "identity",fill = rainbow(10),colour = "white") 
```
- 条形分列
```
ggplot(same_melt,aes(x=gene_name,weight=value,fill=variable)) +
  geom_bar(position =  "dodge")
```

#### 折线图
- 数据排好序，按照x轴排序
```{r}
data_all = data_all[order(data_all[,color]),]  ## 按照时间顺序等排序

geom_path(aes(x=pc1_mean,y=pc2_mean,group=data_all[,shape])) # geom_path或者geom_line 都可以
```
- 最后可以额外加上箭头,输入具体位置
```{r}
  geom_segment(aes(x = -.5, y = -.25, xend = 0, yend = 0),
               arrow = arrow(length = unit(0.5, "cm")),arrow.fill = "red",size=2,color="red")
               
  geom_curve  ## 有一定弧度
  geom_curve(aes(x = -.2, y = -.25, xend = 0, yend = 0),curvature =2,angle = 150,ncp = 8,
                           arrow = arrow(length = unit(0.5, "cm")),arrow.fill = "red",size=2,color="red")
```

##### 散点图
- 同一位置稍微抖动position
```{r}
ggplot(meta1,aes(x=timeFMT,y=observed,group=donor2acceptor))+
  geom_point(aes(color=donor2acceptor),size=2,position = position_dodge2(width = 0.2))
  ```


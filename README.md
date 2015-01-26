git-statistic
=============

use github to do some technology statistics.

Several days ago, I put some time on learning Erlang, which has drawed a lot of attention since Facebook acquired WhatsApp[Writen in Erlang]. But so much confusion rised during learning Erlang, such as why people didn't pay some attention to such an execellent language?

And I ever saw people published blogs about the ***language trend in github***, it's really cool, but sometime out-of-date, so I decide to build a small program to do some kinds of statistics like that.
 
Maybe in the not long future, I'll add some other data source, such as stackoverflow. 


Version 1.0.0 [MVP dev]
-----
support functions bellow:   

- Get all the repos writen in a user-defined language; [done]
- Get all the commits number each month of a user-defined language; [done]
- Get all the contributors number of each repo writen in a user-defined language[done];  
- Get the new repos each year; [done] 
- Get all the repos' data of fork, watch, star; [done]
- Get the push number of each repos in a peroid;
- Get the issues number of a repos;[done]
- Get the release number of each repos in a peroid;


The steps to use git-statis to do your statistic  
----- 
Since needs a lot of data to do the statistic, it's not a good choice to fetch data every time when you need to conduct a statistic. The best and fastest, also the most simple way to take a statistic is to download all the data you need in advanced. And for your convinent, I have downloaded and pre-process the data you need to do a simple statistic. So you can easily use my data to do a simple statistic, I would update the data every month.  

The steps are as follows:    

- Download the data or just simply use my data;
- Configure your statistic parampeters;
- Start your statistic;
- Visualized your result; 


因为这些分析都不是实时的，所以很有必要先把数据down下来，后期分析直接用本地数据，所以需要有一个数据存储的过程，用数据库就太重了，直接缓存为本地json文件就可以满足使用了。   
repo数量   
commit数量   
contributor数量   
流失率   
活跃度   
forks, stars, watched   
repo总数   
issues   
要分析一下，什么样的repo是库，什么样的repo是学习资料   
分析repo的质量   

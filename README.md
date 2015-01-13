git-statistic
=============

use github to do some technology statistics.

Several days ago, I put some time on learning Erlang, which has drawed a lot of attention since Facebook acquired WhatsApp[Writen in Erlang]. But so much confusion rised during learning Erlang, such as why people didn't pay some attention to such an execellent language?

And I ever saw people published blogs about the ***language trend in github***, it's really cool, but sometime out-of-date, so I decide to build a small program to do some kinds of statistics like that.
 
Maybe in the not long future, I'll add some other data source, such as stackoverflow. 


Version 1.0.0 [MVP dev]
-----
support functions bellow:

- Get all the repos writen in a user-defined language;
- Get all the commits number each month of a user-defined language;
- Get all the contributors number of a user-defined language;


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

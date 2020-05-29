## python中的多线程和多进程

测试脚本中用三种模式去运行一个简单的测试样例，即循环一千万次对一个变量加一。三种模式分别是：串行执行三遍，用threading模块开三个“多线程”跑，用multiprocessing模块开三个进程跑。

结果如下：
```log
a = 10000001, b = 10000001, c = 10000001
cost time : 1.6796090602874756 s

myThread: count = 10000001
myThread: count = 10000001
myThread: count = 10000001
cost time : 2.3651394844055176 s

test: count = 10000001
test: count = 10000001
test: count = 10000001
cose time : 0.7939774990081787 s
```

运行时间（s）：
|串行|threading多线程|multiprocessing多进程
|--|--|--|
|1.6796|2.3651|0.7939|

时长：threading > 串行 > multiprocessing

说明python的多线程确实是假多线程，它仍然不能利用多核，而是在单核上面分配CPU的时间片，它由于比串行多出了线程之间的状态切换，所以耗时更久。而多进程是真实的多进程。

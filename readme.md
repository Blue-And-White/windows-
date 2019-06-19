本程序是一个简单的窗口锁屏程序，在这里我们能够设定一些简单的任务进行锁屏，并且写入日志。
以下是程序效果图
![images](https://github.com/Blue-And-White/windows-/blob/master/1.png?raw=true)

另外，建议你讲windows命令行改为全屏，不然代码中弄出来的覆盖的图层，会很烦人。

当我们输入完任务名称以及时间后，他会锁机到我们倒计时结束，并且写入日志
![images](https://github.com/Blue-And-White/windows-/blob/master/2.png?raw=true)
以上是简单的程序执行，除此之外，我们可以设置背景图片，在桌面上，设定的背景为1.jpg就可以改变程序背景。
![images](https://github.com/Blue-And-White/windows-/blob/master/3.png?raw=true)
成功写入日志
已知bug ：程序线程不同步问题还未解决，最后可能计时结束前1~2秒左右，鼠标键盘已经解锁了！

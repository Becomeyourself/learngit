# learngit
第一次的任务已经上传
很遗憾没能全部完成第二次的任务，下面我来讲一讲我所了解的内容把。
其实第二次任务像是第一次任务的升级版，从单纯的图像处理，加上了机器人ros这个平台，需要自己领悟，把ros和图像处理融合进来。

古月老师讲的ros非常清晰，侧重于概念和整体的介绍。他分析了，话题的发布订阅，是一种异步机制，多对多；客户端与服务器之间，是一种同步机制，一对多
话题中消息的传递，就像任务二中所说的那样，主要的框架就是：发布图像 -> 订阅话题 -> 接收图像 -> 对于每一帧图像进行处理 -> 再次发布新的图像topic
其实图像处理和话题的发布订阅，分开来看，我应该都掌握了吧。。。但是把他们两个融合起来，我没有做到。


具体的成果：在ubuntu上，我已经把OpenCV和ros装好了（过程非常痛苦）学会了创建工作空间和功能包，对于古月老师小海龟的例子可以跑通。
           任务一的颜色特征提取，OpenCV库对于图像的处理函数已经明白了。

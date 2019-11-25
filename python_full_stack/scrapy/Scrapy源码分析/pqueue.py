# -*- coding: utf-8 -*- 
# @Time : 2019/11/25 下午12:16 
# @Author : yangchengkai
# @File : pqueue.py
class PriorityQueue(object):
    """
        PriorityQueue的实现是由一个hash表组成，k是队列等级，v是队列，同时维护一个指针，指向最高的队列等级。
        在这里数值越小，代表优先级越大。
        * push(obj)入队列
        * pop()出队列
        * close()关闭
        * __len__()

    """

    def __init__(self, qfactory, startprios=()):
        """

        :param qfactory: 队列的工厂类,在这里就是queue.py下面中FifoDiskQueue等各种类。他们也都实现了push,pop方法。
        :param startprios: 初始队列优先级，比如上次关闭队列时遗留的队列优先级。
        """
        # 队列queues由散列表实现，k存储优先级，v存储这一优先级的Queue（根据qfactory的不同）的队列
        self.queues = {}
        # qfactory也就是queue.py下面中FifoDiskQueue等各种类
        self.qfactory = qfactory
        for p in startprios:
            # 如果qfactory是FifoDiskQueue或LifoSQLite这种磁盘型队列，则从文件夹+“队列”的形式读取，如果是内存型队列则没有缓存。
            self.queues[p] = self.qfactory(p)
        # curprio可以看成一个指针，指向最高优先级的队列桶
        self.curprio = min(startprios) if startprios else None

    def push(self, obj, priority=0):
        """
        入队列
        :param obj: 要插入的对象。
        :param priority:  要插入的对象的优先级。
        :return: None
        """
        # 如果hash表中没有则赋值
        if priority not in self.queues:
            self.queues[priority] = self.qfactory(priority)
        q = self.queues[priority]
        # 该优先级中队列push一个obj
        q.push(obj) # this may fail (eg. serialization error)
        # 保持指针指向最大优先级。
        if self.curprio is None or priority < self.curprio:
            self.curprio = priority

    def pop(self):
        """
        返回最大优先级的对象
        :return: 最大优先级的对象
        """
        # 如果指针为空，则返回
        if self.curprio is None:
            return
        # 获得指针指向的最大优先级的队列
        q = self.queues[self.curprio]
        # 返回队列数据
        m = q.pop()
        # 如果pop后队列为空，则删除该优先级的队列，同时重新计算指向最大优先级的指针
        if len(q) == 0:
            del self.queues[self.curprio]
            q.close()
            prios = [p for p, q in self.queues.items() if len(q) > 0]
            self.curprio = min(prios) if prios else None
        # 返回pop的对象
        return m

    def close(self):
        """
        关闭队列并保存：如果队列长度大于0,返回该优先级
        :return: 队列不为空的优先级列表
        """
        active = []
        for p, q in self.queues.items():
            if len(q):
                active.append(p)
            q.close()
        return active

    def __len__(self):
        """
        :return:每个优先级中队列的长度和。
        """
        # 获得hash表中每个队列工厂，调用他们的len()方法，然后求和
        return sum(len(x) for x in self.queues.values()) if self.queues else 0

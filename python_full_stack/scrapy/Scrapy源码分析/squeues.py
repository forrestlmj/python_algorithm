# -*- coding: utf-8 -*- 
# @Time : 2019/11/26 上午7:06 
# @Author : yangchengkai
# @File : squeues.py
"""
Scheduler queues
"""

import marshal
from six.moves import cPickle as pickle

from queuelib import queue

def _serializable_queue(queue_class, serialize, deserialize):
    """
    继承父类，重写push,pop方法，使用指定的方式对数据进行序列化与反序列化。
    :param queue_class: 父类名称
    :param serialize: 序列化方法
    :param deserialize: 反序列化方法
    :return: 放回子类
    """

    class SerializableQueue(queue_class):

        def push(self, obj):
            """
            序列化入队列的对象
            :param obj:要入队列的对象
            :return: 无
            """
            s = serialize(obj)
            super(SerializableQueue, self).push(s)

        def pop(self):
            """
            反序列化出对列的对象
            :return: 反序列化的对象
            """
            s = super(SerializableQueue, self).pop()
            if s:
                return deserialize(s)

    return SerializableQueue

def _pickle_serialize(obj):
    """
    使用pickle的dumps方法。
    :param obj:
    :return:
    """
    try:
        return pickle.dumps(obj, protocol=2)
    # Python>=3.5 raises AttributeError here while
    # Python<=3.4 raises pickle.PicklingError
    except (pickle.PicklingError, AttributeError) as e:
        raise ValueError(str(e))

PickleFifoDiskQueue = _serializable_queue(queue.FifoDiskQueue, \
    _pickle_serialize, pickle.loads)
PickleLifoDiskQueue = _serializable_queue(queue.LifoDiskQueue, \
    _pickle_serialize, pickle.loads)
MarshalFifoDiskQueue = _serializable_queue(queue.FifoDiskQueue, \
    marshal.dumps, marshal.loads)
MarshalLifoDiskQueue = _serializable_queue(queue.LifoDiskQueue, \
    marshal.dumps, marshal.loads)
FifoMemoryQueue = queue.FifoMemoryQueue
LifoMemoryQueue = queue.LifoMemoryQueue

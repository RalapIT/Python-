'''
异常处理
如果程序没有进行异常处理
那么在遇到异常的时候,整个程序都会退出
要解决这个问题,那么就需要对出现异常的地方进行异常捕获

'''
#注意,出现异常,异常以后的为值得内容都不会执行,直接退出程序
'''

使用try将可能报错的包裹起来
如果try结构中报错了,跳过try结构中还没进行的except子句
except子句执行后继续执行外面的内容,程序不会退出
如果try结构中没有报错 则不会进入except子句,直接执行后面的内心


'''
# print(1)
# num = 0
# try:
#     num = int(input("请输入一个数字"))
#     print(2)
# except:
#     print("出现异常了")
#
# print(num)
# print(3)

#捕获某些特定的异常

# print(1)
# num = 0
# try:
#     # 1 / 0
#     print(2)
#     li = [12,23]
#     next(iter(li))
#     num=int(input("请输入一个数字"))
#     print(3)
# except Exception as e:#
#     print(e)
# except ZeroDivisionError as e:#捕获的是参数类型的错误
#     #可以针对性捕获某个异常
#     print(e)
# except ValueError as e :
#     print(e)
#     print("只要执行这里面就是报了异常")
#     print("可以将异常信息写入日志文件")
# except IndexError as e:
#     print(e)
#     print("下标越界,下次不要乱搞了")
# except StopAsyncIteration as e:
#     print("迭代器又越界了")
# print(num)
# print(4)
'''
python标准异常
异常名称	            描述

BaseException	所有异常的基类
SystemExit	解释器请求退出
KeyboardInterrupt	用户中断执行(通常是输入^C)
Exception	常规错误的基类
StopIteration	迭代器没有更多的值
GeneratorExit	生成器(generator)发生异常来通知退出
StandardError	所有的内建标准异常的基类
ArithmeticError	所有数值计算错误的基类
FloatingPointError	浮点计算错误
OverflowError	数值运算超出最大限制
ZeroDivisionError	除(或取模)零 (所有数据类型)
AssertionError	断言语句失败
AttributeError	对象没有这个属性
EOFError	没有内建输入,到达EOF 标记
EnvironmentError	操作系统错误的基类
IOError	输入/输出操作失败
OSError	操作系统错误
WindowsError	系统调用失败
ImportError	导入模块/对象失败
LookupError	无效数据查询的基类
IndexError	序列中没有此索引(index)
KeyError	映射中没有这个键
MemoryError	内存溢出错误(对于Python 解释器不是致命的)
NameError	未声明/初始化对象 (没有属性)
UnboundLocalError	访问未初始化的本地变量
ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError	一般的运行时错误
NotImplementedError	尚未实现的方法
SyntaxError	Python 语法错误
IndentationError	缩进错误
TabError	Tab 和空格混用
SystemError	一般的解释器系统错误
TypeError	对类型无效的操作
ValueError	传入无效的参数
UnicodeError	Unicode 相关的错误
UnicodeDecodeError	Unicode 解码时的错误
UnicodeEncodeError	Unicode 编码时错误
UnicodeTranslateError	Unicode 转换时错误
Warning	警告的基类
DeprecationWarning	关于被弃用的特征的警告
FutureWarning	关于构造将来语义会有改变的警告
OverflowWarning	旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning	关于特性将会被废弃的警告
RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
SyntaxWarning	可疑的语法的警告
UserWarning	用户代码生成的警告
'''
try :
    # 1/0
    pass
except Exception :
    print('出错了')
else:
    print("这是else中的内容")
    #没有报错就会执行
    #如果报错就不执行
finally:
    print("不管你报错还是没报错,这里面一定执行")
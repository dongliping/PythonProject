## Python 类

### 面向对象的三要素
* 封装  
* 继承  
* 多态

### 类的定义
```python
    def className:
        pass
```
&emsp;&emsp;类定义完成后就产生了一个类对象，绑定到了classname上。

### 类的实例化
```python
obj = className()
```

### 实例对象
**类对象**，类的定义就会生成一个类对象。  
**类的属性**，类定义中的变量和类中定义的方法都是类属性。  
**类变量**，x是类MyClass的类变量
```python
# -*- coding:UTF-8 -*-
class MyClass:
	x='abc'  #类属性
	def foo(self):   #类属性foo，也是方法
		return 'My class'
```
&emsp;&emsp;foo方法是类属性，如同吃是人类的方法，但是每一个具体的人才能吃东西，就是说吃是人的实例才能调用的方法。  
&emsp;&emsp;Foo是method方法对象，不是普通的函数对象function了，它必须至少有1个参数，且第一个参数必须是self（self可以换个名字），这个参数位置就留给了self。
### Self
```python
# -*- coding:UTF-8 -*-
class MyClass:
	def __init__(self):
		print "self in init={}".format(id(self))
c=MyClass()
print 'c={}'.format(id(c))


self in init=40848520
c=40848520
[Finished in 0.3s]
```
&emsp;&emsp;上列说明，self就是调用者，就是c对应的实例对象
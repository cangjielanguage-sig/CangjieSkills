### Exception 类案例分析

`Exception` 类问题一般是开发者或仓颉标准库自主抛出的仓颉异常。

这类问题目前有两种场景：

1. 如果是当前应用程序遇到无法解决的只能终止当前业务的故障，需要考虑抛出仓颉异常来终止业务并生成故障日志。

2. 依赖使用仓颉标准库模块接口，对于可能抛出异常的接口，需要考虑使用 `try-catch` 机制进行捕获，或者提前增加保护性检查，否则也会终止当前业务。

#### 案例一：开发者自主抛出一个自定义的仓颉异常来终止程序

开发者自主抛出仓颉异常，可以通过如下代码实现：

```cangjie
throw Exception("throwing exception")
```

或者继承内置的 `Exception` 或其子类来自定义异常并抛出，自定义异常的代码实现请参见[定义异常](https://developer.huawei.com/consumer/cn/doc/cangjie-guides/cj-exception_overview)。

该类问题，通过故障日志中异常代码堆栈的栈顶抛出点可以直接定位到具体的代码行。

![image-20250425104944](./figures/cangjiecrash_image_001.png)

之后进一步检视上下文来分析问题即可。
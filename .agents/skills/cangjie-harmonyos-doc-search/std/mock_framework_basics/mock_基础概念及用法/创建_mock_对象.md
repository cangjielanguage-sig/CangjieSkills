## 创建 mock 对象

**mock 构造函数**可以通过调用 `mock<T>` 和 `spy<T>` 函数来创建两种对象：**mock** 和 **spy**，其中 `T` 表示被 mock 的类或接口。

```cangjie
public func mock<T>(): T
public func spy<T>(objectToSpyOn: T): T
```

<!-- 链接至 mock/spy 构造函数 -->

**mock** 作为骨架对象，默认不对成员进行任何操作。

**spy** 作为一种特殊的 mock 对象用于封装某个类或接口的当前实例。默认情况下，spy 对象将其成员调用委托给底层对象。
其他方面，spy 和 mock 对象非常相似。

只有**类**（包括 final 类和 sealed 类）和**接口**支持通过这种方式 mock 。

参阅[使用 mock 和 spy 对象](#使用-spy-和-mock-对象)。

参阅[顶级和静态声明](#顶级和静态声明) 了解如何 mock 顶级和静态声明。
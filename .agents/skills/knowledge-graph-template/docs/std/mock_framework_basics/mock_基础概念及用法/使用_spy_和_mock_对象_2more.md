## 使用 spy 和 mock 对象

**spy** 对象和 **mock** 对象在配置上是类似的，只不过 spy 对象监控的是当前实例。

主要区别如下：成员调用没有触发任何桩时，spy 对象调用底层实例的原始实现，mock 对象抛出运行时错误（并且测试失败）。

mock 对象无需创建真正的依赖来测试 API ，只需配置特定测试场景所需的行为。

spy 对象支持重写真实实例的可观察行为。只有通过 spy 对象引用的调用才会被拦截。创建 spy 对象对原始 spy 实例的引用无影响。spy 调用自己的方法不会被拦截。

<!--compile.onlyformat-->
```cangjie
let serviceSpy = spy(service)
// 模拟超时，继续使用真正的实现
@On(serviceSpy.request()).throws(TimeoutException()).once().then().callsOriginal()
// 测试代码必须使用'serviceSpy'引用
```

> **注意：**
>
> 静态成员或顶级函数/变量的打桩行为类似于 spy，即对于未打桩的声明，将调用原始成员或原顶级函数/变量，而不是像 mock 中那样抛出异常。

## mock 依赖

接口始终可以被 mock 。从另一个包 mock 一个类时，类本身和它的超类必须按特定方式编译，
即只能 mock 预编译库（如 **stdlib** ）中的接口，不能 mock 类。

### 使用 cjc 编译

对于 **cjc** 来说，mock 是通过 `--mock` 标志来控制的。
如果想 mock 特定包中的类 `p` ，添加 `--mock=on` 标志到 cjc 进行调用。

> **说明：**
>
> 在编译依赖 `p` 的包时，也必须添加此标志。

在测试中使用 mock 对象（ `cjc --test` ）不需要额外的标志。

### 使用 cjpm 编译

**cjpm** 会自动检测 mock 使用，并生成正确的 **cjc** 调用，确保可以从任何从源代码编译的包中 mock 类。

还可以使用 cjpm 配置文件控制哪些包支持 mock 。

<!-- 待办：添加关于默认 mock 行为的章节。-->

<!-- 待办：添加对其他文档的引用。-->
## 配置 API

**配置 API** 是框架的核心，可以定义 mock/spy 对象成员（或顶层/静态声明）的行为（或重新定义 spy 对象（或顶层/静态声明））。

**配置 API** 的入口是 `@On` 宏调用。

<!--compile.onlyformat-->
```cangjie
@On(storage.getComments(testId)).returns(testComments)
```

示例中，如果 mock 对象 `storage` *接收*到 `getComments` 方法的调用，并且指定了参数 `testId` ，则返回 `testComment` 。

如上行为即为**打桩**，桩（Stub， 模拟还未实现或无法在测试环境中执行的组件）需在测试用例主体内部先定义。

如下声明类型可以被打桩：

* 类和接口的实例成员（包括 final 成员）
* 静态函数、属性和字段
* 顶层函数和变量

以下声明**不能**打桩：

* 扩展成员
* Foreign 函数
* 局部函数和变量
* 构造器
* 常量
* 任意私有声明

一个完整的**桩声明**包含以下部分：

1. `@On` 宏调用中描述的**桩签名**。
2. 用于描述桩行为的[操作](#操作-api)。
3. （可选）用于设置[预期](#预期)的基数说明符（cardinality specifier， 指定预期执行次数的表达式）。
4. （可选）[续体](#桩链)（continuation， 支持链式调用的表达式）。

mock 框架拦截匹配桩签名的调用，并执行桩声明中指定的操作。

### 顶级和静态声明

与类或接口的成员不同，要打桩静态成员或顶层函数或变量时，不需要创建模拟对象。这些声明应该直接使用配置 API （例如 `@On` 宏）进行打桩。

如下是一个为顶层函数打桩的示例：

<!--run -->
```cangjie
import std.unittest.mock.*
import std.unittest.mock.mockmacro.*

public class Entry {
    Entry(let id: Int64, let title: String, let description: String) {}
    static func parse(): Entry {
        Entry(1, "1", "1")
    }
}

public func loadLastEntryInCatalog(): Entry {
    return Entry.parse()
}

public func drawLastEntryWidget() {
    let lastEntry = loadLastEntryInCatalog()
    // drawing...
}

@Test
class RightsTest {
    @TestCase
    func removeLastEntry() {
        @On(loadLastEntryInCatalog()).returns(Entry(1, "Test entry", "Test description"))
        drawLastEntryWidget()
    }
}
```

### 桩签名

**桩签名**定义了与特定调用子集匹配的一组条件，包括以下部分：

* mock/spy 对象的引用，必须是单个标识符。（独立声明（顶层或静态函数、变量）不需要此部分）
* 成员以及独立声明的调用。
* 特定格式的参数调用，参见[参数匹配器](#参数匹配器)。

签名可以匹配以下实体：

* 方法
* 属性 getter
* 属性 setter
* 字段读操作
* 字段写操作
* 静态函数
* 静态属性 getter
* 静态 属性 setter
* 静态字段读操作
* 静态字段写操作
* 顶层函数
* 顶层字段读操作
* 顶层字段写操作

只要对应声明被调用，并且所有参数（若有）都与相应的参数匹配器匹配时，桩签名就会匹配调用。

方法的桩的签名结构：`<mock object name>.<method name>(<argument matcher>*)`。

<!--compile.onlyformat-->
```cangjie
@On(foo.method(0, 1)) // 带参数 0 和 1 的方法调用
@On(foo.method(param1: 0, param2: 1)) // 带命名参数的方法调用
```

当桩属性 getter/setter 或字段读/写操作时，使用 `<mock object name>.<property or field name>` 或 `<mock object name>.<property or field name> = <argument matcher>` 。

<!--compile.onlyformat-->
```cangjie
@On(foo.prop) // 属性 getter
@On(foo.prop = 3) // 参数为 3 的属性 setter
```

对于顶层函数和静态函数，签名是类似的：

* 顶层函数：`<function name>(<argument matcher>*)`
* 静态函数：`<class name>.<static method name>(<argument matcher>*)`

顶层变量和静态属性或字段的签名如下：

* 顶层变量：`<top-level variable name>` 或 `<top-level variable name> = <argument matcher>`
* 静态属性或字段：`<class name>.<static property/field name>` 或 `<class name>.<static property/field name> = <argument matcher>`

对运算符函数打桩时，运算符的接收者必须是对 mock/spy 对象的单个引用，而运算符的参数必须是参数匹配器。

<!--compile.onlyformat-->
```cangjie
@On(foo + 3) // 'operator func +'，参数为 3
@On(foo[0]) // 'operator func []'，参数为 0
```
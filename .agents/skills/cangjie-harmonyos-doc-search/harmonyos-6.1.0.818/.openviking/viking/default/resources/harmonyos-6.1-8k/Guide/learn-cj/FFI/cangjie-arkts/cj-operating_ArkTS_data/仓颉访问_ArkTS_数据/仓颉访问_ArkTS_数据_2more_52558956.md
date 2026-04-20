# 仓颉访问 ArkTS 数据

此章节详细介绍通过 JSValue 类型使用 ArkTS 数据。

## 使用方法

1. 获取 JSValue 对应的 ArkTS 类型

   从 ArkTS 传过来的参数，其原始类型是`JSValue`，这是一个匿名类型的数据，首先需要获取其类型。获取类型有以下两种方式：

   - 通过 `JSValue.typeof()` 获取其类型枚举 `JSType`。
   - 通过其他途径（包括但不限于阅读 ArkTS 源码、参考文档等）知晓其类型，然后通过类型校验接口来验证，比如判断是否是 number 类型 `JSValue.isNumber()`。

2. 使用 JSValue

   获取 JSValue 类型之后，可以将 `JSValue` 转换为对应的仓颉类型或 ArkTS 引用。

   - 转换为仓颉类型。此时仓颉数据为 ArkTS 数据的拷贝，ArkTS 数据可能在仓颉变量生命周期中释放。例如 ArkTS string 转换为仓颉 String，`var a:String = JSValue.toString(JSContext)`。
   - 转换为 ArkTS 引用。此时仓颉数据为 ArkTS 数据的引用，ArkTS 数据不能在仓颉变量生命周期中释放。比如一个 ArkTS string 转换为 JSString，`var b:JSString = JSValue.asString(JSContext)`。

3. 构造仓颉类型的 ArkTS 数据

   通过仓颉类型来构造 ArkTS 数据，是通过 JSContext 的方法类来构造的。以 `number` 为例，创建一个 `number` 的方式是 `var a : Float64 = JSContext.number(Float64)`。

   ArkTS 主要数据类型对应到仓颉类型的映射如下：

| ArkTS 类型 | 引用类型    | typeof 类型      |
| ---------- | ----------- | ---------------- |
| undefined  | JSUndefined | JSType.UNDEFINED |
| null       | JSNull      | JSType.NULL      |
| boolean    | JSBoolean   | JSType.BOOL      |
| number     | JSNumber    | JSType.NUMBER    |
| string     | JSString    | JSType.STRING    |
| object     | JSObject    | JSType.OBJECT    |
| Array      | JSArray     | JSType.OBJECT    |
| bigint     | JSBigInt    | JSType.BIGINT    |
| function   | JSFunction  | JSType.FUNCTION  |
| symbol     | JSSymbol    | JSType.SYMBOL    |
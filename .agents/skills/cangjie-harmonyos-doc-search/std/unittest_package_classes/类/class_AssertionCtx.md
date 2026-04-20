## class AssertionCtx

```cangjie
public class AssertionCtx {}
```

功能：存储用户定义的断言的状态。提供用于编写​​用户定义断言的方法。

### prop args

```cangjie
public prop args: String
```

功能：返回以逗号分隔的未解析的用户定义断言参数的字符串。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)。

### prop caller

```cangjie
public prop caller: String
```

功能：获取用户定义的断言函数的标识符。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)。

### prop hasErrors

```cangjie
public prop hasErrors: Bool
```

功能：如果用户定义内的任何断言失败，则为 `true` 。否则为 `false`。

类型：[Bool](../../core/core_package_api/core_package_intrinsics.md#bool)

### func arg(String)

```cangjie
public func arg(key: String): String
```

功能：返回表示原始传递的标识符的参数值的字符串表达，与参数列表中的标识符匹配。

参数：

- key: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 函数参数列表中的标识符。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 对应标识符的参数值字符串表达。

### func fail(String)

```cangjie
public func fail(message: String): Nothing 
```

功能：存储失败信息，在用户定义的断言函数中提供并抛出 [`AssertExpection`](./unittest_package_exceptions.md#class-assertexception)。

参数：

- message: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 失败信息。

### func fail\<PP>(PP)

```cangjie
public func fail<PP>(pt: PP): Nothing where PP <: PrettyPrintable
```

功能：存储失败信息，在用户定义的断言函数中提供并抛出 [`AssertExpection`](./unittest_package_exceptions.md#class-assertexception)。

参数：

- pt: PP <: [PrettyPrintable](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-prettyprintable) - 失败信息。

### func failExpect(String)

```cangjie
public func failExpect(message: String): Unit 
```

功能：存储失败信息，在用户定义的断言函数内提供并继续函数执行。

参数：

- message: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 失败信息。

### func failExpect\<PP>(PP)

```cangjie
public func failExpect<PP>(pt: PP): Unit where PP <: PrettyPrintable
```

功能：存储失败信息，在用户定义的断言函数内提供并继续函数执行。

参数：

- pt: PP <: [PrettyPrintable](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-prettyprintable) - 失败信息。

### func setArgsAliases(Array\<String>)

```cangjie
public func setArgsAliases(aliases: Array<String>): Unit
```

功能：设置别名以通过函数 [`arg`](#func-argstring) 访问未解析的用户定义的断言函数参数。框架内部使用，用户无需使用该函数。

参数：

- aliases: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 标识符数组。数组的大小应与参数列表匹配（除 [`AssertionCtx`](#class-assertionctx) 外）。
## class PowerAssertDiagramBuilder

```cangjie
public class PowerAssertDiagramBuilder {
    public init(expression: String)
}
```

功能：[PowerAssert](../../unittest_testmacro/unittest_testmacro_package_api/unittest_testmacro_package_macros.md#powerassert-宏) 输出结果构造器。

### init(String)

```cangjie
public init(expression: String)
```

功能：构造函数。

参数：

- expression: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 表达式字符串。

### func r\<T>(T, String, Int64)

```cangjie
public func r<T>(
    value: T,
    exprAsText: String,
    position: Int64
): T 
```

功能：记录对比数据。

参数：

- value: T - 被记录的数据。
- exprAsText: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 表达式字符串。
- position: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 位置信息。

返回值：

- T - 被记录的数据。

### func r(String, String, Int64)

```cangjie
public func r(
    value: String,
    exprAsText: String,
    position: Int64
): String
```

功能：记录对比数据。

参数：

- value: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 被记录的数据。
- exprAsText: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 表达式字符串。
- position: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 位置信息。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 被记录的数据。

### func r(Rune, String, Int64)

```cangjie
public func r(
    value: Rune,
    exprAsText: String,
    position: Int64
): Rune
```

功能：记录对比数据。

参数：

- value: [Rune](../../core/core_package_api/core_package_intrinsics.md#rune) - 被记录的数据。
- exprAsText: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 表达式字符串。
- position: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 位置信息。

返回值：

- [Rune](../../core/core_package_api/core_package_structs.md#struct-string) - 被记录的数据。

### func h(Exception, String, Int64)

```cangjie
public func h(
    exception: Exception,
    exprAsText: String,
    position: Int64
): Nothing
```

功能：处理异常。

参数：

- exception: Exception - 需要被处理的异常。
- exprAsText: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 表达式字符串。
- position: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 位置信息。

### func w(Bool)

```cangjie
public func w(passed: Bool): Unit
```

功能：当用例通过时返回成功结果，失败时抛出异常并打印对比结果。

参数：

- passed: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 用例是否通过。
### static func stubSetter\<TArg>(() -> Unit, () -> TArg,ArgumentMatcher,Option\<String>,String,String,Int64)

```cangjie
public static func stubSetter<TArg>(
    stubCall: () -> Unit,
    _: () -> TArg,
    matcher: ArgumentMatcher,
    prefixRefName: Option<String>,
    fieldOrPropertyName: String,
    callDescription: String,
    lineNumber: Int64
): SetterActionSelector<TArg>
```

功能：创建针对属性 Setter 方法插入桩代码的操作器对象。

参数：

- stubCall: () -> Unit - 桩签名对应的调用表达式。
- _: () -> TArg - 用于捕获属性或者字段的类型。
- matcher: [ArgumentMatcher](#class-argumentmatcher) - 入参的参数匹配器。
- prefixRefName: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 用于模拟类/接口成员的对象引用令牌，用于模拟静态声明的类型引用令牌，用于顶级声明的时为 None。
- fieldOrPropertyName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 被插桩的属性或字段的名称。
- callDescription: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 桩签名对应的调用表达式的字符串表达。
- lineNumber: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 对应的调用表达式的行号。

返回值：

- [MethodActionSelector](#class-methodactionselectortret)\<TRet> - 针对普通成员方法插入桩代码的操作器对象。
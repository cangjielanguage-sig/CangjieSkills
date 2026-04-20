## class ConfigureMock

```cangjie
public class ConfigureMock {}
```

功能：配置 `mock object` 。

### static func stubGetter\<TRet>(() -> TRet,Option\<String>,String,String,Int64)

```cangjie
public static func stubGetter<TRet>(
    stubCall: () -> TRet,
    prefixRefName: Option<String>,
    fieldOrPropertyName: String,
    callDescription: String,
    lineNumber: Int64
): GetterActionSelector<TRet>
```

功能：创建针对属性的 Getter 方法插入桩代码的操作器对象。

参数：

- stubCall: () -> TRet - 桩签名对应的调用表达式。
- prefixRefName: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 用于模拟类/接口成员的对象引用令牌，用于模拟静态声明的类型引用令牌，用于顶级声明的时为 None。
- fieldOrPropertyName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 被插桩的字段或属性名称。
- callDescription: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 桩签名对应的调用表达式的字符串表达。
- lineNumber: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 对应的调用表达式的行号。

返回值：

- [GetterActionSelector](#class-getteractionselectortret)\<TRet> - 针对属性的 Getter 方法插入桩代码的操作器对象。

### static func stubFunction\<TRet>(() -> TRet, Array\<ArgumentMatcher>, Option\<String>, String, String, Int64)

```cangjie
public static func stubFunction<TRet>(
    stubCall: () -> TRet,
    matchers: Array<ArgumentMatcher>,
    prefixRefName: Option<String>,
    methodName: String,
    callDescription: String,
    lineNumber: Int64
): MethodActionSelector<TRet>
```

功能：创建针对普通成员方法插入桩代码的操作器对象。

参数：

- stubCall: () -> Unit - 桩签名对应的调用表达式。
- _: () -> TArg - 用于捕获属性或者字段的类型。
- matchers: Array\<[ArgumentMatcher](#class-argumentmatcher)> - 对应入参的参数匹配器。
- prefixRefName: [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 用于模拟类/接口成员的对象引用令牌，用于模拟静态声明的类型引用令牌，用于顶级声明的时为 None。
- methodName: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 方法的名称。
- callDescription: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 桩签名对应的调用表达式的字符串表达。
- lineNumber: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 对应的调用表达式的行号。

返回值：

- [MethodActionSelector](#class-methodactionselectortret)\<TRet> - 针对普通成员方法插入桩代码的操作器对象。
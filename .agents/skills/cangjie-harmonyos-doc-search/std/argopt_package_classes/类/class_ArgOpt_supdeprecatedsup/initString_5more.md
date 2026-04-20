### init(String)

```cangjie
public init(shortArgFormat: String)
```

功能：构造 `ArgOpt` 实例，并从短参名字符串中解析短参名。

参数：

- shortArgFormat: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 包含短参名的字符串。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当短参名字符串不符合规范，或字符串不符合 UTF-8 编码，或不存在该 Unicode 字符时，抛出异常。

### init(String, Array\<String>)

```cangjie
public init(shortArgFormat: String, longArgList: Array<String>)
```

功能：构造 `ArgOpt` 实例，并从短参名字符串中解析短参名，从列表的字符串中解析长参名。

参数：

- shortArgFormat: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 包含短参名的字符串。
- longArgList: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 包含长参名的字符串数组。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当短参名字符串不符合规范，或字符串数组中的长参名字符串不符合规范，或字符串不符合 UTF-8 编码，或不存在该 Unicode 字符时，抛出异常。

### func getArg(String)

```cangjie
public func getArg(arg: String): Option<String>
```

功能：返回参数 `arg` 指定参数的解析值。

参数：

- arg: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 前缀和参数名组成的字符串（可省略前缀）。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 参数解析值。

### func getArgumentsMap()

```cangjie
public func getArgumentsMap(): HashMap<String, String>
```

功能：获取所有已解析的参数名和参数值，以哈希表的形式返回。

返回值：

- [HashMap](../../collection/collection_package_api/collection_package_class.md#class-hashmapk-v-where-k--hashable--equatablek)\<[String](../../core/core_package_api/core_package_structs.md#struct-string), [String](../../core/core_package_api/core_package_structs.md#struct-string)> - 已解析的参数名为键，参数值为值的哈希表。

### func getUnparseArgs()

```cangjie
public func getUnparseArgs(): Array<String>
```

功能：返回未被解析的命令行参数。

返回值：

- [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)> - 存放没有被解析的字符串的数组。
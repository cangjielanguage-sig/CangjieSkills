### operator func !=(String)

```cangjie
public operator const func !=(right: String): Bool
```

功能：判断两个字符串是否不相等。

参数：

- right: [String](core_package_structs.md#struct-string) - 待比较的 [String](core_package_structs.md#struct-string) 实例。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 不相等返回 true，相等返回 false。

### operator func *(Int64)

```cangjie
public operator const func *(count: Int64): String
```

功能：原字符串重复 [count](../../collection/collection_package_api/collection_package_function.md#func-counttiterablet) 次。

参数：

- count: [Int64](core_package_intrinsics.md#int64) - 原字符串重复的次数。

返回值：

- [String](core_package_structs.md#struct-string) - 返回重复 [count](../../collection/collection_package_api/collection_package_function.md#func-counttiterablet) 次后的新字符串。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 当试图构造长度超过 [UInt32 的最大值](./core_package_intrinsics.md#uint32) 的字符串时，抛出异常。

### operator func +(String)

```cangjie
public operator const func +(right: String): String
```

功能：两个字符串相加，将 right 字符串拼接在原字符串的末尾。

参数：

- right: [String](core_package_structs.md#struct-string) - 待追加的字符串。

返回值：

- [String](core_package_structs.md#struct-string) - 返回拼接后的字符串。

异常：

- [IllegalArgumentException](core_package_exceptions.md#class-illegalargumentexception) - 当试图构造长度超过 [UInt32 的最大值](./core_package_intrinsics.md#uint32) 的字符串时，抛出异常。

### operator func <(String)

```cangjie
public operator const func <(right: String): Bool
```

功能：判断两个字符串大小。

参数：

- right: [String](core_package_structs.md#struct-string) - 待比较的字符串。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 原字符串字典序小于 right 时，返回 true，否则返回 false。

### operator func <=(String)

```cangjie
public operator const func <=(right: String): Bool
```

功能：判断两个字符串大小。

参数：

- right: [String](core_package_structs.md#struct-string) - 待比较的字符串。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 原字符串字典序小于或等于 right 时，返回 true，否则返回 false。

### operator func ==(String)

```cangjie
public operator const func ==(right: String): Bool
```

功能：判断两个字符串是否相等。

参数：

- right: [String](core_package_structs.md#struct-string) - 待比较的字符串。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 相等返回 true，不相等返回 false。

### operator func >(String)

```cangjie
public operator const func >(right: String): Bool
```

功能：判断两个字符串大小。

参数：

- right: [String](core_package_structs.md#struct-string) - 待比较的字符串。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 原字符串字典序大于 right 时，返回 true，否则返回 false。

### operator func >=(String)

```cangjie
public operator const func >=(right: String): Bool
```

功能：判断两个字符串大小。

参数：

- right: [String](core_package_structs.md#struct-string) - 待比较的字符串。

返回值：

- [Bool](core_package_intrinsics.md#bool) - 原字符串字典序大于或等于 right 时，返回 true，否则返回 false。
## interface Parsable\<T>

```cangjie
public interface Parsable<T> {
    static func parse(value: String): T
    static func tryParse(value: String): Option<T>
}
```

功能：本接口提供了统一的方法，以支持将字符串解析为特定类型。

本接口提供了 parse 和 tryParse 两套方法，parse 方法将在解析失败时抛出异常，tryParse 方法将返回值用 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont) 包裹，解析失败时将返回 None。
本包内已经为 [Bool](../../core/core_package_api/core_package_intrinsics.md#bool)，[Rune](../../core/core_package_api/core_package_intrinsics.md#rune)，[Float16](../../core/core_package_api/core_package_intrinsics.md#float16)，[Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 等基础类型实现该接口，可用于将字符串转换为这些类型。

### static func parse(String)

```cangjie
static func parse(value: String): T
```

功能：从字符串中解析特定类型。

参数：

- value: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待解析的字符串。

返回值：

- T - 转换后的值。

### static func tryParse(String)

```cangjie
static func tryParse(value: String): Option<T>
```

功能：从字符串中解析特定类型。

参数：

- value: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 待解析的字符串。

返回值：

- [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T> - 转换后值，转换失败返回 [Option](../../core/core_package_api/core_package_enums.md#enum-optiont)\<T>.None。
## interface SwapEndianOrder\<T>

```cangjie
public interface SwapEndianOrder<T> {
    func swapBytes(): T
}
```

功能：反转字节顺序接口。

### func swapBytes()

```cangjie
func swapBytes(): T
```

功能：反转 T 值的字节顺序。

返回值：

- T - T 值。

### extend Int16 <: SwapEndianOrder\<Int16>

```cangjie
extend Int16 <: SwapEndianOrder<Int16>
```

功能：为 [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 扩展 [SwapEndianOrder](binary_package_interfaces.md#interface-swapendianordert) 接口，以实现将 [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 值的字节顺序反转。

父类型：

- [SwapEndianOrder](#interface-swapendianordert)\<[Int16](../../core/core_package_api/core_package_intrinsics.md#int16)>

#### func swapBytes()

```cangjie
public func swapBytes(): Int16
```

功能：反转 [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 值的字节顺序。

返回值：

- [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) - [Int16](../../core/core_package_api/core_package_intrinsics.md#int16) 值。

示例：

<!-- run -->
```cangjie
import std.binary.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let n = 0x1234i16
    let m = n.swapBytes()
    @Assert(m, 0x3412)
}
```

### extend Int32 <: SwapEndianOrder\<Int32>

```cangjie
extend Int32 <: SwapEndianOrder<Int32>
```

功能：为 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 扩展 [SwapEndianOrder](binary_package_interfaces.md#interface-swapendianordert) 接口，以实现将 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 值的字节顺序反转。

父类型：

- [SwapEndianOrder](#interface-swapendianordert)\<[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)>

#### func swapBytes()

```cangjie
public func swapBytes(): Int32
```

功能：反转 [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 值的字节顺序。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) 值。

示例：

<!-- run -->
```cangjie
import std.binary.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let n = 0x12345678i32
    let m = n.swapBytes()
    @Assert(m, 0x78563412)
}
```

### extend Int64 <: SwapEndianOrder\<Int64>

```cangjie
extend Int64 <: SwapEndianOrder<Int64>
```

功能：为 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 扩展 [SwapEndianOrder](binary_package_interfaces.md#interface-swapendianordert) 接口，以实现将 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 值的字节顺序反转。

父类型：

- [SwapEndianOrder](#interface-swapendianordert)\<[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)>

#### func swapBytes()

```cangjie
public func swapBytes(): Int64
```

功能：反转 [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 值的字节顺序。

返回值：

- [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) 值。

示例：

<!-- run -->
```cangjie
import std.binary.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let n = 0x1234567890123456i64
    let m = n.swapBytes()
    @Assert(m, 0x5634129078563412)
}
```
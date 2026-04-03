### extend Int8 <: SwapEndianOrder\<Int8>

```cangjie
extend Int8 <: SwapEndianOrder<Int8>
```

功能：为 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 扩展 [SwapEndianOrder](binary_package_interfaces.md#interface-swapendianordert) 接口，以实现将 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 值的字节顺序反转。

父类型：

- [SwapEndianOrder](#interface-swapendianordert)\<[Int8](../../core/core_package_api/core_package_intrinsics.md#int8)>

#### func swapBytes()

```cangjie
public func swapBytes(): Int8
```

功能：反转 [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 值的字节顺序。

返回值：

- [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) - [Int8](../../core/core_package_api/core_package_intrinsics.md#int8) 值。

示例：

<!-- run -->
```cangjie
import std.binary.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let n = 0x12i8
    let m = n.swapBytes()
    @Assert(m, 0x12)
}
```

### extend UInt16 <: SwapEndianOrder\<UInt16>

```cangjie
extend UInt16 <: SwapEndianOrder<UInt16>
```

功能：为 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 扩展 [SwapEndianOrder](binary_package_interfaces.md#interface-swapendianordert) 接口，以实现将 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 值的字节顺序反转。

父类型：

- [SwapEndianOrder](#interface-swapendianordert)\<[UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16)>

#### func swapBytes()

```cangjie
public func swapBytes(): UInt16
```

功能：反转 [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 值的字节顺序。

返回值：

- [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) - [UInt16](../../core/core_package_api/core_package_intrinsics.md#uint16) 值。

示例：

<!-- run -->
```cangjie
import std.binary.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let n = 0x1234u16
    let m = n.swapBytes()
    @Assert(m, 0x3412)
}
```

### extend UInt32 <: SwapEndianOrder\<UInt32>

```cangjie
extend UInt32 <: SwapEndianOrder<UInt32>
```

功能：为 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 扩展 [SwapEndianOrder](binary_package_interfaces.md#interface-swapendianordert) 接口，以实现将 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 值的字节顺序反转。

父类型：

- [SwapEndianOrder](#interface-swapendianordert)\<[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)>

#### func swapBytes()

```cangjie
public func swapBytes(): UInt32
```

功能：反转 [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 值的字节顺序。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) 值。

示例：

<!-- run -->
```cangjie
import std.binary.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let n = 0x12345678u32
    let m = n.swapBytes()
    @Assert(m, 0x78563412)
}
```
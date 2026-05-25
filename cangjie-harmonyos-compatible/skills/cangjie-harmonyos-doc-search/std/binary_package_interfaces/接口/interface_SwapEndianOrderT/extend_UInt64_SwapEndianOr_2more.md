### extend UInt64 <: SwapEndianOrder\<UInt64>

```cangjie
extend UInt64 <: SwapEndianOrder<UInt64>
```

功能：为 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 扩展 [SwapEndianOrder](binary_package_interfaces.md#interface-swapendianordert) 接口，以实现将 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 值的字节顺序反转。

父类型：

- [SwapEndianOrder](#interface-swapendianordert)\<[UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64)>

#### func swapBytes()

```cangjie
public func swapBytes(): UInt64
```

功能：反转 [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 值的字节顺序。

返回值：

- [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) - [UInt64](../../core/core_package_api/core_package_intrinsics.md#uint64) 值。

示例：

<!-- run -->
```cangjie
import std.binary.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let n = 0x1234567890123456u64
    let m = n.swapBytes()
    @Assert(m, 0x5634129078563412)
}
```

### extend UInt8 <: SwapEndianOrder\<UInt8>

```cangjie
extend UInt8 <: SwapEndianOrder<UInt8>
```

功能：为 [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) 扩展 [SwapEndianOrder](binary_package_interfaces.md#interface-swapendianordert) 接口，以实现将 [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) 值的字节顺序反转。

父类型：

- [SwapEndianOrder](#interface-swapendianordert)\<[UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)>

#### func swapBytes()

```cangjie
public func swapBytes(): UInt8
```

功能：反转 [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8)  值的字节顺序。

返回值：

- [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) - [UInt8](../../core/core_package_api/core_package_intrinsics.md#uint8) 值。

示例：

<!-- run -->
```cangjie
import std.binary.*
import std.unittest.*
import std.unittest.testmacro.*

main() {
    let n = 0x12u8
    let m = n.swapBytes()
    @Assert(m, 0x12)
}
```
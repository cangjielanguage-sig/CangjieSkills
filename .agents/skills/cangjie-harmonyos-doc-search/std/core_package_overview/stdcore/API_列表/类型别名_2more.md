### 类型别名

|  类型别名 | 功能  |
| ------------ | ------------ |
| [Byte](./core_package_api/core_package_types.md#type-byte) | `Byte` 类型是内置类型 `UInt8` 的别名。 |
| [Int](./core_package_api/core_package_types.md#type-int) | `Int` 类型是内置类型 `Int64` 的别名。 |
| [UInt](./core_package_api/core_package_types.md#type-uint) | `UInt` 类型是内置类型 `UInt64` 的别名。 |

### 内置类型

|  内置类型名 | 功能  |
| ------------ | ------------ |
| [Int8](./core_package_api/core_package_intrinsics.md#int8) | 表示 8 位有符号整型，表示范围为 [-2^7, 2^7 - 1]。 |
| [Int16](./core_package_api/core_package_intrinsics.md#int16) | 表示 16 位有符号整型，表示范围为 [-2^{15}, 2^{15} - 1]。 |
| [Int32](./core_package_api/core_package_intrinsics.md#int32) | 表示 32 位有符号整型，表示范围为 [-2^{31}, 2^{31} - 1]。 |
| [Int64](./core_package_api/core_package_intrinsics.md#int64) | 表示 64 位有符号整型，表示范围为 [-2^{63}, 2^{63} - 1]。 |
| [IntNative](./core_package_api/core_package_intrinsics.md#intnative) | 表示平台相关的有符号整型，其长度与当前系统的位宽一致。 |
| [UInt8](./core_package_api/core_package_intrinsics.md#uint8) | 表示 8 位无符号整型，表示范围为 [0 ~ 2^8 - 1]。 |
| [UInt16](./core_package_api/core_package_intrinsics.md#uint16) | 表示 16 位无符号整型，表示范围为 [0 ~ 2^{16} - 1]。 |
| [UInt32](./core_package_api/core_package_intrinsics.md#uint32) | 表示 32 位无符号整型，表示范围为 [0 ~ 2^{32} - 1]。 |
| [UInt64](./core_package_api/core_package_intrinsics.md#uint64) | 表示 64 位无符号整型，表示范围为 [0 ~ 2^{64} - 1]。 |
| [UIntNative](./core_package_api/core_package_intrinsics.md#uintnative) | 表示平台相关的无符号整型，其长度与当前系统的位宽一致。 |
| [Float16](./core_package_api/core_package_intrinsics.md#float16) | 表示 16 位浮点数，符合 `IEEE 754` 中的半精度格式（`binary16`）。 |
| [Float32](./core_package_api/core_package_intrinsics.md#float32) | 表示 32 位浮点数，符合 `IEEE 754` 中的单精度格式（`binary32`）。 |
| [Float64](./core_package_api/core_package_intrinsics.md#float64) | 表示 64 位浮点数，符合 `IEEE 754` 中的双精度格式（`binary64`）。 |
| [Bool](./core_package_api/core_package_intrinsics.md#bool) | 表示布尔类型，有 `true` 和 `false` 两种取值。 |
| [Rune](./core_package_api/core_package_intrinsics.md#rune) | 表示 unicode 字符集中的字符。 |
| [Unit](./core_package_api/core_package_intrinsics.md#unit) | 表示仓颉语言中只关心副作用而不关心值的表达式的类型。 |
| [CPointer\<T>](./core_package_api/core_package_intrinsics.md#cpointert) | 表示 `T` 类型实例的指针，在与 C 语言互操作的场景下使用，对应 C 语言的 `T*`。 |
| [CString](./core_package_api/core_package_intrinsics.md#cstring) | 表示 C 风格字符串，在与 C 语言互操作的场景下使用。 |
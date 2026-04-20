## CPointer\<T>

功能：表示 `T` 类型实例的指针，在与 C 语言互操作的场景下使用，对应 C 语言的 `T*`。

其中 `T` 必须满足 [CType](core_package_interfaces.md#interface-ctype) 约束。

[CPointer](core_package_intrinsics.md#cpointert) 类型必须满足：

- 大小和对齐与平台相关。
- 对它做加减法算术运算、读写内存，是需要在 unsafe 上下文操作的。
- [CPointer](core_package_intrinsics.md#cpointert)\<T1> 可以在 unsafe 上下文中使用类型强制转换，变成 [CPointer](core_package_intrinsics.md#cpointert)\<T2> 类型。
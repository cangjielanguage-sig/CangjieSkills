## CString

功能：表示 C 风格字符串，在与 C 语言互操作的场景下使用。

可以通过 [CString](core_package_intrinsics.md#cstring) 的构造函数或 [LibC](core_package_structs.md#struct-libc) 的 `mallocCString` 创建 C 风格字符串，如需在仓颉端释放，则调用 [LibC](core_package_structs.md#struct-libc) 的 free 方法。
### static func withNativeData(CPointer\<UInt8>, Int64)

```cangjie
public static unsafe func withNativeData(data: CPointer<UInt8>, length: Int64): FuzzDataProvider
```

功能：使用 C 指针数据生成 [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) 类型实例。

参数：

- data: CPointer\<UInt8> - 输入的外部数据。
- length: Int64 - 数据长度。

返回值：

- [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) - 构造的 [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) 类型实例。
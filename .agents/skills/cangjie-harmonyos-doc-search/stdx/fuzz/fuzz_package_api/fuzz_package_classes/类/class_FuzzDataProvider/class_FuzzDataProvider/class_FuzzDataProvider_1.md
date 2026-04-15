## class FuzzDataProvider

```cangjie
public open class FuzzDataProvider {
    public let data: Array<UInt8>
    public var remainingBytes: Int64
    public var offset: Int64
}
```

功能：[FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) 是一个工具类，目的是将变异数据的字节流转化为标准的仓颉基本数据。

当前支持的数据结构如下：
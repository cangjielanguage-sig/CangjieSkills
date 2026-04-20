### sizeOf/alignOf

仓颉还提供了 `sizeOf` 和 `alignOf` 两个函数，用于获取上述 C 互操作类型的内存占用和内存对齐数值（单位：字节），函数声明如下：

```cangjie
public func sizeOf<T>(): UIntNative where T <: CType
public func alignOf<T>(): UIntNative where T <: CType
```

使用示例：

<!-- run -->

```cangjie
@C
struct Data {
    var a: Int64 = 0
    var b: Float32 = 0.0
}

main() {
    println(sizeOf<Data>())
    println(alignOf<Data>())
}
```

在 64 位机器上运行，将输出：

```text
16
8
```
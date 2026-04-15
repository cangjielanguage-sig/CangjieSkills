## class FuzzerBuilder

```cangjie
public class FuzzerBuilder {
    public init(targetFunction: (Array<UInt8>) -> Int32)
    public init(targetFunction: (FuzzDataProvider) -> Int32)
}
```

功能：此类用于 [Fuzzer](fuzz_package_classes.md#class-fuzzer) 类的构建。

### init((Array\<UInt8>) -> Int32)

```cangjie
public init(targetFunction: (Array<UInt8>) -> Int32)
```

功能：根据以 UInt8 数组为参数，以 Int32 为返回值的目标函数，创建 [FuzzerBuilder](fuzz_package_classes.md#class-fuzzerbuilder) 实例。

参数：

- targetFunction: (Array\<UInt8>) ->Int32 - 以 UInt8 数组为参数，以 Int32 为返回值的目标函数。

### init((FuzzDataProvider) -> Int32)

```cangjie
public init(targetFunction: (FuzzDataProvider) -> Int32)
```

功能：根据以 [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) 为参数，以 Int32 为返回值的目标函数，创建 [FuzzerBuilder](fuzz_package_classes.md#class-fuzzerbuilder) 实例。

参数：

- targetFunction: ([FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider)) ->Int32 - 以 [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) 为参数，以 Int32 为返回值的目标函数。

### func build()

```cangjie
public func build(): Fuzzer
```

功能：生成一个 [Fuzzer](fuzz_package_classes.md#class-fuzzer) 实例。

返回值：

- [Fuzzer](fuzz_package_classes.md#class-fuzzer) - [Fuzzer](fuzz_package_classes.md#class-fuzzer) 实例。

### func setArgs(Array\<String>)

```cangjie
public func setArgs(args: Array<String>): FuzzerBuilder
```

功能：设置 Fuzz 运行参数。

参数：

- args: Array\<String> - Fuzz 运行参数。

返回值：

- [FuzzerBuilder](fuzz_package_classes.md#class-fuzzerbuilder) - 当前 [FuzzerBuilder](fuzz_package_classes.md#class-fuzzerbuilder) 实例。

### func setTargetFunction((Array\<UInt8>) -> Int32)

```cangjie
public func setTargetFunction(targetFunction: (Array<UInt8>) -> Int32): FuzzerBuilder
```

功能：设置 Fuzz 目标函数。

参数：

- targetFunction: (Array\<UInt8>) ->Int32 - 以 UInt8 数组为参数，以 Int32 为返回值的目标函数。

返回值：

- [FuzzerBuilder](fuzz_package_classes.md#class-fuzzerbuilder) - 当前 [FuzzerBuilder](fuzz_package_classes.md#class-fuzzerbuilder) 实例。

### func setTargetFunction((FuzzDataProvider) -> Int32)

```cangjie
public func setTargetFunction(targetFunction: (FuzzDataProvider) -> Int32): FuzzerBuilder
```

功能：设置 Fuzz 目标函数。

参数：

- targetFunction: ([FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider)) ->Int32 - 以 [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) 为参数，以 Int32 为返回值的目标函数。

返回值：

- [FuzzerBuilder](fuzz_package_classes.md#class-fuzzerbuilder) - 当前 [FuzzerBuilder](fuzz_package_classes.md#class-fuzzerbuilder) 实例。
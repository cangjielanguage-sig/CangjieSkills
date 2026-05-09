## class Fuzzer

```cangjie
public class Fuzzer {
    public init(targetFunction: (Array<UInt8>) -> Int32)
    public init(targetFunction: (Array<UInt8>) -> Int32, args: Array<String>)
    public init(targetFunction: (FuzzDataProvider) -> Int32)
    public init(targetFunction: (FuzzDataProvider) -> Int32, args: Array<String>)
}
```

功能：[Fuzzer](fuzz_package_classes.md#class-fuzzer) 类提供了 fuzz 工具的创建。用户提供需要进行 fuzz 测试的函数 `targetFunction`，以及设置特定的 fuzz 运行参数 `args` 比如 fuzz 执行次数、初始种子、生成数据最大长度等，可创建相应类型的 [Fuzzer](fuzz_package_classes.md#class-fuzzer)。

### init((Array\<UInt8>) -> Int32)

```cangjie
public init(targetFunction: (Array<UInt8>) -> Int32)
```

功能：根据以 UInt8 数组为参数，以 Int32 为返回值的目标函数，创建 [Fuzzer](fuzz_package_classes.md#class-fuzzer) 实例。

参数：

- targetFunction: (Array\<UInt8>) ->Int32 - 以 UInt8 数组为参数，以 Int32 为返回值的目标函数。

### init((Array\<UInt8>) -> Int32, Array\<String>)

```cangjie
public init(targetFunction: (Array<UInt8>) -> Int32, args: Array<String>)
```

功能：根据以 UInt8 数组为参数，以 Int32 为返回值的目标函数，以及 Fuzz 运行参数，创建 [Fuzzer](fuzz_package_classes.md#class-fuzzer) 实例。

参数：

- targetFunction: (Array\<UInt8>) ->Int32 - 以 UInt8 数组为参数，以 Int32 为返回值的目标函数。
- args: Array\<String> - Fuzz 运行参数。

### init((FuzzDataProvider) -> Int32)

```cangjie
public init(targetFunction: (FuzzDataProvider) -> Int32)
```

功能：根据以 [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) 为参数，以 Int32 为返回值的目标函数，创建 [Fuzzer](fuzz_package_classes.md#class-fuzzer) 实例。

参数：

- targetFunction: ([FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider)) ->Int32 - 以 [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) 为参数，以 Int32 为返回值的目标函数。

### init((FuzzDataProvider) -> Int32, Array\<String>)

```cangjie
public init(targetFunction: (FuzzDataProvider) -> Int32, args: Array<String>)
```

功能：根据以 [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) 为参数，以 Int32 为返回值的目标函数，以及 Fuzz 运行参数，创建 [Fuzzer](fuzz_package_classes.md#class-fuzzer) 实例。

参数：

- targetFunction: ([FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider)) ->Int32 - 以 [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) 为参数，以 Int32 为返回值的目标函数。
- args: Array\<String> - Fuzz 运行参数。

### func disableDebugDataProvider()

```cangjie
public func disableDebugDataProvider(): Unit
```

功能：关闭调试信息打印功能，当 [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider).consumeXXX 被调用时，返回值将不被打印到 `stdout`。

### func disableFakeCoverage()

```cangjie
public func disableFakeCoverage(): Unit
```

功能：关闭调用 `enableFakeCoverage` 对 Fuzz 的影响。

### func enableDebugDataProvider()

```cangjie
public func enableDebugDataProvider(): Unit
```

功能：启用调试信息打印功能，当 [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider).consumeXXX 被调用时，返回值将被打印到 `stdout`。该功能默认为关闭。

### func enableFakeCoverage()

```cangjie
public func enableFakeCoverage(): Unit
```

功能：创建一块虚假的覆盖率反馈区域，保持 Fuzz 持续进行。在 [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) 模式下，前几轮运行时可能由于数据不足而导致没有覆盖率，libfuzzer 会退出。该功能默认为关闭。

### func getArgs()

```cangjie
public func getArgs(): Array<String>
```

功能：获取 Fuzz 运行参数。

返回值：

- Array\<String> - 当前 Fuzz 运行参数。
### func setArgs(Array\<String>)

```cangjie
public func setArgs(args: Array<String>): Unit
```

功能：设置 Fuzz 运行参数。

参数：

- args: Array\<String> - Fuzz 运行参数。

### func setTargetFunction((Array\<UInt8>) -> Int32)

```cangjie
public func setTargetFunction(targetFunction: (Array<UInt8>) -> Int32): Unit
```

功能：设置 Fuzz 目标函数。

参数：

- targetFunction: (Array\<UInt8>) ->Int32 - 以 UInt8 数组为参数，以 Int32 为返回值的目标函数。

### func setTargetFunction((FuzzDataProvider) -> Int32)

```cangjie
public func setTargetFunction(targetFunction: (FuzzDataProvider) -> Int32): Unit
```

功能：设置 Fuzz 目标函数。

参数：

- targetFunction: ([FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider)) ->Int32 - 以 [FuzzDataProvider](fuzz_package_classes.md#class-fuzzdataprovider) 为参数，以 Int32 为返回值的目标函数。

### func startFuzz()

```cangjie
public func startFuzz(): Unit
```

功能：执行 Fuzz。
## struct BatchInputProvider\<T>

```cangjie
public struct BatchInputProvider<T> <: BenchInputProvider<T> {
    public BatchInputProvider(let builder: () -> T)
}
```

功能：输入提供程序，在执行之前在缓冲区中生成整个基准批次的输入。

父类型：

- [BenchInputProvider](unittest_package_interfaces.md#interface-benchinputprovider)\<T>

### BatchInputProvider(() -> T)

```cangjie
public BatchInputProvider(let builder: () -> T)
```

功能：BatchInputProvider 构造函数。

参数：

- builder: () -> T - 用于生成基准测试输入的闭包。

### func get(Int64)

```cangjie
public mut func get(idx: Int64): T
```

功能：获取元素，该函数的执行时间包含在基准测量中，然后作为框架开销计算的一部分从结果中排除。

参数：

- idx: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 元素索引值。

返回值：

- T - 元素值。

### func reset(Int64)

```cangjie
public mut func reset(max: Int64)
```

功能：在基准测量之前调用。调用此函数后，后续的 `get(i)` 调用必须成功获取 [0, max) 中的 `i` 。

参数：

- max: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 最大值。

## struct BatchSizeOneInputProvider\<T>

```cangjie
public struct BatchSizeOneInputProvider<T> <: BenchInputProvider<T>{
    public BatchSizeOneInputProvider(let builder: () -> T)
}
```

功能：基准输入提供程序，在每次执行基准之前生成输入。
与 `GenerateEachInputProvider` 的区别在于，当批量大小为 1 时，我们可以测量。
每个基准测试调用都是独立的，因此输入生成永远不会包含在测量中。
如果 `GenerateEachInputProvider` 给出的结果质量较差，则应使用。 这种情况可能会发生，因为生成输入所需的时间比实际基准要多得多，或者如果输入生成的执行时间非常不稳定。

父类型：

- [BenchInputProvider](unittest_package_interfaces.md#interface-benchinputprovider)\<T>

### BatchSizeOneInputProvider(() -> T)

```cangjie
public BatchSizeOneInputProvider(let builder: () -> T)
```

功能：BatchSizeOneInputProvider 构造函数。

参数：

- builder: () -> T - 用于生成基准测试输入的 lambda 。

### func get(Int64)

```cangjie
public mut func get(idx: Int64): T
```

功能：获取元素，该函数的执行时间包含在基准测量中，然后作为框架开销计算的一部分从结果中排除。

参数：

- idx: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 元素索引值。

返回值：

- T - 元素值。

### func reset(Int64)

```cangjie
public mut func reset(max: Int64)
```

功能：在基准测量之前调用。调用此函数后，后续的 `get(i)` 调用必须成功获取 [0, max) 中的 `i` 。

参数：

- max: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 最大值。
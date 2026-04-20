## struct ImmutableInputProvider\<T>

```cangjie
public struct ImmutableInputProvider<T> <: BenchInputProvider<T> {
    public ImmutableInputProvider(let data: T)
}
```

功能：最简单的输入提供程序，只需为基准测试的每次调用复制数据。适用于基准测试不会改变输入的情况。它在框架内默认使用。

父类型：

- [BenchInputProvider](unittest_package_interfaces.md#interface-benchinputprovider)\<T>

### ImmutableInputProvider(T)

```cangjie
public ImmutableInputProvider(let data: T)
```

功能：ImmutableInputProvider 构造函数。

参数：

- data: T - 基准测试的输入。

### func get(Int64)

```cangjie
public mut func get(idx: Int64): T
```

功能：获取元素，该函数的执行时间包含在基准测量中，然后作为框架开销计算的一部分从结果中排除。

参数：

- idx: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 元素索引值。

返回值：

- T - 元素值。

### static func createOrExisting(T, Int64)

```cangjie
public static func createOrExisting(arg: T, x!:Int64=0): ImmutableInputProvider<T>
```

功能：创建或获取一个 ImmutableInputProvider 对象。

参数：

- arg: T - 提供器需复制的参数。
- x!: [Int64](../../core/core_package_api/core_package_intrinsics.md#int64) - 为实现重载而增加的参数。

返回值：

- ImmutableInputProvider\<T> - 输入提供器。

### static func createOrExisting\<U>(U)

```cangjie
public static func createOrExisting<U>(arg: U): U where U <: BenchInputProvider<T>
```

功能：创建或获取一个 BenchInputProvider 的子类型对象。

参数：

- arg: T - 提供器需复制的参数。

返回值：

- U - 输入提供器。

## struct KeyBaseline

```cangjie
public struct KeyBaseline <: KeyFor<String> {}
```

功能：用于在 [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) 中作为对应配置项的键值。

例如：

<!-- compile -->
```cangjie
let conf = Configuration()
conf.set(KeyBaseline.baseline, "baseline")
```

父类型：

- [KeyFor](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-keyfor)

### prop baseline

```cangjie
public static prop baseline: Baseline
```

功能：配置项的键值。

### prop name

```cangjie
public prop name: String
```

功能：配置项的键值的名称。

## struct KeyBaselinePath

```cangjie
public struct KeyBaselinePath <: KeyFor<String> {}
```

功能：用于在 [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) 中作为对应配置项的键值。

父类型：

- [KeyFor](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-keyfor)

### prop baselinePath

```cangjie
public static prop baselinePath: BaselinePath
```

功能：配置项的键值。

### prop name

```cangjie
public prop name: String
```

功能：配置项的键值的名称。

## struct KeyBatchSize

```cangjie
public struct KeyBatchSize <: KeyFor<Int64> & KeyFor<Range<Int64>> {}
```

功能：用于在 [Configuration](../../unittest_common/unittest_common_package_api/unittest_common_package_classes.md#class-configuration) 中作为对应配置项的键值。

父类型：

- [KeyFor](../../unittest_common/unittest_common_package_api/unittest_common_package_interfaces.md#interface-keyfor)

### prop batchSize

```cangjie
public static prop batchSize: BatchSize
```

功能：配置项的键值。

### prop name

```cangjie
public prop name: String
```

功能：配置项的键值的名称。
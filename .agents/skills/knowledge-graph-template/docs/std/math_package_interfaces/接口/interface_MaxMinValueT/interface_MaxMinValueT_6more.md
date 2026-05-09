## interface MaxMinValue\<T>

```cangjie
public interface MaxMinValue<T> {
    static func getMax(): T
    static func getMin(): T
}
```

功能：提供获取最大值和最小值的方法。

### static func getMax()

```cangjie
static func getMax(): T
```

功能：获取最大值。

返回值：

- T - 最大值。

### static func getMin()

```cangjie
static func getMin(): T
```

功能：获取最小值。

返回值：

- T - 最小值。

### extend Float16 <: MaxMinValue\<Float16>

```cangjie
extend Float16 <: MaxMinValue<Float16>
```

功能：为 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 类型扩展 [MaxMinValue](#interface-maxminvaluet) 接口。

父类型：

- [MaxMinValue](#interface-maxminvaluet)\<[Float16](../../core/core_package_api/core_package_intrinsics.md#float16)>

#### static func getMax()

```cangjie
public static func getMax(): Float16
```

功能：获取 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 类型的最大值。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 半精度浮点数类型的最大值。

#### static func getMin()

```cangjie
public static func getMin(): Float16
```

功能：获取 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 类型的最小值。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 半精度浮点数类型的最小值。

### extend Float32 <: MaxMinValue\<Float32>

```cangjie
extend Float32 <: MaxMinValue<Float32>
```

功能：为 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型扩展 [MaxMinValue](#interface-maxminvaluet) 接口。

父类型：

- [MaxMinValue](#interface-maxminvaluet)\<[Float32](../../core/core_package_api/core_package_intrinsics.md#float32)>

#### static func getMax()

```cangjie
public static func getMax(): Float32
```

功能：获取 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型的最大值。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 单精度浮点数类型的最大值。

#### static func getMin()

```cangjie
public static func getMin(): Float32
```

功能：获取 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 类型的最小值。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 单精度浮点数类型的最小值。

### extend Float64 <: MaxMinValue\<Float64>

```cangjie
extend Float64 <: MaxMinValue<Float64>
```

功能：为 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型扩展 [MaxMinValue](#interface-maxminvaluet) 接口。

父类型：

- [MaxMinValue](#interface-maxminvaluet)\<[Float64](../../core/core_package_api/core_package_intrinsics.md#float64)>

#### static func getMax()

```cangjie
public static func getMax(): Float64
```

功能：获取 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型的最大值。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 双精度浮点数类型的最大值。

#### static func getMin()

```cangjie
public static func getMin(): Float64
```

功能：获取 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 类型的最小值。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 双精度浮点数类型的最小值。
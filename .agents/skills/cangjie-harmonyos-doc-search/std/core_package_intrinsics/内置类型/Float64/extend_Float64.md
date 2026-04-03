### extend Float64

```cangjie
extend Float64
```

功能：拓展双精度浮点数以支持一些数学常数。

#### static prop Inf

```cangjie
public static prop Inf: Float64
```

功能：获取双精度浮点数的无穷数。

类型：[Float64](./core_package_intrinsics.md#float64)

#### static prop Max

```cangjie
public static prop Max: Float64
```

功能：获取双精度浮点数的最大值。

类型：[Float64](./core_package_intrinsics.md#float64)

#### static prop Min

```cangjie
public static prop Min: Float64
```

功能：获取双精度浮点数的最小值。

类型：[Float64](./core_package_intrinsics.md#float64)

#### static prop MinDenormal

```cangjie
public static prop MinDenormal: Float64
```

功能：获取双精度浮点数的最小次正规数。

类型：[Float64](./core_package_intrinsics.md#float64)

#### static prop MinNormal

```cangjie
public static prop MinNormal: Float64
```

功能：获取双精度浮点数的最小正规数。

类型：[Float64](./core_package_intrinsics.md#float64)

#### static prop NaN

```cangjie
public static prop NaN: Float64
```

功能：获取双精度浮点数的非数。

类型：[Float64](./core_package_intrinsics.md#float64)

#### static func max(Float64, Float64, Array\<Float64>)

```cangjie
public static func max(a: Float64, b: Float64, others: Array<Float64>): Float64
```

功能：返回一组[Float64](./core_package_intrinsics.md#float64)中的最大值，此函数的第三个参数是一个变长参数，可以获取二个以上的[Float64](./core_package_intrinsics.md#float64)最大值，如果参数中有 `NaN`，该函数会返回 `NaN`。

参数：

- a: [Float64](./core_package_intrinsics.md#float64) - 第一个待比较的数。
- b: [Float64](./core_package_intrinsics.md#float64) - 第二个待比较的数。
- others: [Array](core_package_structs.md#struct-arrayt)\<[Float64](./core_package_intrinsics.md#float64)> - 其他待比较的数。

返回值：

- [Float64](./core_package_intrinsics.md#float64) - 返回参数中的最大值。

#### static func min(Float64, Float64, Array\<Float64>)

```cangjie
public static func min(a: Float64, b: Float64, others: Array<Float64>): Float64
```

功能：返回一组[Float64](./core_package_intrinsics.md#float64)中的最小值，此函数的第三个参数是一个变长参数，可以获取二个以上的[Float64](./core_package_intrinsics.md#float64)最小值，如果参数中有 `NaN`，该函数会返回 `NaN`。

参数：

- a: [Float64](./core_package_intrinsics.md#float64) - 第一个待比较的数。
- b: [Float64](./core_package_intrinsics.md#float64) - 第二个待比较的数。
- others: [Array](core_package_structs.md#struct-arrayt)\<[Float64](./core_package_intrinsics.md#float64)> - 其他待比较的数。

返回值：

- [Float64](./core_package_intrinsics.md#float64) - 返回参数中的最小值。

#### func isInf()

```cangjie
public func isInf(): Bool
```

功能：判断某个浮点数 [Float64](./core_package_intrinsics.md#float64) 是否为无穷数值。

返回值：

- [Bool](./core_package_intrinsics.md#bool) - 如果 [Float64](./core_package_intrinsics.md#float64) 的值正无穷大或负无穷大，则返回 `true`；否则，返回 `false`。

#### func isNaN()

```cangjie
public func isNaN(): Bool
```

功能：判断某个浮点数 [Float64](./core_package_intrinsics.md#float64) 是否为非数值。

返回值：

- [Bool](./core_package_intrinsics.md#bool) - 如果 [Float64](./core_package_intrinsics.md#float64) 的值为非数值，则返回 `true`；否则，返回 `false`。

#### func isNormal()

```cangjie
public func isNormal(): Bool
```

功能：判断某个浮点数 [Float64](./core_package_intrinsics.md#float64) 是否为常规数值。

返回值：

- [Bool](./core_package_intrinsics.md#bool) - 如果 [Float64](./core_package_intrinsics.md#float64) 的值是正常的浮点数，返回 `true`；否则，返回 `false`。
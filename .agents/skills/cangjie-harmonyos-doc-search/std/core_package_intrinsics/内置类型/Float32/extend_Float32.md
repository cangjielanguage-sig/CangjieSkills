### extend Float32

```cangjie
extend Float32
```

功能：拓展单精度浮点数以支持一些数学常数。

#### static prop Inf

```cangjie
public static prop Inf: Float32
```

功能：获取单精度浮点数的无穷数。

类型：[Float32](./core_package_intrinsics.md#float32)

#### static prop Max

```cangjie
public static prop Max: Float32
```

功能：获取单精度浮点数的最大值。

类型：[Float32](./core_package_intrinsics.md#float32)

#### static prop Min

```cangjie
public static prop Min: Float32
```

功能：获取单精度浮点数的最小值。

类型：[Float32](./core_package_intrinsics.md#float32)

#### static prop MinDenormal

```cangjie
public static prop MinDenormal: Float32
```

功能：获取单精度浮点数的最小次正规数。

类型：[Float32](./core_package_intrinsics.md#float32)

#### static prop MinNormal

```cangjie
public static prop MinNormal: Float32
```

功能：获取单精度浮点数的最小正规数。

类型：[Float32](./core_package_intrinsics.md#float32)

#### static prop NaN

```cangjie
public static prop NaN: Float32
```

功能：获取单精度浮点数的非数。

类型：[Float32](./core_package_intrinsics.md#float32)

#### static func max(Float32, Float32, Array\<Float32>)

```cangjie
public static func max(a: Float32, b: Float32, others: Array<Float32>): Float32
```

功能：返回一组[Float32](./core_package_intrinsics.md#float32)中的最大值，此函数的第三个参数是一个变长参数，可以获取二个以上的[Float32](./core_package_intrinsics.md#float32)最大值，如果参数中有 `NaN`，该函数会返回 `NaN`。

参数：

- a: [Float32](./core_package_intrinsics.md#float32) - 第一个待比较的数。
- b: [Float32](./core_package_intrinsics.md#float32) - 第二个待比较的数。
- others: [Array](core_package_structs.md#struct-arrayt)\<[Float32](./core_package_intrinsics.md#float32)> - 其他待比较的数。

返回值：

- [Float32](./core_package_intrinsics.md#float32) - 返回参数中的最大值。

#### static func min(Float32, Float32, Array\<Float32>)

```cangjie
public static func min(a: Float32, b: Float32, others: Array<Float32>): Float32
```

功能：返回一组[Float32](./core_package_intrinsics.md#float32)中的最小值，此函数的第三个参数是一个变长参数，可以获取二个以上的[Float32](./core_package_intrinsics.md#float32)最小值，如果参数中有 `NaN`，该函数会返回 `NaN`。

参数：

- a: [Float32](./core_package_intrinsics.md#float32) - 第一个待比较的数。
- b: [Float32](./core_package_intrinsics.md#float32) - 第二个待比较的数。
- others: [Array](core_package_structs.md#struct-arrayt)\<[Float32](./core_package_intrinsics.md#float32)> - 其他待比较的数。

返回值：

- [Float32](./core_package_intrinsics.md#float32) - 返回参数中的最小值。

#### func isInf()

```cangjie
public func isInf(): Bool
```

功能：判断某个浮点数 [Float32](./core_package_intrinsics.md#float32) 是否为无穷数值。

返回值：

- [Bool](./core_package_intrinsics.md#bool) - 如果 [Float32](./core_package_intrinsics.md#float32) 的值正无穷大或负无穷大，则返回 `true`；否则，返回 `false`。

#### func isNaN()

```cangjie
public func isNaN(): Bool
```

功能：判断某个浮点数 [Float32](./core_package_intrinsics.md#float32) 是否为非数值。

返回值：

- [Bool](./core_package_intrinsics.md#bool) - 如果 [Float32](./core_package_intrinsics.md#float32) 的值为非数值，则返回 `true`；否则，返回 `false`。

#### func isNormal()

```cangjie
public func isNormal(): Bool
```

功能：判断某个浮点数 [Float32](./core_package_intrinsics.md#float32) 是否为常规数值。

返回值：

- [Bool](./core_package_intrinsics.md#bool) - 如果 [Float32](./core_package_intrinsics.md#float32) 的值是正常的浮点数，返回 `true`；否则，返回 `false`。
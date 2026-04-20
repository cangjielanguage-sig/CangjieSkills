### extend Float16

```cangjie
extend Float16
```

功能：拓展半精度浮点数以支持一些数学常数。

#### static prop Inf

```cangjie
public static prop Inf: Float16
```

功能：获取半精度浮点数的无穷数。

类型：[Float16](./core_package_intrinsics.md#float16)

#### static prop Max

```cangjie
public static prop Max: Float16
```

功能：获取半精度浮点数的最大值。

类型：[Float16](./core_package_intrinsics.md#float16)

#### static prop Min

```cangjie
public static prop Min: Float16
```

功能：获取半精度浮点数的最小值。

类型：[Float16](./core_package_intrinsics.md#float16)

#### static prop MinDenormal

```cangjie
public static prop MinDenormal: Float16
```

功能：获取半精度浮点数的最小次正规数。最小的正的次正规数是以 IEEE 双精度格式表示的最小正数。

类型：[Float16](./core_package_intrinsics.md#float16)

#### static prop MinNormal

```cangjie
public static prop MinNormal: Float16
```

功能：获取半精度浮点数的最小正规数。

类型：[Float16](./core_package_intrinsics.md#float16)

#### static prop NaN

```cangjie
public static prop NaN: Float16
```

功能：获取半精度浮点数的非数。

类型：[Float16](./core_package_intrinsics.md#float16)

#### static func max(Float16, Float16, Array\<Float16>)

```cangjie
public static func max(a: Float16, b: Float16, others: Array<Float16>): Float16
```

功能：返回一组[Float16](./core_package_intrinsics.md#float16)中的最大值，此函数的第三个参数是一个变长参数，可以获取二个以上的[Float16](./core_package_intrinsics.md#float16)最大值，如果参数中有 `NaN`，该函数会返回 `NaN`。

参数：

- a: [Float16](./core_package_intrinsics.md#float16) - 第一个待比较的数。
- b: [Float16](./core_package_intrinsics.md#float16) - 第二个待比较的数。
- others: [Array](core_package_structs.md#struct-arrayt)\<[Float16](./core_package_intrinsics.md#float16)> - 其他待比较的数。

返回值：

- [Float16](./core_package_intrinsics.md#float16) - 返回参数中的最大值。

#### static func min(Float16, Float16, Array\<Float16>)

```cangjie
public static func min(a: Float16, b: Float16, others: Array<Float16>): Float16
```

功能：返回一组[Float16](./core_package_intrinsics.md#float16)中的最小值，此函数的第三个参数是一个变长参数，可以获取二个以上的[Float16](./core_package_intrinsics.md#float16)最小值，如果参数中有 `NaN`，该函数会返回 `NaN`。

参数：

- a: [Float16](./core_package_intrinsics.md#float16) - 第一个待比较的数。
- b: [Float16](./core_package_intrinsics.md#float16) - 第一个待比较的数。
- others: [Array](core_package_structs.md#struct-arrayt)\<[Float16](./core_package_intrinsics.md#float16)> - 其他待比较的数。

返回值：

- [Float16](./core_package_intrinsics.md#float16) - 返回参数中的最小值。

#### func isInf()

```cangjie
public func isInf(): Bool
```

功能：判断某个浮点数 [Float16](./core_package_intrinsics.md#float16) 是否为无穷数值。

返回值：

- [Bool](./core_package_intrinsics.md#bool) - 如果 [Float16](./core_package_intrinsics.md#float16) 的值正无穷大或负无穷大，则返回 `true`；否则，返回 `false`。

#### func isNaN()

```cangjie
public func isNaN(): Bool
```

功能：判断某个浮点数 [Float16](./core_package_intrinsics.md#float16) 是否为非数值。

返回值：

- [Bool](./core_package_intrinsics.md#bool) - 如果 [Float16](./core_package_intrinsics.md#float16) 的值为非数值，则返回 `true`；否则，返回 `false`。
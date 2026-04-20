### extend Float32 <: NearEquatable\<Float32, RelativeDelta\<Float32>>

功能：对类型 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 扩展接口 [NearEquatable](#interface-nearequatablect-d)，且使用 [RelativeDelta](../unittest_package_api/unittest_package_structs.md#struct-relativedeltat) 做近似计算。

#### func isNear(Float32, RelativeDelta\<Float32>)

```cangjie
public func isNear(obj: Float32, delta!: RelativeDelta<Float32>): Bool
```

功能：判断某个对象是否基于这个 delta 近似相等。

参数：

- obj: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 被比较的对象。
- delta!: [RelativeDelta](../unittest_package_api/unittest_package_structs.md#struct-relativedeltat)\<[Float32](../../core/core_package_api/core_package_intrinsics.md#float32)> - 判断近似相等的 delta。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否近似相等。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - delta 值不能为负数，且不是 NaN，否则将抛出该异常。

### extend Float64 <: NearEquatable\<Float64, Float64>

功能：对类型 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 扩展接口 [NearEquatable](#interface-nearequatablect-d)。

#### func isNear(Float64, Float64)

```cangjie
public func isNear(obj: Float64, delta!: Float64): Bool
```

功能：判断某个对象是否基于这个 delta 近似相等。

参数：

- obj: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 被比较的对象。
- delta!: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 判断近似相等的 delta。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否近似相等。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - delta 值不能为负数，且不是 NaN，否则将抛出该异常。

### extend Float64 <: NearEquatable\<Float64, RelativeDelta\<Float64>>

功能：对类型 [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) 扩展接口 [NearEquatable](#interface-nearequatablect-d)，且使用 [RelativeDelta](../unittest_package_api/unittest_package_structs.md#struct-relativedeltat) 做近似计算。

#### func isNear(Float64, RelativeDelta\<Float64>)

```cangjie
public func isNear(obj: Float64, delta!: RelativeDelta<Float64>): Bool
```

功能：判断某个对象是否基于这个 delta 近似相等。

参数：

- obj: [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 被比较的对象。
- delta!: [RelativeDelta](../unittest_package_api/unittest_package_structs.md#struct-relativedeltat)\<[Float64](../../core/core_package_api/core_package_intrinsics.md#float64)> - 判断近似相等的 delta。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否近似相等。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - delta 值不能为负数，且不是 NaN，否则将抛出该异常。
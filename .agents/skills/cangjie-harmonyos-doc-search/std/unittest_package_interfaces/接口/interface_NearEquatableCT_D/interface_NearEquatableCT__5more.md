## interface NearEquatable\<CT, D>

```cangjie
public interface NearEquatable<CT, D> {
    func isNear(obj: CT, delta!: D): Bool
} 
```

功能：判断某个对象是否基于这个 delta 近似相等。

### func isNear(CT, D)

```cangjie
public func isNear(obj: CT, delta!: D): Bool
```

功能：判断某个对象是否基于这个 delta 近似相等。

参数：

- obj: CT - 被比较的对象。
- delta!: D - 判断近似相等的 delta。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否近似相等。

### extend Float16 <: NearEquatable\<Float16, Float16>

功能：对类型 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 扩展接口 [NearEquatable](#interface-nearequatablect-d)。

#### func isNear(Float16, Float16)

```cangjie
public func isNear(obj: Float16, delta!: Float16): Bool
```

功能：判断某个对象是否基于这个 delta 近似相等。

参数：

- obj: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 被比较的对象。
- delta!: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 判断近似相等的 delta。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否近似相等。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - delta 值不能为负数，且不是 NaN, 否则将抛出该异常。

### extend Float16 <: NearEquatable\<Float16, RelativeDelta\<Float16>>

功能：对类型 [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) 扩展接口 [NearEquatable](#interface-nearequatablect-d)，且使用 [RelativeDelta](../unittest_package_api/unittest_package_structs.md#struct-relativedeltat) 做近似计算。

#### func isNear(Float16, RelativeDelta\<Float16>)

```cangjie
public func isNear(obj: Float16, delta!: RelativeDelta<Float16>): Bool
```

功能：判断某个对象是否基于这个 delta 近似相等。

参数：

- obj: [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 被比较的对象。
- delta!: [RelativeDelta](../unittest_package_api/unittest_package_structs.md#struct-relativedeltat)\<[Float16](../../core/core_package_api/core_package_intrinsics.md#float16)> - 判断近似相等的 delta。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否近似相等。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - delta 值不能为负数，且不是 NaN，否则将抛出该异常。

### extend Float32 <: NearEquatable\<Float32, Float32>

功能：对类型 [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) 扩展接口 [NearEquatable](#interface-nearequatablect-d)。

#### func isNear(Float32, Float32)

```cangjie
public func isNear(obj: Float32, delta!: Float32): Bool
```

功能：判断某个对象是否基于这个 delta 近似相等。

参数：

- obj: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 被比较的对象。
- delta!: [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 判断近似相等的 delta。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否近似相等。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - delta 值不能为负数，且不是 NaN，否则将抛出该异常。
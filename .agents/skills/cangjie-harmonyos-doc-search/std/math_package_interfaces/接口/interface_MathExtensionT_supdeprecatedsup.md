## interface MathExtension\<T> <sup>(deprecated)</sup>

```cangjie
public interface MathExtension<T> {
    static func GetPI(): T
    static func GetE(): T
}
```

功能：本接口提供了统一的方法获取一些数学常数。

> **注意：**
>
> 未来版本即将废弃，使用 [FloatingPoint\<T>](#interface-floatingpointt) 替代。

### static func GetE()

```cangjie
static func GetE(): T
```

功能：获取 T 类型的自然常数。

返回值：

- T - 类型 T 的自然常数。

### static func GetPI()

```cangjie
static func GetPI(): T
```

功能：获取 T 类型的圆周率常数。

返回值：

- T - 类型 T 的圆周率常数。

### extend Float16 <: MathExtension\<Float16>

```cangjie
extend Float16 <: MathExtension<Float16>
```

功能：拓展半精度浮点数以支持一些数学常数。

父类型：

- [MathExtension <sup>(deprecated)</sup>](#interface-mathextensiont-deprecated)\<[Float16](../../core/core_package_api/core_package_intrinsics.md#float16)>

#### static func GetE()

```cangjie
public static func GetE(): Float16
```

功能：获取半精度浮点数的自然常数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 类型的自然常数

#### static func GetPI()

```cangjie
public static func GetPI(): Float16
```

功能：获取半精度浮点数的圆周率常数。

返回值：

- [Float16](../../core/core_package_api/core_package_intrinsics.md#float16) - 类型的圆周率常数

### extend Float32 <: MathExtension\<Float32>

```cangjie
extend Float32 <: MathExtension<Float32>
```

功能：拓展单精度浮点数以支持一些数学常数。

父类型：

- [MathExtension <sup>(deprecated)</sup>](#interface-mathextensiont-deprecated)\<[Float32](../../core/core_package_api/core_package_intrinsics.md#float32)>

#### static func GetE()

```cangjie
public static func GetE(): Float32
```

功能：获取单精度浮点数的自然常数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 类型的自然常数

#### static func GetPI()

```cangjie
public static func GetPI(): Float32
```

功能：获取单精度浮点数的圆周率常数。

返回值：

- [Float32](../../core/core_package_api/core_package_intrinsics.md#float32) - 类型的圆周率常数

### extend Float64 <: MathExtension\<Float64>

```cangjie
extend Float64 <: MathExtension<Float64>
```

功能：拓展双精度浮点数以支持一些数学常数。

父类型：

- [MathExtension <sup>(deprecated)</sup>](#interface-mathextensiont-deprecated)\<[Float64](../../core/core_package_api/core_package_intrinsics.md#float64)>

#### static func GetE()

```cangjie
public static func GetE(): Float64
```

功能：获取双精度浮点数的自然常数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 类型的自然常数

#### static func GetPI()

```cangjie
public static func GetPI(): Float64
```

功能：获取双精度浮点数的圆周率常数。

返回值：

- [Float64](../../core/core_package_api/core_package_intrinsics.md#float64) - 类型的圆周率常数
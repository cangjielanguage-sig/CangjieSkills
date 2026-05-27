## interface FloatingPoint\<T>

```cangjie
public interface FloatingPoint<T> <: Number<T> {
    static func getE(): T
    static func getInf(): T
    static func getPI(): T
    static func getMinDenormal(): T
    static func getMinNormal(): T
    static func getNaN(): T
    func isInf(): Bool
    func isNaN(): Bool
    func isNormal(): Bool
}
```

功能：本接口提供了浮点数相关的方法。

父类型：

- [Number](#interface-numbert)\<T>

### static func getE()

```cangjie
static func getE(): T
```

功能：获取 T 类型的自然常数。

返回值：

- T - 类型 T 的自然常数。

### static func getInf()

```cangjie
static func getInf(): T
```

功能：获取浮点数的无穷数。

返回值：

- T - 类型 T 的无穷数。

### static func getMinDenormal()

```cangjie
static func getMinDenormal(): T
```

功能：获取单精度浮点数的最小次正规数。

返回值：

- T - 类型 T 的最小次正规数。

### static func getMinNormal()

```cangjie
static func getMinNormal(): T
```

功能：获取单精度浮点数的最小正规数。

返回值：

- T - 类型 T 的最小正规数。

### static func getNaN()

```cangjie
static func getNaN(): T
```

功能：获取浮点数的非数。

返回值：

- T - 类型 T 的非数。

### static func getPI()

```cangjie
static func getPI(): T
```

功能：获取 T 类型的圆周率常数。

返回值：

- T - 类型 T 的圆周率常数。

### func isInf()

```cangjie
func isInf(): Bool
```

功能：判断浮点数是否为无穷数值。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果浮点数的值正无穷大或负无穷大，则返回 `true`；否则，返回 `false`。

### func isNaN()

```cangjie
func isNaN(): Bool
```

功能：判断浮点数是否为非数值。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果浮点数的值为非数值，则返回 `true`；否则，返回 `false`。

### func isNormal()

```cangjie
func isNormal(): Bool
```

功能：判断浮点数是否为常规数值。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果是正常的浮点数，返回 `true`；否则，返回 `false`。
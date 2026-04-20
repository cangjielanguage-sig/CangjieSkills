### 基础类型

仓颉与 C 语言支持基本数据类型的映射，总体原则是：

1. 仓颉的类型不包含指向托管内存的引用类型；
2. 仓颉的类型和 C 的类型具有同样的内存布局。

比如说，一些基本的类型映射关系如下：

| Cangjie Type |   C Type   |    Size (byte)     |
|:------------:|:----------:|:------------------:|
|    `Unit`    |   `void`   |         0          |
|    `Bool`    |   `bool`   |         1          |
|   `UInt8`    |   `char`   |         1          |
|    `Int8`    |  `int8_t`  |         1          |
|   `UInt8`    | `uint8_t`  |         1          |
|   `Int16`    | `int16_t`  |         2          |
|   `UInt16`   | `uint16_t` |         2          |
|   `Int32`    | `int32_t`  |         4          |
|   `UInt32`   | `uint32_t` |         4          |
|   `Int64`    | `int64_t`  |         8          |
|   `UInt64`   | `uint64_t` |         8          |
| `IntNative`  | `ssize_t`  | platform dependent |
| `UIntNative` |  `size_t`  | platform dependent |
|  `Float32`   |  `float`   |         4          |
|  `Float64`   |  `double`  |         8          |

> **说明：**
>
> `int` 类型、`long` 类型等由于其在不同平台上的不确定性，需要程序员自行指定对应仓颉编程语言类型。在 C 互操作场景中，与 C 语言类似，`Unit` 类型仅可作为 `CFunc` 中的返回类型和 `CPointer` 的泛型参数。

仓颉也支持与 C 语言的结构体和指针类型的映射。

### 结构体

对于结构体类型，仓颉用 `@C` 修饰的 `struct` 来对应。比如说 C 语言里面有这样的一个结构体：

```c
typedef struct {
    long long x;
    long long y;
    long long z;
} Point3D;
```

那么它对应的仓颉类型可以这样定义：

<!-- run -example00-->

```cangjie
@C
struct Point3D {
    var x: Int64 = 0
    var y: Int64 = 0
    var z: Int64 = 0
}
```

如果 C 语言里有这样的一个函数：

```c
Point3D addPoint(Point3D p1, Point3D p2);
```

那么对应的，在仓颉里面可以这样声明这个函数：

<!-- run -example00-->

```cangjie
foreign func addPoint(p1: Point3D, p2: Point3D): Point3D
```

用 `@C` 修饰的 `struct` 必须满足以下限制：

- 成员变量的类型必须满足 `CType` 约束
- 不能实现或者扩展 `interfaces`
- 不能作为 `enum` 的关联值类型
- 不允许被闭包捕获
- 不能具有泛型参数

用 `@C` 修饰的 `struct` 自动满足 `CType` 约束。
## VArray

除了引用类型的数组 Array，仓颉还引入了值类型数组 `VArray<T, $N>` ，其中 `T` 表示该值类型数组的元素类型，`$N` 是一个固定的语法。通过 `$` 加上一个 `Int64` 类型的数值字面量表示这个值类型数组的长度。需要注意的是，`VArray<T, $N>` 不能省略 `<T, $N>`，且使用类型别名时，不允许拆分 `VArray` 关键字与其泛型参数。

与频繁使用引用类型 Array 相比，使用值类型 VArray 可以减少堆上内存分配和垃圾回收的压力。但是需要注意的是，由于值类型本身在传递和赋值时的拷贝，会产生额外的性能开销，因此建议不要在性能敏感场景使用较大长度的 `VArray`。值类型和引用类型的特点请参见[值类型和引用类型变量](../basic_programming_concepts/program_structure.md#值类型和引用类型变量)。
<!-- compile.error -->

```cangjie
type varr1 = VArray<Int64, $3> // OK
type varr2 = VArray // Error
```

> **注意：**
>
> 由于运行时后端限制，当前 `VArray<T, $N>` 的元素类型 `T` 或 `T` 的成员不能包含引用类型、枚举类型、Lambda 表达式（`CFunc` 除外）以及未实例化的泛型类型。

`VArray` 可以由一个数组的字面量来进行初始化，左值 `a` 必须标识出 `VArray` 的实例化类型：

<!-- compile -->

```cangjie
var a: VArray<Int64, $3> = [1, 2, 3]
```

同时，它拥有两个构造函数：

<!-- compile -->

```cangjie
// VArray<T, $N>(initElement: (Int64) -> T)
let b = VArray<Int64, $5>({ i => i }) // [0, 1, 2, 3, 4]
// VArray<T, $N>(repeat!: T)
let c = VArray<Int64, $5>(repeat: 0) // [0, 0, 0, 0, 0]
```

除此之外，`VArray<T, $N>` 类型提供了两个成员方法：

- 用于下标访问和修改的 `[]` 操作符方法：

  <!-- compile -->

  ```cangjie
  var a: VArray<Int64, $3> = [1, 2, 3]
  let i = a[1] // i is 2
  a[2] = 4 // a is [1, 2, 4]
  ```

  下标访问的下标类型必须为 `Int64`。

- 用于获取 `VArray` 长度的 `size` 成员：

  <!-- compile -->

  ```cangjie
  var a: VArray<Int64, $3> = [1, 2, 3]
  let s = a.size // s is 3
  ```

  size 属性的类型为 `Int64`。

此外，`VArray` 还支持仓颉与 C 语言互操作场景使用，相关内容请参见[数组](../FFI/cangjie-c.md#数组)。
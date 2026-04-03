## func sort\<T>(ArrayList\<T>, (T, T) -> Ordering, Bool, Bool)

```cangjie
public func sort<T>(data: ArrayList<T>, by!: (T, T) -> Ordering, stable!: Bool = false, descending!: Bool = false): Unit
```

功能：对 `ArrayList` 按照比较函数进行排序。可根据入参指定是否要进行稳定排序，是升序还是降序。

用户需传入自定义的比较函数 `by`。如果 `by` 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).GT，排序后 `t1` 在 `t2` 后；如果 `by` 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).LT，排序后 `t1` 在 `t2` 前；如果 `by` 的返回值为 [Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering).EQ，排序后 `t1` 与 `t2` 的位置与是否是稳定排序有关，稳定则较排序前保持不变，否则有可能发生改变。

参数：

- data: [ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<T> - 需要排序的 `ArrayList`。
- by!: (T, T) ->[Ordering](../../core/core_package_api/core_package_enums.md#enum-ordering) - 传入的比较函数。
- stable!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用稳定排序，默认为否。
- descending!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用降序排序，默认为否。

示例：

<!-- verify -->
```cangjie
import std.sort.*
import std.collection.*

class Rectangle <: ToString {
    var width: Int64
    var height: Int64

    public init(width: Int64, height: Int64) {
        this.width = width
        this.height = height
    }

    public func toString(): String {
        return "#width: ${this.width}, height: ${this.height}"
    }
}

main() {
    /* 按照面积降序排序 */
    var arr = ArrayList<Rectangle>([Rectangle(4, 8), Rectangle(6, 7), Rectangle(2, 6)])
    sort<Rectangle>(
        arr,
        by: {
            r1: Rectangle, r2: Rectangle =>
            let r1Value: Int64 = r1.width * r1.height
            let r2Value: Int64 = r2.width * r2.height
            if (r1Value > r2Value) {
                return Ordering.GT
            } else if (r1Value == r2Value) {
                return Ordering.EQ
            } else {
                return Ordering.LT
            }
        },
        stable: true,
        descending: true
    )
    println(arr)
    return 0
}
```

运行结果：

```text
[#width: 6, height: 7, #width: 4, height: 8, #width: 2, height: 6]
```
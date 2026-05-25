## func sort\<T>(Array\<T>, (T, T) -> Bool, Bool, Bool)

```cangjie
public func sort<T>(data: Array<T>, lessThan!: (T, T) -> Bool, stable!: Bool = false, descending!: Bool = false): Unit
```

功能：对数组按照比较函数进行排序。可根据入参指定是否要进行稳定排序，是升序还是降序。

用户需传入自定义的比较函数 `lessThan`。如果 `lessThan` 的返回值为 `true`，排序后 `t1` 在 `t2` 前；如果 `lessThan` 的返回值为`false`，又会分为两种情况，如果 `t1` 和 `t2` 不相等，排序后 `t1` 在 `t2` 后，如果相等，`t1` 与 `t2` 的前后位置关系与是否是稳定排序有关，稳定则较排序前保持不变，否则有可能发生改变。

参数：

- data: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - 需要排序的数组。
- lessThan!: (T, T) ->[Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 传入的比较函数。
- stable!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用稳定排序，默认为否。
- descending!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用降序排序，默认为否。

示例：

<!-- verify -->
```cangjie
import std.sort.*

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
    var arr = [Rectangle(4, 8), Rectangle(6, 7), Rectangle(2, 6)]
    sort<Rectangle>(
        arr,
        lessThan: {
            r1: Rectangle, r2: Rectangle =>
            let r1Value: Int64 = r1.width * r1.height
            let r2Value: Int64 = r2.width * r2.height
            return r1Value < r2Value
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
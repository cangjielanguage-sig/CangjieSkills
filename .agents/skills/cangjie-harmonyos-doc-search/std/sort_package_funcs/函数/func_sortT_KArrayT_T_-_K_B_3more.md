## func sort\<T, K>(Array\<T>, (T) -> K, Bool, Bool) where K <: Comparable\<K>

```cangjie
public func sort<T, K>(data: Array<T>, key!: (T) -> K, stable!: Bool = false, descending!: Bool = false): Unit where K <: Comparable<K>
```

功能：对数组按照指定的键（键与键之间可比较）进行排序。可根据入参指定是否要进行稳定排序，是升序还是降序。

用户需传入数组元素到键的映射函数。

参数：

- data: [Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<T> - 需要排序的数组。
- key!: (T) -> K - 元素到键的映射函数。
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
    /* 按照宽降序排序 */
    var arr = [Rectangle(4, 8), Rectangle(6, 7), Rectangle(2, 6)]
    sort<Rectangle, Int64>(
        arr,
        key: {
            r: Rectangle => return r.width
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

## func sort\<T, K>(ArrayList\<T>, (T) -> K, Bool, Bool) where K <: Comparable\<K>

```cangjie
public func sort<T, K>(data: ArrayList<T>, key!: (T) -> K, stable!: Bool = false, descending!: Bool = false): Unit where K <: Comparable<K>
```

功能：对 `ArrayList` 按照指定的键（键与键之间可比较）进行排序。可根据入参指定是否要进行稳定排序，是升序还是降序。

用户需传入 `ArrayList` 元素到键的映射函数。

参数：

- data: [ArrayList](../../collection/collection_package_api/collection_package_class.md#class-arraylistt)\<T> - 需要排序的 `ArrayList`。
- key!: (T) -> K - 元素到键的映射函数。
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
    /* 按照宽降序排序 */
    var arr = ArrayList<Rectangle>([Rectangle(4, 8), Rectangle(6, 7), Rectangle(2, 6)])
    sort<Rectangle, Int64>(
        arr,
        key: {
            r: Rectangle => return r.width
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

## func sort\<T, K>(List\<T>, (T) -> K, Bool, Bool) where K <: Comparable\<K>

```cangjie
public func sort<T, K>(data: List<T>, key!: (T) -> K, stable!: Bool = false, descending!: Bool = false): Unit where K <: Comparable<K>
```

功能：对 `List` 按照指定的键（键与键之间可比较）进行排序。可根据入参指定是否要进行稳定排序，是升序还是降序。

用户需传入 `List` 元素到键的映射函数。

参数：

- data: [List](../../collection/collection_package_api/collection_package_interface.md#interface-listt)\<T> - 需要排序的 `List`。
- key!: (T) -> K - 元素到键的映射函数。
- stable!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用稳定排序，默认为否。
- descending!: [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 是否使用降序排序，默认为否。
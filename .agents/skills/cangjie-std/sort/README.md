# 仓颉语言排序 Skill

## 1. 基本排序

- 来自 `std.sort.*`
- 所有 `sort` 重载都原地修改传入集合并返回 `Unit`
- **支持 `Array<T>`、`ArrayList<T>`、`List<T>` 三种集合类型，所有重载形式均适用**

| 函数 | 说明 |
|------|------|
| `sort<T>(data: Array<T>)` | 默认升序排序（`T <: Comparable`） |
| `sort<T>(data: ArrayList<T>)` | 对 `ArrayList` 升序排序 |
| `sort<T>(data: Array<T>, descending!: Bool)` | 降序排序 |

### 1.1 排序路径选择

- 允许修改目标集合时，直接调用 `sort(data)`，后续从同一个 `data` 读取结果。
- 必须保留输入顺序时，先按集合专题构造独立副本，再对副本排序；普通赋值可能共享底层存储，不能自动视为复制。
- 当前环境无法使用 `std.sort.*` 时，可以选择已验证的替代算法；是否值得手写取决于输入规模、稳定性要求和可用验证，而不是把标准库路径假设为唯一实现。

---

## 2. 自定义排序

| 函数 | 说明 |
|------|------|
| `sort<T>(data: Array<T>, by!: (T, T) -> Ordering)` | 使用比较器排序（返回 `Ordering` 枚举） |
| `sort<T>(data: Array<T>, lessThan!: (T, T) -> Bool)` | 使用比较函数排序 |
| `sort<T, K>(data: Array<T>, key!: (T) -> K)` | 按键提取函数排序（`K <: Comparable`） |

以上 `Array<T>` 参数位置均可替换为 `ArrayList<T>` 或 `List<T>`，签名一致。

- 可选命名参数：`stable: Bool = false`、`descending: Bool = false`

---

## 3. 稳定排序

- `sort(arr, stable: true)` — 保持相等元素的原始顺序
- 可与 `by`、`lessThan`、`key` 组合使用

```cangjie
package test_proj
import std.sort.*
import std.collection.*

class Student <: ToString {
    public let name: String
    public let age: Int64
    public init(name: String, age: Int64) {
        this.name = name
        this.age = age
    }
    public func toString(): String {
        return "{name: ${name} age: ${age}}"
    }
}

main() {
    // 基本排序
    let a = [1, 3, 5, 2, 4]
    sort(a)
    println(a)

    // by 比较器排序
    let b = [Student("A", 8), Student("B", 7), Student("C", 3), Student("D", 4), Student("E", 6)]
    let comparator = {l: Student, r: Student => l.age.compare(r.age)}
    sort(b, by: comparator)
    println(b)

    // lessThan 降序排序
    let c = [Student("A", 8), Student("B", 7), Student("C", 3), Student("D", 4), Student("E", 6)]
    let lessThan = {l: Student, r: Student => l.age < r.age}
    sort(c, lessThan: lessThan, descending: true)
    println(c)

    // key 稳定排序
    let d = [Student("A", 8), Student("B", 7), Student("C", 7), Student("D", 4), Student("E", 7)]
    let key = {i: Student => i.age}
    sort(d, key: key, stable: true)
    println(d)

    // ArrayList 排序
    let al = ArrayList<Int64>([5, 3, 1, 4, 2])
    sort(al)
    println(al)  // [1, 2, 3, 4, 5]
    sort(al, descending: true)
    println(al)  // [5, 4, 3, 2, 1]
    return 0
}
```

---

## 4. 关键规则速查

1. 排序结果保存在传入集合中；调用完成后从该集合读取结果
2. `by` 参数接收返回 `Ordering` 的比较器
3. `lessThan` 参数接收返回 `Bool` 的比较函数
4. `key` 参数接收键提取函数，按提取值排序
5. `descending: true` 可与任意排序方式组合使用
6. 支持 `Array<T>`、`ArrayList<T>`、`List<T>` 等集合类型

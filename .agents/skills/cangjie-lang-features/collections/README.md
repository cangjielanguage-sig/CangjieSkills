# 仓颉集合数据类型

本页只负责路由，不提供具体 API 的可用性证明。最终源码一旦出现相应构造，写入前必须继续读取对应专题：

- [Array](./array/README.md)：定长数组；构造、索引修改、切片、直接相等比较都读此专题。
- [ArrayList](./arraylist/README.md)：可变长列表；需要追加、删除或动态收集结果时读此专题，并由 `cangjie-std` 核对 `std.collection` import 与方法名。
- [HashMap](./hashmap/README.md)：哈希表/键值映射；核对键值约束、插入方法和 import。
- [HashSet](./hashset/README.md)：集合；核对元素约束、插入方法和 import。

固定长度已知时优先比较 `Array` 的预分配路径；长度未知或需要追加时再选择动态集合。不能把其它语言的 `append`、`put`、`filter`、`sort` 成员调用直接迁移到这些类型。

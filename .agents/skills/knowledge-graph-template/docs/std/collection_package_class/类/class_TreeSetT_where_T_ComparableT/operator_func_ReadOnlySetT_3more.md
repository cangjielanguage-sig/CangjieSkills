### operator func |(ReadOnlySet\<T>)

```cangjie
public operator func |(other: ReadOnlySet<T>): TreeSet<T>
```

功能：返回包含两个集合并集的元素的新集合。

参数：

- other: [ReadOnlySet](collection_package_interface.md#interface-readonlysett)\<T> - 传入集合。

返回值：

- [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)\<T> - T 类型集合。

### extend\<T> TreeSet\<T> <: Equatable\<TreeSet\<T>>

```cangjie
extend<T> TreeSet<T> <: Equatable<TreeSet<T>>
```

功能：为 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)\<T> 类型扩展 [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)\<T>> 接口，支持判等操作。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)\<T>>

#### operator func !=(TreeSet\<T>)

```cangjie
public operator func !=(that: TreeSet<T>): Bool
```

功能：判断当前实例与参数指向的 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)\<T> 实例是否不等。

参数：

- that: [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)\<T> - 被比较的对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果不等，则返回 true，否则返回 false。

#### operator func ==(TreeSet\<T>)

```cangjie
public operator func ==(that: TreeSet<T>): Bool
```

功能：判断当前实例与参数指向的 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)\<T> 实例是否相等。

两个 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)\<T> 相等指的是其中包含的元素完全相等。

参数：

- that: [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)\<T> - 被比较的对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果相等，则返回 true，否则返回 false。

### extend\<T> TreeSet\<T> <: ToString where T <: ToString

```cangjie
extend<T> TreeSet<T> <: ToString where T <: ToString
```

功能：为 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)\<T> 扩展 [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring) 接口，支持转字符串操作。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

#### func toString()

```cangjie
public func toString(): String
```

功能：将当前 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)\<T> 实例转换为字符串。

该字符串包含 [TreeSet](collection_package_class.md#class-treesett-where-t--comparablet)\<T> 内每个元素的字符串表示，形如："[elem1, elem2, elem3]"。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转换得到的字符串。
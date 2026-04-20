### extend\<T> LinkedList\<T> <: Equatable\<LinkedList\<T>> where T <: Equatable\<T>

```cangjie
extend<T> LinkedList<T> <: Equatable<LinkedList<T>> where T <: Equatable<T>
```

功能：为 [LinkedList](./collection_package_class.md#class-linkedlistt)\<T> 类型扩展 [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[LinkedList](./collection_package_class.md#class-linkedlistt)\<T>> 接口，支持判等操作。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[LinkedList](#class-linkedlistt)\<T>>

#### operator func !=(LinkedList\<T>)

```cangjie
public operator func !=(right: LinkedList<T>): Bool
```

功能：判断当前实例与参数指向的 [LinkedList](./collection_package_class.md#class-linkedlistt)\<T> 实例是否不等。

参数：

- right: [LinkedList](./collection_package_class.md#class-linkedlistt)\<T> - 被比较的对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果不等，则返回 true，否则返回 false。

#### operator func ==(LinkedList\<T>)

```cangjie
public operator func ==(right: LinkedList<T>): Bool
```

功能：判断当前实例与参数指向的 [LinkedList](./collection_package_class.md#class-linkedlistt)\<T> 实例是否相等。

两个 [LinkedList](./collection_package_class.md#class-linkedlistt)\<T> 相等指的是其中包含的元素完全相等。

参数：

- right: [LinkedList](./collection_package_class.md#class-linkedlistt)\<T> - 被比较的对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果相等，则返回 true，否则返回 false。

### extend\<T> LinkedList\<T> <: ToString where T <: ToString

```cangjie
extend<T> LinkedList<T> <: ToString where T <: ToString
```

功能：为 [LinkedList](./collection_package_class.md#class-linkedlistt)\<T> 扩展 [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring) 接口，支持转字符串操作。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

#### func toString()

```cangjie
public func toString(): String
```

功能：将当前 [LinkedList](./collection_package_class.md#class-linkedlistt)\<T> 实例转换为字符串。

该字符串包含 [LinkedList](./collection_package_class.md#class-linkedlistt)\<T> 内每个元素的字符串表示，形如："[elem1, elem2, elem3]"。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转换得到的字符串。
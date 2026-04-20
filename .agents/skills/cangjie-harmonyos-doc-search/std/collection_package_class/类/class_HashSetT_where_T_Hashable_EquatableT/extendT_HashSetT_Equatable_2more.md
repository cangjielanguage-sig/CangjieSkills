### extend\<T> HashSet\<T> <: Equatable\<HashSet\<T>>

```cangjie
extend<T> HashSet<T> <: Equatable<HashSet<T>>
```

功能：为 [HashSet](./collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T> 类型扩展 [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[HashSet](./collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T>> 接口，支持判等操作。

父类型：

- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[HashSet](./collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T>>

#### operator func !=(HashSet\<T>)

```cangjie
public operator func !=(that: HashSet<T>): Bool
```

功能：判断当前实例与参数指向的 [HashSet](./collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T> 实例是否不等。

参数：

- that: [HashSet](./collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T> - 被比较的对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果不等，则返回 true，否则返回 false。

#### operator func ==(HashSet\<T>)

```cangjie
public operator func ==(that: HashSet<T>): Bool
```

功能：判断当前实例与参数指向的 [HashSet](./collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T> 实例是否相等。

两个 [HashSet](./collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T> 相等指的是其中包含的元素完全相等。

参数：

- that: [HashSet](./collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T> - 被比较的对象。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果相等，则返回 true，否则返回 false。

### extend\<T> HashSet\<T> <: ToString where T <: ToString

```cangjie
extend<T> HashSet<T> <: ToString where T <: ToString
```

功能：为 [HashSet](./collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T> 扩展 [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring) 接口，支持转字符串操作。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

#### func toString()

```cangjie
public func toString(): String
```

功能：将当前 [HashSet](./collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T> 实例转换为字符串。

该字符串包含 [HashSet](./collection_package_class.md#class-hashsett-where-t--hashable--equatablet)\<T> 内每个元素的字符串表示，形如："[elem1, elem2, elem3]"。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转换得到的字符串。
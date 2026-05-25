### extend\<T> ArrayQueue\<T> <: ToString where T <: ToString

```cangjie
extend<T> ArrayQueue<T> <: ToString where T <: ToString
```

功能：为 [ArrayQueue](./collection_package_class.md#class-arrayqueuet)\<T> 扩展 [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring) 接口，支持转字符串操作。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

#### func toString()

```cangjie
public func toString(): String
```

功能：获取当前 [ArrayQueue](./collection_package_class.md#class-arrayqueuet)\<T> 实例的字符串表示。

该字符串包含双端队列内每个元素的字符串表示，其顺序为从前到后的顺序，形如："[elem1, elem2, elem3]"。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转换得到的字符串。
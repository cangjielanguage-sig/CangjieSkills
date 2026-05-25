### extend\<T> HashSet\<T> <: Serializable\<HashSet\<T>> where T <: Serializable\<T> & Hashable & Equatable\<T>

```cangjie
extend<T> HashSet<T> <: Serializable<HashSet<T>> where T <: Serializable<T> & Hashable & Equatable<T>
```

功能：为 HashSet\<T> 类型实现 [Serializable](#interface-serializable)\<HashSet\<T>> 接口。

父类型：

- [Serializable](#interface-serializable)\<HashSet\<T>>

#### static func deserialize(DataModel)

```cangjie
public static func deserialize(dm: DataModel): HashSet<T>
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为 HashSet\<T>。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 需要被反序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- HashSet\<T> - 反序列化后的 HashSet\<T>。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 的类型不是 [DataModelSeq](serialization_package_classes.md#class-datamodelseq) 时，抛出异常。

#### func serialize()

```cangjie
public func serialize(): DataModel
```

功能：将 HashSet\<T> 序列化为 [DataModelSeq](serialization_package_classes.md#class-datamodelseq)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModelSeq](serialization_package_classes.md#class-datamodelseq)。

### extend Int16 <: Serializable

```cangjie
extend Int16 <: Serializable<Int16>
```

功能：为 Int16 类型实现 [Serializable](#interface-serializable) 接口。

父类型：

- [Serializable](#interface-serializable)\<Int16>

#### static func deserialize(DataModel)

```cangjie
public static func deserialize(dm: DataModel): Int16
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为 Int16。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 需要被反序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- Int16 - 反序列化后的 Int16。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 的类型不是 [DataModelInt](serialization_package_classes.md#class-datamodelint) 时，则抛出异常。

#### func serialize()

```cangjie
public func serialize(): DataModel
```

功能：将 Int16 序列化为 [DataModelInt](serialization_package_classes.md#class-datamodelint)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModelInt](serialization_package_classes.md#class-datamodelint)。
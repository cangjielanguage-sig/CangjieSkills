### extend\<T> ArrayList\<T> <: Serializable\<ArrayList\<T>> where T <: Serializable\<T>

```cangjie
extend<T> ArrayList<T> <: Serializable<ArrayList<T>> where T <: Serializable<T>
```

功能：为 ArrayList\<T> 类型实现 [Serializable](#interface-serializable)\<ArrayList\<T>> 接口。

父类型：

- [Serializable](#interface-serializable)\<ArrayList\<T>>

#### static func deserialize(DataModel)

```cangjie
public static func deserialize(dm: DataModel): ArrayList<T>
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为 ArrayList\<T>。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 需要被反序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- ArrayList\<T> - 反序列化后的 ArrayList\<T>。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 的类型不是 [DataModelSeq](serialization_package_classes.md#class-datamodelseq) 时，抛出异常。

#### func serialize()

```cangjie
public func serialize(): DataModel
```

功能：将 ArrayList\<T> 序列化为 [DataModelSeq](serialization_package_classes.md#class-datamodelseq)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModelSeq](serialization_package_classes.md#class-datamodelseq)。

### extend Bool <: Serializable

```cangjie
extend Bool <: Serializable<Bool>
```

功能：为 Bool 类型实现 [Serializable](#interface-serializable) 接口。

父类型：

- [Serializable](#interface-serializable)\<Bool>

#### static func deserialize(DataModel)

```cangjie
public static func deserialize(dm: DataModel): Bool
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为 Bool。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 需要被反序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- Bool - 反序列化后的 Bool。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 的类型不是 [DataModelBool](serialization_package_classes.md#class-datamodelbool) 时，抛出异常。

#### func serialize()

```cangjie
public func serialize(): DataModel
```

功能：将 Bool 序列化为 [DataModelBool](serialization_package_classes.md#class-datamodelbool)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModelBool](serialization_package_classes.md#class-datamodelbool)。
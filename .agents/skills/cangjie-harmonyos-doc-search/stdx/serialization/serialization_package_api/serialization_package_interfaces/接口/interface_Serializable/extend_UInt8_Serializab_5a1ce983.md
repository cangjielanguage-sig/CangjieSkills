### extend UInt8 <: Serializable

```cangjie
extend UInt8 <: Serializable<UInt8>
```

功能：为 UInt8 类型实现 [Serializable](#interface-serializable) 接口。

父类型：

- [Serializable](#interface-serializable)\<UInt8>

#### static func deserialize(DataModel)

```cangjie
public static func deserialize(dm: DataModel): UInt8
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为 UInt8。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 需要被反序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- UInt8 - 反序列化后的 UInt8。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 的类型不是 [DataModelInt](serialization_package_classes.md#class-datamodelint) 时，则抛出异常。

#### func serialize()

```cangjie
public func serialize(): DataModel
```

功能：将 UInt8 序列化为 [DataModelInt](serialization_package_classes.md#class-datamodelint)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModelInt](serialization_package_classes.md#class-datamodelint)。
### extend Float16 <: Serializable

```cangjie
extend Float16 <: Serializable<Float16>
```

功能：为 Float16 类型实现 [Serializable](#interface-serializable) 接口。

父类型：

- [Serializable](#interface-serializable)\<Float16>

#### static func deserialize(DataModel)

```cangjie
public static func deserialize(dm: DataModel): Float16
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为 Float16。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 需要被反序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- Float16 - 反序列化后的 Float16。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 的类型不是 [DataModelFloat](serialization_package_classes.md#class-datamodelfloat) 或者 [DataModelInt](serialization_package_classes.md#class-datamodelint) 时，抛出异常。

#### func serialize()

```cangjie
public func serialize(): DataModel
```

功能：将 Float16 序列化为 [DataModelFloat](serialization_package_classes.md#class-datamodelfloat)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModelFloat](serialization_package_classes.md#class-datamodelfloat)。

### extend Float32 <: Serializable

```cangjie
extend Float32 <: Serializable<Float32>
```

功能：为 Float32 类型实现 [Serializable](#interface-serializable) 接口。

父类型：

- [Serializable](#interface-serializable)\<Float32>

#### static func deserialize(DataModel)

```cangjie
public static func deserialize(dm: DataModel): Float32
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为 Float32。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 需要被反序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- Float32 - 反序列化后的 Float32。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 的类型不是 [DataModelFloat](serialization_package_classes.md#class-datamodelfloat) 或者 [DataModelInt](serialization_package_classes.md#class-datamodelint) 时，抛出异常。

#### func serialize()

```cangjie
public func serialize(): DataModel
```

功能：将 Float32 序列化为 [DataModelFloat](serialization_package_classes.md#class-datamodelfloat)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModelFloat](serialization_package_classes.md#class-datamodelfloat)。
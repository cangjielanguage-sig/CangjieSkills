### extend UInt16 <: Serializable

```cangjie
extend UInt16 <: Serializable<UInt16>
```

功能：为 UInt16 类型实现 [Serializable](#interface-serializable) 接口。

父类型：

- [Serializable](#interface-serializable)\<UInt16>

#### static func deserialize(DataModel)

```cangjie
public static func deserialize(dm: DataModel): UInt16
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为 UInt16。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 需要被反序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- UInt16 - 反序列化后的 UInt16。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 的类型不是 [DataModelInt](serialization_package_classes.md#class-datamodelint) 时，则抛出异常。

#### func serialize()

```cangjie
public func serialize(): DataModel
```

功能：将 UInt16 序列化为 [DataModelInt](serialization_package_classes.md#class-datamodelint)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModelInt](serialization_package_classes.md#class-datamodelint)。

### extend UInt32 <: Serializable

```cangjie
extend UInt32 <: Serializable<UInt32>
```

功能：为 UInt32 类型实现 [Serializable](#interface-serializable) 接口。

父类型：

- [Serializable](#interface-serializable)\<UInt32>

#### static func deserialize(DataModel)

```cangjie
public static func deserialize(dm: DataModel): UInt32
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为 UInt32。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 需要被反序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- UInt32 - 反序列化后的 UInt32。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 的类型不是 [DataModelInt](serialization_package_classes.md#class-datamodelint) 时，则抛出异常。

#### func serialize()

```cangjie
public func serialize(): DataModel
```

功能：将 UInt32 序列化为 [DataModelInt](serialization_package_classes.md#class-datamodelint)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModelInt](serialization_package_classes.md#class-datamodelint)。

### extend UInt64 <: Serializable

```cangjie
extend UInt64 <: Serializable<UInt64>
```

功能：为 UInt64 类型实现 [Serializable](#interface-serializable) 接口。

父类型：

- [Serializable](#interface-serializable)\<UInt64>

#### static func deserialize(DataModel)

```cangjie
public static func deserialize(dm: DataModel): UInt64
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为 UInt64。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 需要被反序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- UInt64 - 反序列化后的 UInt64。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 的类型不是 [DataModelInt](serialization_package_classes.md#class-datamodelint) 时，则抛出异常。

#### func serialize()

```cangjie
public func serialize(): DataModel
```

功能：将 UInt64 序列化为 [DataModelInt](serialization_package_classes.md#class-datamodelint)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModelInt](serialization_package_classes.md#class-datamodelint)。
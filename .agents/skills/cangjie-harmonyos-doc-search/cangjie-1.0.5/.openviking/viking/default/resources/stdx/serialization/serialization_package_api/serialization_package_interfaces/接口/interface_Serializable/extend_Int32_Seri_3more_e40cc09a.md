### extend Int32 <: Serializable

```cangjie
extend Int32 <: Serializable<Int32>
```

功能：为 Int32 类型实现 [Serializable](#interface-serializable) 接口。

父类型：

- [Serializable](#interface-serializable)\<Int32>

#### static func deserialize(DataModel)

```cangjie
public static func deserialize(dm: DataModel): Int32
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为 Int32。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 需要被反序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- Int32 - 反序列化后的 Int32。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 的类型不是 [DataModelInt](serialization_package_classes.md#class-datamodelint) 时，抛出异常

#### func serialize()

```cangjie
public func serialize(): DataModel
```

功能：将 Int32 序列化为 [DataModelInt](serialization_package_classes.md#class-datamodelint)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModelInt](serialization_package_classes.md#class-datamodelint)。

### extend Int64 <: Serializable

```cangjie
extend Int64 <: Serializable<Int64>
```

功能：为 Int64 类型实现 [Serializable](#interface-serializable) 接口。

父类型：

- [Serializable](#interface-serializable)\<Int64>

#### static func deserialize(DataModel)

```cangjie
public static func deserialize(dm: DataModel): Int64
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为 Int64。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 需要被反序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- Int64 - 反序列化后的 Int64。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 的类型不是 [DataModelInt](serialization_package_classes.md#class-datamodelint) 时，抛出异常。

#### func serialize()

```cangjie
public func serialize(): DataModel
```

功能：将 Int64 序列化为 [DataModelInt](serialization_package_classes.md#class-datamodelint)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModelInt](serialization_package_classes.md#class-datamodelint)。

### extend Int8 <: Serializable

```cangjie
extend Int8 <: Serializable<Int8>
```

功能：为 Int8 类型实现 [Serializable](#interface-serializable) 接口。

父类型：

- [Serializable](#interface-serializable)\<Int8>

#### static func deserialize(DataModel)

```cangjie
public static func deserialize(dm: DataModel): Int8
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为 Int8。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 需要被反序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- Int8 - 反序列化后的 Int8。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 的类型不是 [DataModelInt](serialization_package_classes.md#class-datamodelint) 时，抛出异常。

#### func serialize()

```cangjie
public func serialize(): DataModel
```

功能：将 Int8 序列化为 [DataModelInt](serialization_package_classes.md#class-datamodelint)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModelInt](serialization_package_classes.md#class-datamodelint)。
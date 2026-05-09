### extend\<T> Option\<T> <: Serializable\<Option\<T>> where T <: Serializable\<T>

```cangjie
extend<T> Option<T> <: Serializable<Option<T>> where T <: Serializable<T>
```

功能：为 Option\<T> 类型实现 [Serializable](#interface-serializable)\<Option\<T>> 接口。

父类型：

- [Serializable](#interface-serializable)\<Option\<T>>

#### static func deserialize(DataModel)

```cangjie
public static func deserialize(dm: DataModel): Option<T>
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为 Option\<T>。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 需要被反序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- Option\<T> - 反序列化后的 Option\<T>。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 的类型不支持反序列化到 T 类型时，抛出异常。

#### func serialize()

```cangjie
public func serialize(): DataModel
```

功能：将 Option\<T> 中的 `T` 序列化为 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

### extend Rune <: Serializable

```cangjie
extend Rune <: Serializable<Rune>
```

功能：为 Rune 类型实现 [Serializable](#interface-serializable) 接口。

父类型：

- [Serializable](#interface-serializable)\<Rune>

#### static func deserialize(DataModel)

```cangjie
public static func deserialize(dm: DataModel): Rune
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为 Rune。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 需要被反序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- Rune - 反序列化后的字符。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 的类型不是 [DataModelString](serialization_package_classes.md#class-datamodelstring) 时，则抛出此异常。
- Exception - 当 `dm` 的类型不是 Rune 时，则抛出此异常。

#### func serialize()

```cangjie
public func serialize(): DataModel
```

功能：将 Rune 序列化为 [DataModelString](serialization_package_classes.md#class-datamodelstring)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModelString](serialization_package_classes.md#class-datamodelstring)。

### extend String <: Serializable

```cangjie
extend String <: Serializable<String>
```

功能：为 String 类型实现 [Serializable](#interface-serializable) 接口。

父类型：

- [Serializable](#interface-serializable)\<String>

#### static func deserialize(DataModel)

```cangjie
public static func deserialize(dm: DataModel): String
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为 String。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 需要被反序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- String - 反序列化后的 String。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 的类型不是 [DataModelString](serialization_package_classes.md#class-datamodelstring) 时，则抛出异常。

#### func serialize()

```cangjie
public func serialize(): DataModel
```

功能：将 String 序列化为 [DataModelString](serialization_package_classes.md#class-datamodelstring)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModelString](serialization_package_classes.md#class-datamodelstring)。
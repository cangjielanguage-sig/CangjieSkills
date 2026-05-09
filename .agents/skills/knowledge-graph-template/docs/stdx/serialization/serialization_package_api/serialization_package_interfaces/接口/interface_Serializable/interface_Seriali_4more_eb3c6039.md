## interface Serializable

```cangjie
public interface Serializable<T> {
    func serialize(): DataModel
    static func deserialize(dm: DataModel): T
}
```

功能：用于规范序列化。

### static func deserialize(DataModel)

```cangjie
static func deserialize(dm: DataModel): T
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为对象。

> **说明：**
>
> 支持实现 [Serializable](serialization_package_interfaces.md#interface-serializable) 的类型包括：
>
> - 基本数据类型：整数类型、浮点类型、布尔类型、字符类型、字符串类型。
> - Collection 类型：Array、ArrayList、HashSet、HashMap、Option。
> - 用户自定义的实现了 [Serializable](serialization_package_interfaces.md#interface-serializable)\<T> 的类型。

参数：

- dm: [DataModel](./serialization_package_classes.md#class-datamodel) - 待反序列化的数据。

返回值：

- T - 反序列化的对象。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 的类型不支持反序列化到 T 类型时，抛出异常。

### func serialize()

```cangjie
func serialize(): DataModel
```

功能：将自身序列化为 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

### extend\<T> Array\<T> <: Serializable\<Array\<T>> where T <: Serializable\<T>

```cangjie
extend<T> Array<T> <: Serializable<Array<T>> where T <: Serializable<T>
```

功能：为 Array\<T> 类型实现 [Serializable](#interface-serializable)\<Array\<T>> 接口。

父类型：

- [Serializable](#interface-serializable)\<Array\<T>>

#### static func deserialize(DataModel)

```cangjie
public static func deserialize(dm: DataModel): Array<T>
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为 Array\<T>。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 需要被反序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- Array\<T> - 反序列化后的 Array\<T>。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 的类型不是 [DataModelSeq](serialization_package_classes.md#class-datamodelseq) 时，则抛出异常。

#### func serialize()

```cangjie
public func serialize(): DataModel
```

功能：将 Array\<T> 序列化为 [DataModelSeq](serialization_package_classes.md#class-datamodelseq)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModelSeq](serialization_package_classes.md#class-datamodelseq)。
### extend Float64 <: Serializable

```cangjie
extend Float64 <: Serializable<Float64>
```

功能：为 Float64 类型实现 [Serializable](#interface-serializable) 接口。

父类型：

- [Serializable](#interface-serializable)\<Float64>

#### static func deserialize(DataModel)

```cangjie
public static func deserialize(dm: DataModel): Float64
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为 Float64。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 需要被反序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- Float64 - 反序列化后的 Float64。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 的类型不是 [DataModelFloat](serialization_package_classes.md#class-datamodelfloat) 或者 [DataModelInt](serialization_package_classes.md#class-datamodelint) 时，抛出异常。

#### func serialize()

```cangjie
public func serialize(): DataModel
```

功能：将 Float64 序列化为 [DataModelFloat](serialization_package_classes.md#class-datamodelfloat)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModelFloat](serialization_package_classes.md#class-datamodelfloat)。

### extend\<K, V> HashMap\<K, V> <: Serializable\<HashMap\<K, V>> where K <: Serializable\<K> & Hashable & Equatable\<K>, V <: Serializable\<V>

```cangjie
extend<K, V> HashMap<K, V> <: Serializable<HashMap<K, V>> where K <: Serializable<K> & Hashable & Equatable<K>, V <: Serializable<V>
```

功能：为 HashMap\<K, V> 类型实现 [Serializable](#interface-serializable)\<HashMap\<K, V>> 接口。

父类型：

- [Serializable](#interface-serializable)\<HashMap\<K, V>>

#### static func deserialize(DataModel)

```cangjie
public static func deserialize(dm: DataModel): HashMap<K, V>
```

功能：将 [DataModel](serialization_package_classes.md#class-datamodel) 反序列化为 HashMap\<K, V>。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 需要被反序列化的 [DataModel](serialization_package_classes.md#class-datamodel)。

返回值：

- HashMap\<K, V> - 反序列化后的 HashMap\<K, V>。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当 `dm` 不是 [DataModelStruct](serialization_package_classes.md#class-datamodelstruct) 类型，或者 [DataModelStruct](serialization_package_classes.md#class-datamodelstruct) 类型的 `dm` 中的 [Field](serialization_package_classes.md#class-field) 不是 String 类型时，抛出异常。

#### func serialize()

```cangjie
public func serialize(): DataModel
```

功能：将 HashMap\<K, V> 序列化为 [DataModelSeq](serialization_package_classes.md#class-datamodelseq)。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 序列化的 [DataModelSeq](serialization_package_classes.md#class-datamodelseq)。

异常：

- [DataModelException](serialization_package_exceptions.md#class-datamodelexception) - 当前 HashMap 实例中的 Key 不是 String 类型时，抛出异常。
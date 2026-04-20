## class DataModelSeq

```cangjie
public class DataModelSeq <: DataModel {
    public init()
    public init(list: ArrayList<DataModel>)
}
```

功能：此类为 [DataModel](serialization_package_classes.md#class-datamodel) 的子类，实现对 ArrayList\<[DataModel](serialization_package_classes.md#class-datamodel)> 类型数据的封装。

父类型：

- [DataModel](#class-datamodel)

### init()

```cangjie
public init()
```

功能：构造一个参数为空的 [DataModelSeq](serialization_package_classes.md#class-datamodelseq) 实例。其中的数据默认为空的 ArrayList\<[DataModel](serialization_package_classes.md#class-datamodel)>。

### init(ArrayList\<DataModel>)

```cangjie
public init(list: ArrayList<DataModel>)
```

功能：构造一个具有初始数据的 [DataModelSeq](serialization_package_classes.md#class-datamodelseq) 实例。

参数：

- list: ArrayList\<[DataModel](serialization_package_classes.md#class-datamodel)> - 传入的 ArrayList\<[DataModel](serialization_package_classes.md#class-datamodel)> 类型的数据。

### func add(DataModel)

```cangjie
public func add(dm: DataModel): Unit 
```

功能：在 [DataModelSeq](serialization_package_classes.md#class-datamodelseq) 末尾增加一个 [DataModel](serialization_package_classes.md#class-datamodel) 数据。

参数：

- dm: [DataModel](serialization_package_classes.md#class-datamodel) - 传入的 [DataModel](serialization_package_classes.md#class-datamodel) 类型的数据。

### func getItems()

```cangjie
public func getItems(): ArrayList<DataModel>
```

功能：获取 [DataModelSeq](serialization_package_classes.md#class-datamodelseq) 中的数据。

返回值：

- ArrayList\<[DataModel](serialization_package_classes.md#class-datamodel)> - [DataModelSeq](serialization_package_classes.md#class-datamodelseq) 中的数据，类型为 ArrayList\<[DataModel](serialization_package_classes.md#class-datamodel)>。

## class DataModelString

```cangjie
public class DataModelString <: DataModel {
    public init(sv: String)
}
```

功能：此类为 [DataModel](serialization_package_classes.md#class-datamodel) 的子类，实现对 String 类型数据的封装。

父类型：

- [DataModel](#class-datamodel)

### init(String)

```cangjie
public init(sv: String)
```

功能：构造一个具有初始数据的 [DataModelString](serialization_package_classes.md#class-datamodelstring)。

参数：

- sv: String - 传入的 String 类型。

### func getValue()

```cangjie
public func getValue(): String
```

功能：获取 [DataModelString](serialization_package_classes.md#class-datamodelstring) 中的数据。

返回值：

- String - [DataModelString](serialization_package_classes.md#class-datamodelstring) 中类型为 String 的 `value` 数值。
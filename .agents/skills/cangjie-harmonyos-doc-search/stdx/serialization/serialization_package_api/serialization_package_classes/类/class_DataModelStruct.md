## class DataModelStruct

```cangjie
public class DataModelStruct <: DataModel {
    public init()
    public init(list: ArrayList<Field>)
}
```

功能：此类为 [DataModel](serialization_package_classes.md#class-datamodel) 的子类，用来实现 `class` 对象到 [DataModel](serialization_package_classes.md#class-datamodel) 的转换。

父类型：

- [DataModel](#class-datamodel)

### init()

```cangjie
public init()
```

功能：构造一个空参的 `DataModelStructfields` 默认为空的 ArrayList\<[Field](serialization_package_classes.md#class-field)>。

### init(ArrayList\<Field>)

```cangjie
public init(list: ArrayList<Field>)
```

功能：构造一个具有初始数据的 [DataModelStruct](serialization_package_classes.md#class-datamodelstruct)。

参数：

- list: ArrayList\<[Field](serialization_package_classes.md#class-field)> - 传入的 ArrayList\<[Field](serialization_package_classes.md#class-field)> 类型的数据。

### func add(Field)

```cangjie
public func add(fie: Field): DataModelStruct
```

功能：添加数据 `fie` 到 [DataModelStruct](serialization_package_classes.md#class-datamodelstruct) 中。

参数：

- fie: [Field](serialization_package_classes.md#class-field) - 传入的 [Field](serialization_package_classes.md#class-field) 类型的数据。

返回值：

- [DataModelStruct](serialization_package_classes.md#class-datamodelstruct) - 得到新的 [DataModelStruct](serialization_package_classes.md#class-datamodelstruct)。

### func get(String)

```cangjie
public func get(key: String): DataModel
```

功能：获取 `key` 对应的数据。

参数：

- key: String - 传入的 String 类型。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 类型为 [DataModel](serialization_package_classes.md#class-datamodel)，如未查找到对应值，则返回 [DataModelNull](serialization_package_classes.md#class-datamodelnull)。

### func getFields()

```cangjie
public func getFields(): ArrayList<Field>
```

功能：获取 [DataModelStruct](serialization_package_classes.md#class-datamodelstruct) 的数据集合。

返回值：

- ArrayList\<[Field](serialization_package_classes.md#class-field)> - 类型为 ArrayList\<[Field](serialization_package_classes.md#class-field)> 的数据集合。
## class Field

```cangjie
public class Field {
    public init(name: String, data: DataModel)
}
```

功能：用于存储 [DataModelStruct](serialization_package_classes.md#class-datamodelstruct) 的元素。

### init(String, DataModel)

```cangjie
public init(name: String, data: DataModel)
```

功能：[Field](serialization_package_classes.md#class-field) 的构造函数。

参数：

- name: String - `name` 字段值，`name` 字段为 `""` 时行为与为其它字符串时一致。
- data: [DataModel](serialization_package_classes.md#class-datamodel) - `data` 字段值。

### func getData()

```cangjie
public func getData(): DataModel
```

功能：获取 `data` 字段。

返回值：

- [DataModel](serialization_package_classes.md#class-datamodel) - 获取到的 `data` 字段，类型为 [DataModel](serialization_package_classes.md#class-datamodel)。

### func getName()

```cangjie
public func getName(): String
```

功能：获取 `name` 字段。

返回值：

- String - 获取到的 `name` 字段，类型为 String。
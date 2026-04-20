## class DataModel

```cangjie
public abstract class DataModel
```

功能：此类为中间数据层。

## class DataModelBool

```cangjie
public class DataModelBool <: DataModel {
    public init(bv: Bool)
}
```

功能：此类为 [DataModel](serialization_package_classes.md#class-datamodel) 的子类，实现对 Bool 类型数据的封装。

父类型：

- [DataModel](#class-datamodel)

### init(Bool)

```cangjie
public init(bv: Bool)
```

功能：构造一个具有初始数据的 [DataModelBool](serialization_package_classes.md#class-datamodelbool) 实例。

参数：

- bv: Bool - 传入的 Bool 类型的数据。

### func getValue()

```cangjie
public func getValue(): Bool
```

功能：获取 [DataModelBool](serialization_package_classes.md#class-datamodelbool) 中的数据。

返回值：

- Bool - [DataModelBool](serialization_package_classes.md#class-datamodelbool) 中类型为 Bool 的 `value` 数值。

## class DataModelFloat

```cangjie
public class DataModelFloat <: DataModel {
    public init(fv: Float64)
    public init(v: Int64)
}
```

功能：此类为 [DataModel](serialization_package_classes.md#class-datamodel) 的子类，实现对 Float64 类型数据的封装。

父类型：

- [DataModel](#class-datamodel)

### init(Float64)

```cangjie
public init(fv: Float64)
```

功能：构造一个具有初始数据的 [DataModelFloat](serialization_package_classes.md#class-datamodelfloat) 实例。

参数：

- fv: Float64 - 传入的 Float64 类型的数据。

### init(Int64)

```cangjie
public init(v: Int64)
```

功能：构造一个具有初始数据的 [DataModelFloat](serialization_package_classes.md#class-datamodelfloat) 实例。

参数：

- v: Int64 - 传入的 Int64 类型的数据。

### func getValue()

```cangjie
public func getValue(): Float64
```

功能：获取 [DataModelFloat](serialization_package_classes.md#class-datamodelfloat) 中的数据。

返回值：

- Float64 - [DataModelFloat](serialization_package_classes.md#class-datamodelfloat) 中类型为 Float64 的 `value` 数值。

## class DataModelInt

```cangjie
public class DataModelInt <: DataModel {
    public init(iv: Int64)
}
```

功能：此类为 [DataModel](serialization_package_classes.md#class-datamodel) 的子类，实现对 Int64 类型数据的封装。

父类型：

- [DataModel](#class-datamodel)

### init(Int64)

```cangjie
public init(iv: Int64)
```

功能：构造一个具有初始数据的 [DataModelInt](serialization_package_classes.md#class-datamodelint) 实例。

参数：

- iv: Int64 - 传入的 Int64 类型的数据。

### func getValue()

```cangjie
public func getValue(): Int64
```

功能：获取 [DataModelInt](serialization_package_classes.md#class-datamodelint) 中的数据。

返回值：

- Int64 - [DataModelInt](serialization_package_classes.md#class-datamodelint) 中类型为 Int64 的 `value` 数值。

## class DataModelNull

```cangjie
public class DataModelNull <: DataModel
```

功能：此类为 [DataModel](serialization_package_classes.md#class-datamodel) 的子类，实现对 `Null` 类型数据的封装。

父类型：

- [DataModel](#class-datamodel)
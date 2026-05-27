## enum ValueType

```cangjie
public enum ValueType <: Equatable<ValueType> & ToString {
    | Integer(Int64)
    | Str(String)
    | ...
}
```

**功能：** 表示数据值类型，部分函数参数需要传入键值对，将`ValueType`作为值类型。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**父类型：**

- Equatable\<ValueType>
- ToString

### Integer(Int64)

```cangjie
Integer(Int64)
```

**功能：** 表示Int64的整型数据。

**起始版本：** 19

### Str(String)

```cangjie
Str(String)
```

**功能：** 表示字符串类型的数据。

**起始版本：** 19

### func !=(ValueType)

```cangjie
public operator func !=(other: ValueType): Bool
```

**功能：** 对数据值类型进行判不等。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ValueType](#enum-valuetype)|是|-|获取数据值类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果获取数据值类型不同，返回true，否则返回false。|

### func ==(ValueType)

```cangjie
public operator func ==(other: ValueType): Bool
```

**功能：** 对数据值类型进行判等。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ValueType](#enum-valuetype)|是|-|获取数据值类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果获取数据值类型同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回数据值类型的字符串表示。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|数据值类型的字符串表示。|
## enum DeliveryMode

```cangjie
public enum DeliveryMode <: Equatable<DeliveryMode> & ToString {
    | FAST_MODE
    | HIGH_QUALITY_MODE
    | BALANCE_MODE
    | ...
}
```

**功能：** 资源分发模式。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**父类型：**

- Equatable\<DeliveryMode>
- ToString

### BALANCE_MODE

```cangjie
BALANCE_MODE
```

**功能：** 均衡模式。

**起始版本：** 19

### FAST_MODE

```cangjie
FAST_MODE
```

**功能：** 快速模式。

**起始版本：** 19

### HIGH_QUALITY_MODE

```cangjie
HIGH_QUALITY_MODE
```

**功能：** 高质量模式。

**起始版本：** 19

### func !=(DeliveryMode)

```cangjie
public operator func !=(other: DeliveryMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeliveryMode](#enum-deliverymode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(DeliveryMode)

```cangjie
public operator func ==(other: DeliveryMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DeliveryMode](#enum-deliverymode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|

## enum DynamicRangeType

```cangjie
public enum DynamicRangeType <: Equatable<DynamicRangeType> & ToString {
    | SDR
    | HDR
    | ...
}
```

**功能：** 媒体文件的动态范围类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**父类型：**

- Equatable\<DynamicRangeType>
- ToString

### HDR

```cangjie
HDR
```

**功能：** 高动态范围类型。

**起始版本：** 19

### SDR

```cangjie
SDR
```

**功能：** 标准动态范围类型。

**起始版本：** 19

### func !=(DynamicRangeType)

```cangjie
public operator func !=(other: DynamicRangeType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DynamicRangeType](#enum-dynamicrangetype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(DynamicRangeType)

```cangjie
public operator func ==(other: DynamicRangeType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DynamicRangeType](#enum-dynamicrangetype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|
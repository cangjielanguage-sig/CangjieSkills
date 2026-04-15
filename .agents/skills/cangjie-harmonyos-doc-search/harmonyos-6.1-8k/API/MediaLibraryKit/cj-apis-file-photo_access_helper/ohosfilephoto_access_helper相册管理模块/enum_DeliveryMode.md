## enum DeliveryMode

```cangjie
public enum DeliveryMode <: Equatable<DeliveryMode> & ToString {
    | FastMode
    | HighQualityMode
    | BalanceMode
    | ...
}
```

**功能：** 枚举，资源分发模式。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**父类型：**

- Equatable\<DeliveryMode>
- ToString

### BalanceMode

```cangjie
BalanceMode
```

**功能：** 均衡模式。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### FastMode

```cangjie
FastMode
```

**功能：** 快速模式。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### HighQualityMode

```cangjie
HighQualityMode
```

**功能：** 高质量模式。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### func !=(DeliveryMode)

```cangjie
public operator func !=(other: DeliveryMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

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

**起始版本：** 22

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

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|
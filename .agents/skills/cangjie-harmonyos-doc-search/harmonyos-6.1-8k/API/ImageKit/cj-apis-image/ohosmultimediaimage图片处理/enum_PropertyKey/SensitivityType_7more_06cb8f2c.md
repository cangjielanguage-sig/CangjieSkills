### SensitivityType

```cangjie
SensitivityType
```

**功能：** 灵敏度类型。

修改传参格式说明：修改时传入相应的数字或者字符串。

修改示例：`imageSource.modifyImageProperty(key,'1');`或`imageSource.modifyImageProperty(key,'Standard output sensitivity (SOS)');`

读取结果示例："Standard output sensitivity (SOS)"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### StandardOutputSensitivity

```cangjie
StandardOutputSensitivity
```

**功能：** 标准输出灵敏度。

修改传参格式说明：非负整数字符串。

修改示例：`imageSource.modifyImageProperty(key,'400');`

读取结果示例："400"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### UserComment

```cangjie
UserComment
```

**功能：** 用户注释。

修改传参格式说明：字符串。

修改示例：`imageSource.modifyImageProperty(key,'User Comment');`

读取结果示例："User Comment"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### WhiteBalance

```cangjie
WhiteBalance
```

**功能：** 白平衡。

0："Auto white balance"，自动白平衡。

1："Manual white balance"，手动白平衡。

修改传参格式说明：修改时传入相应的数字或者字符串。

修改示例：`imageSource.modifyImageProperty(key,'0');`或`imageSource.modifyImageProperty(key,'Auto white balance');`

读取结果示例："Auto white balance"

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### func !=(PropertyKey)

```cangjie
public operator func !=(other: PropertyKey): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PropertyKey](#enum-propertykey)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(PropertyKey)

```cangjie
public operator func ==(other: PropertyKey): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PropertyKey](#enum-propertykey)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|
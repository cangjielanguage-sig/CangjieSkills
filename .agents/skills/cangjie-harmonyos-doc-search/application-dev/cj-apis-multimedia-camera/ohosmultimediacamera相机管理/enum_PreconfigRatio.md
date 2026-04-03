## enum PreconfigRatio

```cangjie
public enum PreconfigRatio {
    | PreconfigRatio_1_1
    | PreconfigRatio_4_3
    | PreconfigRatio_16_9
    | ...
}
```

**功能：** 枚举，提供预配置的分辨率比例。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- Equatable\<PreconfigRatio>
- ToString

### PreconfigRatio_16_9

```cangjie
PreconfigRatio_16_9
```

**功能：** 16:9画幅。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### PreconfigRatio_1_1

```cangjie
PreconfigRatio_1_1
```

**功能：** 1:1画幅。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### PreconfigRatio_4_3

```cangjie
PreconfigRatio_4_3
```

**功能：** 4:3画幅。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func !=(PreconfigRatio)

```cangjie
public operator func !=(other: PreconfigRatio): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PreconfigRatio](#enum-preconfigratio)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(PreconfigRatio)

```cangjie
public operator func ==(other: PreconfigRatio): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PreconfigRatio](#enum-preconfigratio)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的字符串值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的字符串值。|
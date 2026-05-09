## enum QualityLevel

```cangjie
public enum QualityLevel {
    | QualityLevelHigh
    | QualityLevelMedium
    | QualityLevelLow
    | ...
}
```

**功能：** 枚举，图片质量。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- Equatable\<QualityLevel>
- ToString

### QualityLevelHigh

```cangjie
QualityLevelHigh
```

**功能：** 图片质量高。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### QualityLevelLow

```cangjie
QualityLevelLow
```

**功能：** 图片质量差。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### QualityLevelMedium

```cangjie
QualityLevelMedium
```

**功能：** 图片质量中等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func !=(QualityLevel)

```cangjie
public operator func !=(other: QualityLevel): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[QualityLevel](#enum-qualitylevel)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(QualityLevel)

```cangjie
public operator func ==(other: QualityLevel): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[QualityLevel](#enum-qualitylevel)|是|-|另一个枚举值。|

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
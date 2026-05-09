## enum VideoStabilizationMode

```cangjie
public enum VideoStabilizationMode {
    | Off
    | Low
    | Middle
    | High
    | Auto
    | ...
}
```

**功能：** 枚举，视频防抖模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- Equatable\<VideoStabilizationMode>
- ToString

### Auto

```cangjie
Auto
```

**功能：** 自动进行选择防抖算法。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### High

```cangjie
High
```

**功能：** 使用防抖效果最好的防抖算法，防抖效果优于Middle类型。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### Low

```cangjie
Low
```

**功能：** 使用基础防抖算法。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### Middle

```cangjie
Middle
```

**功能：** 使用防抖效果一般的防抖算法，防抖效果优于Low类型。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### Off

```cangjie
Off
```

**功能：** 关闭视频防抖功能。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func !=(VideoStabilizationMode)

```cangjie
public operator func !=(other: VideoStabilizationMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[VideoStabilizationMode](#enum-videostabilizationmode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(VideoStabilizationMode)

```cangjie
public operator func ==(other: VideoStabilizationMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[VideoStabilizationMode](#enum-videostabilizationmode)|是|-|另一个枚举值。|

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
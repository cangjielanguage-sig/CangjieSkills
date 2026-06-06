## enum VideoStabilizationMode

```cangjie
public enum VideoStabilizationMode <: Equatable<VideoStabilizationMode> & ToString {
    | OFF
    | LOW
    | MIDDLE
    | HIGH
    | AUTO
    | ...
}
```

**功能：** 视频防抖模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- Equatable\<VideoStabilizationMode>
- ToString

### AUTO

```cangjie
AUTO
```

**功能：** 自动进行选择。

**起始版本：** 19

### HIGH

```cangjie
HIGH
```

**功能：** 使用防抖效果最好的防抖算法，防抖效果优于MIDDLE类型。

**起始版本：** 19

### LOW

```cangjie
LOW
```

**功能：** 关闭视频防抖功能。

**起始版本：** 19

### MIDDLE

```cangjie
MIDDLE
```

**功能：** 使用防抖效果一般的防抖算法，防抖效果优于LOW类型。

**起始版本：** 19

### OFF

```cangjie
OFF
```

**功能：** 关闭视频防抖功能。

**起始版本：** 19

### func !=(VideoStabilizationMode)

```cangjie
public operator func !=(other: VideoStabilizationMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

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

**起始版本：** 19

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

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|
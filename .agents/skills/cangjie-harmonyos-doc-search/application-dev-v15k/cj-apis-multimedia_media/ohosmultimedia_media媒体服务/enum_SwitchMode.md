## enum SwitchMode

```cangjie
public enum SwitchMode <: ToString & Equatable<SwitchMode> {
    | SMOOTH
    | SEGMENT
    | CLOSEST
    | ...
}
```

**功能：** 视频播放的selectTrack模式枚举，可通过selectTrack方法作为参数传递下去，当前仅DASH协议视频轨支持该扩展参数。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<SwitchMode>

### CLOSEST

```cangjie
CLOSEST
```

**功能：** 表示从距离当前播放时间点最近的帧开始播放，该模式立即切换，切换后会卡住3到5s，然后恢复播放。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### SEGMENT

```cangjie
SEGMENT
```

**功能：** 表示切换后从当前分片开始位置播放，该模式立即切换，会有重复播放。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### SMOOTH

```cangjie
SMOOTH
```

**功能：** 表示切换后视频平滑播放，该模式切换存在延迟，不会立即生效。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### func !=(SwitchMode)

```cangjie
public operator func !=(other: SwitchMode): Bool
```

**功能：** 判断两个SwitchMode是否不等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SwitchMode](#enum-switchmode)|是|-|另一SwitchMode。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个SwitchMode不等返回true，否则返回false。|

### func ==(SwitchMode)

```cangjie
public operator func ==(other: SwitchMode): Bool
```

**功能：** 判断两个SwitchMode是否相等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SwitchMode](#enum-switchmode)|是|-|另一SwitchMode。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个SwitchMode相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回SwitchMode的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|SwitchMode的字符串表示。|
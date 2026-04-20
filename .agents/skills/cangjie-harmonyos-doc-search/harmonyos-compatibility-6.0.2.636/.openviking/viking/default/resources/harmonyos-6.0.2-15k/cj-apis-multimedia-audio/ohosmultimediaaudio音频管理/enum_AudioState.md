## enum AudioState

```cangjie
public enum AudioState <: Equatable<AudioState> & ToString {
    | STATE_INVALID
    | STATE_NEW
    | STATE_PREPARED
    | STATE_RUNNING
    | STATE_STOPPED
    | STATE_RELEASED
    | STATE_PAUSED
    | ...
}
```

**功能：** 音频状态。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**父类型：**

- Equatable\<[AudioState](#enum-audiostate)>
- ToString

### STATE_INVALID

```cangjie
STATE_INVALID
```

**功能：** 无效状态。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### STATE_NEW

```cangjie
STATE_NEW
```

**功能：** 创建新实例状态。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### STATE_PAUSED

```cangjie
STATE_PAUSED
```

**功能：** 暂停状态。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### STATE_PREPARED

```cangjie
STATE_PREPARED
```

**功能：** 准备状态。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### STATE_RELEASED

```cangjie
STATE_RELEASED
```

**功能：** 释放状态。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### STATE_RUNNING

```cangjie
STATE_RUNNING
```

**功能：** 运行状态。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### STATE_STOPPED

```cangjie
STATE_STOPPED
```

**功能：** 停止状态。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioState)

```cangjie
public operator func !=(other: AudioState): Bool
```

**功能：** 对音频状态枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioState](#enum-audiostate)|是|-|音频状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频状态不同，返回true，否则返回false。|

### func ==(AudioState)

```cangjie
public operator func ==(other: AudioState): Bool
```

**功能：** 对音频状态枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioState](#enum-audiostate)|是|-|音频状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频状态相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取音频状态枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|音频状态枚举值的字符串表示。|
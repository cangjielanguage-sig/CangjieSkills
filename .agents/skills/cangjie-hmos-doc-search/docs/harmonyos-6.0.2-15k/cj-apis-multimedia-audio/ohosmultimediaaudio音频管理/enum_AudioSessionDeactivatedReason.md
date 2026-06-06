## enum AudioSessionDeactivatedReason

```cangjie
public enum AudioSessionDeactivatedReason <: Equatable<AudioSessionDeactivatedReason> & ToString {
    | DEACTIVATED_LOWER_PRIORITY
    | DEACTIVATED_TIMEOUT
    | ...
}
```

**功能：** 音频会话停用原因。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**父类型：**

- Equatable\<[AudioSessionDeactivatedReason](#enum-audiosessiondeactivatedreason)>
- ToString

### DEACTIVATED_LOWER_PRIORITY

```cangjie
DEACTIVATED_LOWER_PRIORITY
```

**功能：** 应用焦点被抢占。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### DEACTIVATED_TIMEOUT

```cangjie
DEACTIVATED_TIMEOUT
```

**功能：** 应用停流后超时。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioSessionDeactivatedReason)

```cangjie
public operator func !=(other: AudioSessionDeactivatedReason): Bool
```

**功能：** 对音频会话停用原因枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioSessionDeactivatedReason](#enum-audiosessiondeactivatedreason)|是|-|音频会话停用原因。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频会话停用原因不同，返回true，否则返回false。|

### func ==(AudioSessionDeactivatedReason)

```cangjie
public operator func ==(other: AudioSessionDeactivatedReason): Bool
```

**功能：** 对音频会话停用原因枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioSessionDeactivatedReason](#enum-audiosessiondeactivatedreason)|是|-|音频会话停用原因。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频会话停用原因相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取音频会话停用原因枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|音频会话停用原因枚举值的字符串表示。|
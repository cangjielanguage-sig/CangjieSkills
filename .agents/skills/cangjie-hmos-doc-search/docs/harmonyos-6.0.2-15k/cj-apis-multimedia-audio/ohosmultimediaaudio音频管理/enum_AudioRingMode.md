## enum AudioRingMode

```cangjie
public enum AudioRingMode <: Equatable<AudioRingMode> & ToString {
    | RINGER_MODE_SILENT
    | RINGER_MODE_VIBRATE
    | RINGER_MODE_NORMAL
    | ...
}
```

**功能：** 铃声模式。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**起始版本：** 19

**父类型：**

- Equatable\<[AudioRingMode](#enum-audioringmode)>
- ToString

### RINGER_MODE_NORMAL

```cangjie
RINGER_MODE_NORMAL
```

**功能：** 响铃模式。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### RINGER_MODE_SILENT

```cangjie
RINGER_MODE_SILENT
```

**功能：** 静音模式。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### RINGER_MODE_VIBRATE

```cangjie
RINGER_MODE_VIBRATE
```

**功能：** 震动模式。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioRingMode)

```cangjie
public operator func !=(other: AudioRingMode): Bool
```

**功能：** 对铃声模式枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioRingMode](#enum-audioringmode)|是|-|铃声模式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果铃声模式不同，返回true，否则返回false。|

### func ==(AudioRingMode)

```cangjie
public operator func ==(other: AudioRingMode): Bool
```

**功能：** 对铃声模式枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioRingMode](#enum-audioringmode)|是|-|铃声模式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果铃声模式相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取铃声模式枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|音频声道枚举值的字符串表示。|
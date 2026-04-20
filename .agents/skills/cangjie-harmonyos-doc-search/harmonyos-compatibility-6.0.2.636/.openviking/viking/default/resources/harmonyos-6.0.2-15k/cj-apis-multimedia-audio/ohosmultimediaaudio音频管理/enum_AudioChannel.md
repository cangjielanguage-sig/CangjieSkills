## enum AudioChannel

```cangjie
public enum AudioChannel <: Equatable<AudioChannel> & ToString {
    | CHANNEL_1
    | CHANNEL_2
    | CHANNEL_3
    | CHANNEL_4
    | CHANNEL_5
    | CHANNEL_6
    | CHANNEL_7
    | CHANNEL_8
    | CHANNEL_9
    | CHANNEL_10
    | CHANNEL_12
    | CHANNEL_14
    | CHANNEL_16
    | ...
}
```

**功能：** 音频声道。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**父类型：**

- Equatable\<[AudioChannel](#enum-audiochannel)>
- ToString

### CHANNEL_1

```cangjie
CHANNEL_1
```

**功能：** 单声道。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CHANNEL_10

```cangjie
CHANNEL_10
```

**功能：** 十声道。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CHANNEL_12

```cangjie
CHANNEL_12
```

**功能：** 十二声道。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CHANNEL_14

```cangjie
CHANNEL_14
```

**功能：** 十四声道。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CHANNEL_16

```cangjie
CHANNEL_16
```

**功能：** 十六声道。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CHANNEL_2

```cangjie
CHANNEL_2
```

**功能：** 双声道。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CHANNEL_3

```cangjie
CHANNEL_3
```

**功能：** 三声道。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CHANNEL_4

```cangjie
CHANNEL_4
```

**功能：** 四声道。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CHANNEL_5

```cangjie
CHANNEL_5
```

**功能：** 五声道。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CHANNEL_6

```cangjie
CHANNEL_6
```

**功能：** 六声道。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CHANNEL_7

```cangjie
CHANNEL_7
```

**功能：** 七声道。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CHANNEL_8

```cangjie
CHANNEL_8
```

**功能：** 八声道。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### CHANNEL_9

```cangjie
CHANNEL_9
```

**功能：** 九声道。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioChannel)

```cangjie
public operator func !=(other: AudioChannel): Bool
```

**功能：** 对音频声道枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioChannel](#enum-audiochannel)|是|-|音频声道。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频声道不同，返回true，否则返回false。|

### func ==(AudioChannel)

```cangjie
public operator func ==(other: AudioChannel): Bool
```

**功能：** 对音频声道枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioChannel](#enum-audiochannel)|是|-|音频声道。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频声道相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取音频声道枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|音频声道枚举值的字符串表示。|
## enum AudioErrors

```cangjie
public enum AudioErrors <: Equatable<AudioErrors> & ToString {
    | ERROR_INVALID_PARAM
    | ERROR_NO_MEMORY
    | ERROR_ILLEGAL_STATE
    | ERROR_UNSUPPORTED
    | ERROR_TIMEOUT
    | ERROR_STREAM_LIMIT
    | ERROR_SYSTEM
    | ...
}
```

**功能：** 音频错误码。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**父类型：**

- Equatable\<[AudioErrors](#enum-audioerrors)>
- ToString

### ERROR_ILLEGAL_STATE

```cangjie
ERROR_ILLEGAL_STATE
```

**功能：** 状态不支持。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### ERROR_INVALID_PARAM

```cangjie
ERROR_INVALID_PARAM
```

**功能：** 无效入参。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### ERROR_NO_MEMORY

```cangjie
ERROR_NO_MEMORY
```

**功能：** 分配内存失败。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### ERROR_STREAM_LIMIT

```cangjie
ERROR_STREAM_LIMIT
```

**功能：** 音频流数量达到限制。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### ERROR_SYSTEM

```cangjie
ERROR_SYSTEM
```

**功能：** 系统处理异常。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### ERROR_TIMEOUT

```cangjie
ERROR_TIMEOUT
```

**功能：** 处理超时。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### ERROR_UNSUPPORTED

```cangjie
ERROR_UNSUPPORTED
```

**功能：** 参数选项不支持。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioErrors)

```cangjie
public operator func !=(other: AudioErrors): Bool
```

**功能：** 对音频错误码枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioErrors](#enum-audioerrors)|是|-|音频错误码。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频错误码不同，返回true，否则返回false。|

### func ==(AudioErrors)

```cangjie
public operator func ==(other: AudioErrors): Bool
```

**功能：** 对音频错误码枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioErrors](#enum-audioerrors)|是|-|音频错误码。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频错误码相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取音频错误码枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|音频错误码枚举值的字符串表示。|
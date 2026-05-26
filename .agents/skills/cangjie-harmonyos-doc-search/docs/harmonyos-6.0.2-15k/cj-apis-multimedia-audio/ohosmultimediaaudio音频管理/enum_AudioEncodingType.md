## enum AudioEncodingType

```cangjie
public enum AudioEncodingType <: Equatable<AudioEncodingType> & ToString {
    | ENCODING_TYPE_INVALID
    | ENCODING_TYPE_RAW
    | ...
}
```

**功能：** 音频编码类型。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**父类型：**

- Equatable\<[AudioEncodingType](#enum-audioencodingtype)>
- ToString

### ENCODING_TYPE_INVALID

```cangjie
ENCODING_TYPE_INVALID
```

**功能：** 无效。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### ENCODING_TYPE_RAW

```cangjie
ENCODING_TYPE_RAW
```

**功能：** PCM编码。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioEncodingType)

```cangjie
public operator func !=(other: AudioEncodingType): Bool
```

**功能：** 对音频编码类型枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioEncodingType](#enum-audioencodingtype)|是|-|音频编码类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频编码类型不同，返回true，否则返回false。|

### func ==(AudioEncodingType)

```cangjie
public operator func ==(other: AudioEncodingType): Bool
```

**功能：** 对音频编码类型枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioEncodingType](#enum-audioencodingtype)|是|-|音频编码类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频编码类型相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取音频编码类型枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|音频编码类型枚举值的字符串表示。|
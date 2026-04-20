## enum AudioDataCallbackResult

```cangjie
public enum AudioDataCallbackResult <: Equatable<AudioDataCallbackResult> & ToString {
    | INVALID
    | VALID
    | ...
}
```

**功能：** 表示音频数据回调的结果。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**父类型：**

- Equatable\<[AudioDataCallbackResult](#enum-audiodatacallbackresult)>
- ToString

### INVALID

```cangjie
INVALID
```

**功能：** 表示该回调数据无效。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### VALID

```cangjie
VALID
```

**功能：** 表示该回调数据有效。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioDataCallbackResult)

```cangjie
public operator func !=(other: AudioDataCallbackResult): Bool
```

**功能：** 对音频数据回调结果枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioDataCallbackResult](#enum-audiodatacallbackresult)|是|-|音频数据回调结果。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频数据回调结果不同，返回true，否则返回false。|

### func ==(AudioDataCallbackResult)

```cangjie
public operator func ==(other: AudioDataCallbackResult): Bool
```

**功能：** 对音频数据回调结果枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioDataCallbackResult](#enum-audiodatacallbackresult)|是|-|音频数据回调结果。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频数据回调结果相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取音频数据回调结果枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|音频数据回调结果枚举值的字符串表示。|
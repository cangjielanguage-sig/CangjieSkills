## enum AudioPrivacyType

```cangjie
public enum AudioPrivacyType <: Equatable<AudioPrivacyType> & ToString {
    | PRIVACY_TYPE_PUBLIC
    | PRIVACY_TYPE_PRIVATE
    | ...
}
```

**功能：** 用于标识对应播放音频流是否支持被其他应用录制。

**系统能力：** SystemCapability.Multimedia.Audio.PlaybackCapture

**起始版本：** 19

**父类型：**

- Equatable\<[AudioPrivacyType](#enum-audioprivacytype)>
- ToString

### PRIVACY_TYPE_PRIVATE

```cangjie
PRIVACY_TYPE_PRIVATE
```

**功能：** 表示音频流不可以被其他应用录制。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### PRIVACY_TYPE_PUBLIC

```cangjie
PRIVACY_TYPE_PUBLIC
```

**功能：** 表示音频流可以被其他应用录制。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioPrivacyType)

```cangjie
public operator func !=(other: AudioPrivacyType): Bool
```

**功能：** 对枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.PlaybackCapture

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioPrivacyType](#enum-audioprivacytype)|是|-|标识对应播放音频流是否支持被其他应用录制。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果枚举值不同，返回true，否则返回false。|

### func ==(AudioPrivacyType)

```cangjie
public operator func ==(other: AudioPrivacyType): Bool
```

**功能：** 对该枚举类型的枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.PlaybackCapture

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioPrivacyType](#enum-audioprivacytype)|是|-|标识对应播放音频流是否支持被其他应用录制。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果枚举值相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取该枚举类型枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.PlaybackCapture

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表示。|
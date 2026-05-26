## enum AVSessionType

```cangjie
public enum AVSessionType <: ToString & Equatable<AVSessionType> {
    | SESSION_TYPE_AUDIO
    | SESSION_TYPE_VIDEO
    | SESSION_TYPE_VOICE_CALL
    | SESSION_TYPE_VIDEO_CALL
    | ...
}
```

**功能：** 当前会话支持的会话类型。该类型可取的值为下表字符串。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<[AVSessionType](#enum-avsessiontype)>

### SESSION_TYPE_AUDIO

```cangjie
SESSION_TYPE_AUDIO
```

**功能：** 音频。

**起始版本：** 19

### SESSION_TYPE_VIDEO

```cangjie
SESSION_TYPE_VIDEO
```

**功能：** 视频。

**起始版本：** 19

### SESSION_TYPE_VIDEO_CALL

```cangjie
SESSION_TYPE_VIDEO_CALL
```

**功能：** 视频通话。

**起始版本：** 19

### SESSION_TYPE_VOICE_CALL

```cangjie
SESSION_TYPE_VOICE_CALL
```

**功能：** 音频通话。

**起始版本：** 19

### func !=(AVSessionType)

```cangjie
public operator func !=(other: AVSessionType): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVSessionType](#enum-avsessiontype)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(AVSessionType)

```cangjie
public operator func ==(other: AVSessionType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVSessionType](#enum-avsessiontype)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表示。|
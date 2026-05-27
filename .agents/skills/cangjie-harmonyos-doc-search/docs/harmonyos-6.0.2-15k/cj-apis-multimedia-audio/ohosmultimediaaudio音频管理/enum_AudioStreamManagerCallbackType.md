## enum AudioStreamManagerCallbackType

```cangjie
public enum AudioStreamManagerCallbackType <: Equatable<AudioStreamManagerCallbackType> & Hashable & ToString {
    | CAPTURER_CHANGE
    | RENDERER_CHANGE
    | ...
}
```

**功能：** [AudioStreamManager](#class-audiostreammanager)的callback类型。

**系统能力：** 详见各枚举值

**起始版本：** 19

**父类型：**

- Equatable\<[AudioStreamManagerCallbackType](#enum-audiostreammanagercallbacktype)>
- Hashable
- ToString

### CAPTURER_CHANGE

```cangjie
CAPTURER_CHANGE
```

**功能：** 音频采集器更改事件。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

### RENDERER_CHANGE

```cangjie
RENDERER_CHANGE
```

**功能：** 音频渲染器更改事件。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### func !=(AudioStreamManagerCallbackType)

```cangjie
public operator func !=(other: AudioStreamManagerCallbackType): Bool
```

**功能：** 对回调事件类型进行判不等。

**系统能力：** 详见各枚举值

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioStreamManagerCallbackType](#enum-audiostreammanagercallbacktype)|是|-| 相比较的回调事件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果俩回调事件类型不同返回true，否则返回false。|

### func ==(AudioStreamManagerCallbackType)

```cangjie
public operator func ==(other: AudioStreamManagerCallbackType): Bool
```

**功能：** 详见各枚举值

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioStreamManagerCallbackType](#enum-audiostreammanagercallbacktype)|是|-|相比较的回调事件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果俩回调事件类型相同返回true，否则返回false。|

### func hashCode()

```cangjie
public func hashCode(): Int64
```

**功能：** 获取回调事件类型的哈希值。

**系统能力：** 详见各枚举值

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int64|回调事件类型的哈希值。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回回调事件的字符串表示。

**系统能力：** 详见各枚举值

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|事件的字符串表示。|
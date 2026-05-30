## enum AudioRoutingManagerCallbackType

```cangjie
public enum AudioRoutingManagerCallbackType <: Equatable<AudioRoutingManagerCallbackType> & Hashable & ToString {
    | DEVICE_CHANGE
    | AVAILABLE_DEVICE_CHANGE
    | PREFERRED_INPUT_DEVICE_CHANGE_FOR_CAPTURER_INFO
    | PREFERR_OUTPUT_DEVICE_CHANGE_FOR_RENDERER_INFO
    | ...
}
```

**功能：** [AudioRoutingManager](#class-audioroutingmanager)的callback类型。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**父类型：**

- Equatable\<[AudioRoutingManagerCallbackType](#enum-audioroutingmanagercallbacktype)>
- Hashable
- ToString

### AVAILABLE_DEVICE_CHANGE

```cangjie
AVAILABLE_DEVICE_CHANGE
```

**功能：** 音频可选设备连接变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### DEVICE_CHANGE

```cangjie
DEVICE_CHANGE
```

**功能：** 音频设备连接变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### PREFERRED_INPUT_DEVICE_CHANGE_FOR_CAPTURER_INFO

```cangjie
PREFERRED_INPUT_DEVICE_CHANGE_FOR_CAPTURER_INFO
```

**功能：** 最高优先级输入设备变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### PREFERR_OUTPUT_DEVICE_CHANGE_FOR_RENDERER_INFO

```cangjie
PREFERR_OUTPUT_DEVICE_CHANGE_FOR_RENDERER_INFO
```

**功能：** 最高优先级输出设备变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioRoutingManagerCallbackType)

```cangjie
public operator func !=(other: AudioRoutingManagerCallbackType): Bool
```

**功能：** 对回调事件类型进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioRoutingManagerCallbackType](#enum-audioroutingmanagercallbacktype)|是|-|相比较的回调事件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果俩回调事件类型不同返回true，否则返回false。|

### func ==(AudioRoutingManagerCallbackType)

```cangjie
public operator func ==(other: AudioRoutingManagerCallbackType): Bool
```

**功能：** 对回调事件类型进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioRoutingManagerCallbackType](#enum-audioroutingmanagercallbacktype)|是|-|相比较的回调事件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果俩回调事件类型相同返回true，否则返回false。|

### func hashCode()

```cangjie
public func hashCode(): Int64
```

**功能：** 获取回调事件类型的哈希值。

**系统能力：** SystemCapability.Multimedia.Audio.Device

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

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|事件的字符串表示。|
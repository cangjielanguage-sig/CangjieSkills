## enum AudioVolumeManagerCallbackType

```cangjie
public enum AudioVolumeManagerCallbackType <: Equatable<AudioVolumeManagerCallbackType> & Hashable & ToString {
    | VOLUME_CHANGE
    | ...
}
```

**功能：** [AudioVolumeGroupManager](#class-audiovolumegroupmanager)的callback类型。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**父类型：**

- Equatable\<[AudioVolumeManagerCallbackType](#enum-audiovolumemanagercallbacktype)>
- Hashable
- ToString

### VOLUME_CHANGE

```cangjie
VOLUME_CHANGE
```

**功能：** 音量变化改变事件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioVolumeManagerCallbackType)

```cangjie
public operator func !=(other: AudioVolumeManagerCallbackType): Bool
```

**功能：** 对回调事件类型进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioVolumeManagerCallbackType](#enum-audiovolumemanagercallbacktype)|是|-|相比较的回调事件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果俩回调事件类型不同返回true，否则返回false。|

### func ==(AudioVolumeManagerCallbackType)

```cangjie
public operator func ==(other: AudioVolumeManagerCallbackType): Bool
```

**功能：** 对回调事件类型进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioVolumeManagerCallbackType](#enum-audiovolumemanagercallbacktype)|是|-|相比较的回调事件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果俩回调事件类型相同返回true，否则返回false。|

### func hashCode()

```cangjie
public func hashCode(): Int64
```

**功能：** 获取回调事件类型的哈希值。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

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

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|事件的字符串表示。|
## enum AudioVolumeGroupManagerCallbackType

```cangjie
public enum AudioVolumeGroupManagerCallbackType <: Equatable<AudioVolumeGroupManagerCallbackType> & Hashable & ToString {
    | RING_MODE_CHANGE
    | MICSTATE_CHANGE
    | ...
}
```

**功能：** [AudioVolumeGroupManager](#class-audiovolumegroupmanager)的callback类型。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**父类型：**

- Equatable\<[AudioVolumeGroupManagerCallbackType](#enum-audiovolumegroupmanagercallbacktype)>
- Hashable
- ToString

### MICSTATE_CHANGE

```cangjie
MICSTATE_CHANGE
```

**功能：** 麦克风状态改变事件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### RING_MODE_CHANGE

```cangjie
RING_MODE_CHANGE
```

**功能：** 铃声模式状态改变事件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(AudioVolumeGroupManagerCallbackType)

```cangjie
public operator func !=(other: AudioVolumeGroupManagerCallbackType): Bool
```

**功能：** 对回调事件类型进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioVolumeGroupManagerCallbackType](#enum-audiovolumegroupmanagercallbacktype)|是|-| 相比较的回调事件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果俩回调事件类型不同返回true，否则返回false。|

### func ==(AudioVolumeGroupManagerCallbackType)

```cangjie
public operator func ==(other: AudioVolumeGroupManagerCallbackType): Bool
```

**功能：** 对回调事件类型进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AudioVolumeGroupManagerCallbackType](#enum-audiovolumegroupmanagercallbacktype)|是|-|相比较的回调事件类型。|

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
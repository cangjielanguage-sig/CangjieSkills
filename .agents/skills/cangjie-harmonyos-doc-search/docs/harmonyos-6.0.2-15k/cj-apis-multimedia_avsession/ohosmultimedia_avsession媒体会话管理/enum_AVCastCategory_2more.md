## enum AVCastCategory

```cangjie
public enum AVCastCategory <: Equatable<AVCastCategory> & ToString {
    | CATEGORY_LOCAL
    | CATEGORY_REMOTE
    | ...
}
```

**功能：** 投播的类别枚举。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

**父类型：**

- Equatable\<[AVCastCategory](#enum-avcastcategory)>
- ToString

### CATEGORY_LOCAL

```cangjie
CATEGORY_LOCAL
```

**功能：** 本地播放，默认播放设备，声音从本机或者连接的蓝牙耳机设备出声。

**起始版本：** 19

### CATEGORY_REMOTE

```cangjie
CATEGORY_REMOTE
```

**功能：** 远端播放，远端播放设备，声音从其他设备发出声音或者画面。

**起始版本：** 19

### func !=(AVCastCategory)

```cangjie
public operator func !=(other: AVCastCategory): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVCastCategory](#enum-avcastcategory)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(AVCastCategory)

```cangjie
public operator func ==(other: AVCastCategory): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVCastCategory](#enum-avcastcategory)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表示。|

## enum AVCastControlCommandParameterType

```cangjie
public enum AVCastControlCommandParameterType {
    | INT32(Int32)
    | SPEED(PlaybackSpeed)
    | LOOP_MODE(LoopMode)
    | ...
}
```

**功能：** 投播控制器可传递的命令参数类型。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### INT32(Int32)

```cangjie
INT32(Int32)
```

**功能：** Int32值类型。

**起始版本：** 19

### LOOP_MODE(LoopMode)

```cangjie
LOOP_MODE(LoopMode)
```

**功能：** [LoopMode](#enum-loopmode)值类型。

**起始版本：** 19

### SPEED(PlaybackSpeed)

```cangjie
SPEED(PlaybackSpeed)
```

**功能：** [PlaybackSpeed](../MediaKit/cj-apis-multimedia_media.md#enum-playbackspeed)值类型。

**起始版本：** 19
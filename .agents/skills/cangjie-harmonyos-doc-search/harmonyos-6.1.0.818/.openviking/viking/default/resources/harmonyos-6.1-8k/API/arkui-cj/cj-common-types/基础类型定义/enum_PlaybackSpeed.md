## enum PlaybackSpeed

```cangjie
public enum PlaybackSpeed <: Equatable<PlaybackSpeed> {
    | SpeedForward075X
    | SpeedForward100X
    | SpeedForward125X
    | SpeedForward175X
    | SpeedForward200X
    | ...
}
```

**功能：** 定义播放速度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[PlaybackSpeed](#enum-playbackspeed)>

### SpeedForward075X

```cangjie
SpeedForward075X
```

**功能：** 0.75倍速播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### SpeedForward100X

```cangjie
SpeedForward100X
```

**功能：** 1.00倍速播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### SpeedForward125X

```cangjie
SpeedForward125X
```

**功能：** 1.25倍速播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### SpeedForward175X

```cangjie
SpeedForward175X
```

**功能：** 1.75倍速播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### SpeedForward200X

```cangjie
SpeedForward200X
```

**功能：** 2.00倍速播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(PlaybackSpeed)

```cangjie
public operator func ==(other: PlaybackSpeed): Bool
```

**功能：** 判断两个PlaybackSpeed枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PlaybackSpeed](#enum-playbackspeed)|是|-|要比较的另一个PlaybackSpeed枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(PlaybackSpeed)

```cangjie
public operator func !=(other: PlaybackSpeed): Bool
```

**功能：** 判断两个PlaybackSpeed枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PlaybackSpeed](#enum-playbackspeed)|是|-|要比较的另一个PlaybackSpeed枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|
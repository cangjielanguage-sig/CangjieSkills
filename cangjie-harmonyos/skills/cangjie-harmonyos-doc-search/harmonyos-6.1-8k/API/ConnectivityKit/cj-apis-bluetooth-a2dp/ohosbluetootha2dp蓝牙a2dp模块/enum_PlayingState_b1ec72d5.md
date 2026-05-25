## enum PlayingState

```cangjie
public enum PlayingState <: Equatable<PlayingState> & ToString {
    | StateNotPlaying
    | StatePlaying
    | ...
}
```

**功能：** 蓝牙A2DP播放状态。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**父类型：**

- Equatable\<PlayingState>
- ToString

### StateNotPlaying

```cangjie
StateNotPlaying
```

**功能：** 表示未播放。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### StatePlaying

```cangjie
StatePlaying
```

**功能：** 表示正在播放。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### func !=(PlayingState)

```cangjie
public operator func !=(other: PlayingState): Bool
```

**功能：** 对蓝牙A2DP播放状态进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PlayingState](#enum-playingstate)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果蓝牙A2DP播放状态不同，返回true，否则返回false。|

### func ==(PlayingState)

```cangjie
public operator func ==(other: PlayingState): Bool
```

**功能：** 对蓝牙A2DP播放状态进行判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PlayingState](#enum-playingstate)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果蓝牙A2DP播放状态相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回枚举值的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表示。|
## enum AVRecorderState

```cangjie
public enum AVRecorderState <: Equatable<AVRecorderState> & ToString {
    | IDLE
    | PREPARED
    | STARTED
    | PAUSED
    | STOPPED
    | RELEASED
    | ERROR
    | ...
}
```

**功能：** 音视频录制的状态机。可通过state属性获取当前状态。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**父类型：**

- Equatable\<AVRecorderState>
- ToString

### ERROR

```cangjie
ERROR
```

**功能：** 错误状态。当AVRecorder实例发生不可逆错误，会转换至当前状态。切换至error状态时会伴随[AVRecorder.on(AVRECORDER_ERROR)](#func-onavrecordercallbacktype-callback1argumentbusinessexception)事件，该事件会上报详细错误原因。在error状态时，用户需要调用[AVRecorder.reset()](#func-reset)方法重置AVRecorder实例，或者调用[AVRecorder.release()](#func-release)方法释放资源。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### IDLE

```cangjie
IDLE
```

**功能：** 闲置状态。此时可以调用[AVRecorder.prepare()](#func-prepareavrecorderconfig)方法设置录制参数，进入prepared状态。AVRecorder刚被创建，或者在任何非released状态下调用[AVRecorder.reset()](#func-reset)方法，均进入idle状态。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### PAUSED

```cangjie
PAUSED
```

**功能：** 录制暂停。此时可以调用[AVRecorder.resume()](#func-resume)方法继续录制，进入started状态。也可以调用[AVRecorder.stop()](#func-stop)方法结束录制，进入stopped状态。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### PREPARED

```cangjie
PREPARED
```

**功能：** 参数设置完成。此时可以调用[AVRecorder.start()](#func-start)方法开始录制，进入started状态。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### RELEASED

```cangjie
RELEASED
```

**功能：** 录制资源释放。此时不能再进行任何操作。在任何其他状态下，均可以通过调用[AVRecorder.release()](#func-release)方法进入released状态。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### STARTED

```cangjie
STARTED
```

**功能：** 正在录制。此时可以调用[AVRecorder.pause()](#func-pause)方法暂停录制，进入paused状态。也可以调用[AVRecorder.stop()](#func-stop)方法结束录制，进入stopped状态。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### STOPPED

```cangjie
STOPPED
```

**功能：** 录制停止。此时可以调用[AVRecorder.prepare()](#func-prepareavrecorderconfig)方法设置录制参数，重新进入prepared状态。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### func !=(AVRecorderState)

```cangjie
public operator func !=(other: AVRecorderState): Bool
```

**功能：** 对音视频录制的状态进行判不等。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVRecorderState](#enum-avrecorderstate)|是|-|音视频录制的状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不相等，返回true，否则返回false。|

### func ==(AVRecorderState)

```cangjie
public operator func ==(other: AVRecorderState): Bool
```

**功能：** 对音视频录制的状态进行判等。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVRecorderState](#enum-avrecorderstate)|是|-|音视频录制的状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true，否则返回false。|
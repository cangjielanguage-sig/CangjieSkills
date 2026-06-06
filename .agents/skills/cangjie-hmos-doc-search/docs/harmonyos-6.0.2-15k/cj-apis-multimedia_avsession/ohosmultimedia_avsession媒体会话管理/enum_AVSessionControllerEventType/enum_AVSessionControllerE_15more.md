## enum AVSessionControllerEventType

```cangjie
public enum AVSessionControllerEventType <: ToString & Equatable<AVSessionControllerEventType> {
    | EVENT_SESSION_DESTROY
    | EVENT_PLAYBACK_STATE_CHANGE
    | EVENT_META_DATA_CHANGE
    | EVENT_ACTIVE_STATE_CHANGE
    | EVENT_VALID_COMMAND_CHANGE
    | EVENT_OUTPUT_DEVICE_CHANGE
    | EVENT_SESSION_EVENT_CHANGE
    | EVENT_QUEUE_ITEMS_CHANGE
    | EVENT_QUEUE_TITLE_CHANGE
    | EVENT_EXTRAS_CHANGE
    | EVENT_AVCALL_META_DATA_CHANGE
    | EVENT_AVCALL_STATE_CHANGE
    | ...
}
```

**功能：** 回调函数的事件类型。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<[AVSessionControllerEventType](#enum-avsessioncontrollereventtype)>

### EVENT_ACTIVE_STATE_CHANGE

```cangjie
EVENT_ACTIVE_STATE_CHANGE
```

**功能：** 会话的激活状态的监听事件。

**起始版本：** 19

### EVENT_AVCALL_META_DATA_CHANGE

```cangjie
EVENT_AVCALL_META_DATA_CHANGE
```

**功能：** 设置通话元数据变化的监听事件。

**起始版本：** 19

### EVENT_AVCALL_STATE_CHANGE

```cangjie
EVENT_AVCALL_STATE_CHANGE
```

**功能：** 设置通话状态变化的监听事件。

**起始版本：** 19

### EVENT_EXTRAS_CHANGE

```cangjie
EVENT_EXTRAS_CHANGE
```

**功能：** 媒体控制器设置自定义媒体数据包事件变化的监听器。

**起始版本：** 19

### EVENT_META_DATA_CHANGE

```cangjie
EVENT_META_DATA_CHANGE
```

**功能：** 媒体控制器取消监听元数据变化的事件。

**起始版本：** 19

### EVENT_OUTPUT_DEVICE_CHANGE

```cangjie
EVENT_OUTPUT_DEVICE_CHANGE
```

**功能：** 设置播放设备变化的监听事件。

**起始版本：** 19

### EVENT_PLAYBACK_STATE_CHANGE

```cangjie
EVENT_PLAYBACK_STATE_CHANGE
```

**功能：** 设置播放状态变化的监听事件。

**起始版本：** 19

### EVENT_QUEUE_ITEMS_CHANGE

```cangjie
EVENT_QUEUE_ITEMS_CHANGE
```

**功能：** 媒体控制器设置会话自定义播放列表变化的监听器。

**起始版本：** 19

### EVENT_QUEUE_TITLE_CHANGE

```cangjie
EVENT_QUEUE_TITLE_CHANGE
```

**功能：** 媒体控制器设置会话自定义播放列表的名称变化的监听器。

**起始版本：** 19

### EVENT_SESSION_DESTROY

```cangjie
EVENT_SESSION_DESTROY
```

**功能：** 会话销毁的监听事件。

**起始版本：** 19

### EVENT_SESSION_EVENT_CHANGE

```cangjie
EVENT_SESSION_EVENT_CHANGE
```

**功能：** 媒体控制器设置会话自定义事件变化的监听器。

**起始版本：** 19

### EVENT_VALID_COMMAND_CHANGE

```cangjie
EVENT_VALID_COMMAND_CHANGE
```

**功能：** 会话支持的有效命令变化监听事件。

**起始版本：** 19

### func !=(AVSessionControllerEventType)

```cangjie
public operator func !=(other: AVSessionControllerEventType): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVSessionControllerEventType](#enum-avsessioncontrollereventtype)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(AVSessionControllerEventType)

```cangjie
public operator func ==(other: AVSessionControllerEventType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVSessionControllerEventType](#enum-avsessioncontrollereventtype)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|
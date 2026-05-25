## enum InterruptHint

```cangjie
public enum InterruptHint <: Equatable<InterruptHint> & ToString {
    | INTERRUPT_HINT_NONE
    | INTERRUPT_HINT_RESUME
    | INTERRUPT_HINT_PAUSE
    | INTERRUPT_HINT_STOP
    | INTERRUPT_HINT_DUCK
    | INTERRUPT_HINT_UNDUCK
    | INTERRUPT_HINT_UNKNOWN
    | ...
}
```

**功能：** 中断提示。

当用户监听到音频中断（即收到[InterruptEvent](#class-interruptevent)事件）时，将获取此信息。

此类型表示根据焦点策略，当前需要对音频流的具体操作（如暂停、调整音量等）。

可以结合InterruptEvent中的[InterruptForceType](#enum-interruptforcetype)信息，判断该操作是否已由系统强制执行。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**父类型：**

- Equatable\<[InterruptHint](#enum-interrupthint)>
- ToString

### INTERRUPT_HINT_DUCK

```cangjie
INTERRUPT_HINT_DUCK
```

**功能：** 提示音频躲避开始，音频降低音量播放，而不会停止。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### INTERRUPT_HINT_NONE

```cangjie
INTERRUPT_HINT_NONE
```

**功能：** 无提示。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### INTERRUPT_HINT_PAUSE

```cangjie
INTERRUPT_HINT_PAUSE
```

**功能：** 提示音频暂停，暂时失去音频焦点。

后续待焦点可用时，会出现INTERRUPT_HINT_RESUME事件。

**起始版本：** 19

### INTERRUPT_HINT_RESUME

```cangjie
INTERRUPT_HINT_RESUME
```

**功能：** 提示音频恢复，应用可主动触发开始渲染或开始采集的相关操作。

此操作无法由系统强制执行，其对应的[InterruptForceType](#enum-interruptforcetype)一定为INTERRUPT_SHARE类型。

**起始版本：** 19

### INTERRUPT_HINT_STOP

```cangjie
INTERRUPT_HINT_STOP
```

**功能：** 提示音频停止，彻底失去音频焦点。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### INTERRUPT_HINT_UNDUCK

```cangjie
INTERRUPT_HINT_UNDUCK
```

**功能：** 提示音量躲避结束，音频恢复正常音量。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### INTERRUPT_HINT_UNKNOWN

```cangjie
INTERRUPT_HINT_UNKNOWN
```

**功能：** 未知类型的提示。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(InterruptHint)

```cangjie
public operator func !=(other: InterruptHint): Bool
```

**功能：** 对音频声道枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[InterruptHint](#enum-interrupthint)|是|-|中断提示。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果中断提示不同，返回true，否则返回false。|

### func ==(InterruptHint)

```cangjie
public operator func ==(other: InterruptHint): Bool
```

**功能：** 对音频声道枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[InterruptHint](#enum-interrupthint)|是|-|中断提示。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果中断提示相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取中断提示枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|中断提示枚举值的字符串表示。|
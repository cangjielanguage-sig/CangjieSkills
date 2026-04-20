## enum InterruptForceType

```cangjie
public enum InterruptForceType <: Equatable<InterruptForceType> & ToString {
    | INTERRUPT_FORCE
    | INTERRUPT_SHARE
    | ...
}
```

**功能：** 音频打断类型。

当用户监听到音频中断（即收到[InterruptEvent](#class-interruptevent)事件）时，将获取此信息。

此类型表示本次音频打断的操作是否已由系统强制执行，具体操作信息（如音频暂停、停止等）可通过[InterruptHint](#enum-interrupthint)获取。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**父类型：**

- Equatable\<[InterruptForceType](#enum-interruptforcetype)>
- ToString

### INTERRUPT_FORCE

```cangjie
INTERRUPT_FORCE
```

**功能：** 强制打断类型，即具体操作已由系统强制执行。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### INTERRUPT_SHARE

```cangjie
INTERRUPT_SHARE
```

**功能：** 共享打断类型，即系统不执行具体操作，通过[InterruptHint](#enum-interrupthint)提示并建议应用操作，应用可自行决策下一步处理方式。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(InterruptForceType)

```cangjie
public operator func !=(other: InterruptForceType): Bool
```

**功能：** 对音频打断类型枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[InterruptForceType](#enum-interruptforcetype)|是|-|音频打断类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频打断类型不同，返回true，否则返回false。|

### func ==(InterruptForceType)

```cangjie
public operator func ==(other: InterruptForceType): Bool
```

**功能：** 对音频打断类型枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[InterruptForceType](#enum-interruptforcetype)|是|-|音频打断类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果音频打断类型相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取音频打断类型枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|音频打断类型枚举值的字符串表示。|
## enum InterruptType

```cangjie
public enum InterruptType <: Equatable<InterruptType> & ToString {
    | INTERRUPT_TYPE_BEGIN
    | INTERRUPT_TYPE_END
    | ...
}
```

**功能：** 中断类型。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**父类型：**

- Equatable\<[InterruptType](#enum-interrupttype)>
- ToString

### INTERRUPT_TYPE_BEGIN

```cangjie
INTERRUPT_TYPE_BEGIN
```

**功能：** 音频播放中断事件开始。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### INTERRUPT_TYPE_END

```cangjie
INTERRUPT_TYPE_END
```

**功能：** 音频播放中断事件结束。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(InterruptType)

```cangjie
public operator func !=(other: InterruptType): Bool
```

**功能：** 对中断类型枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[InterruptType](#enum-interrupttype)|是|-|中断类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果中断类型不同，返回true，否则返回false。|

### func ==(InterruptType)

```cangjie
public operator func ==(other: InterruptType): Bool
```

**功能：** 对中断类型枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[InterruptType](#enum-interrupttype)|是|-|中断类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果中断类型相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取中断类型枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|中断类型枚举值的字符串表示。|
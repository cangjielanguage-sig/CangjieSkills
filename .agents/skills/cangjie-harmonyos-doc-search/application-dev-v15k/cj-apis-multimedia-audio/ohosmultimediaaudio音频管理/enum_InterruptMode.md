## enum InterruptMode

```cangjie
public enum InterruptMode <: Equatable<InterruptMode> & ToString {
    | SHARE_MODE
    | INDEPENDENT_MODE
    | ...
}
```

**功能：** 焦点模型。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**起始版本：** 19

**父类型：**

- Equatable\<[InterruptMode](#enum-interruptmode)>
- ToString

### INDEPENDENT_MODE

```cangjie
INDEPENDENT_MODE
```

**功能：** 独立焦点模式。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### SHARE_MODE

```cangjie
SHARE_MODE
```

**功能：** 共享焦点模式。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func !=(InterruptMode)

```cangjie
public operator func !=(other: InterruptMode): Bool
```

**功能：** 对焦点模型枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[InterruptMode](#enum-interruptmode)|是|-|焦点模型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果焦点模型不同，返回true，否则返回false。|

### func ==(InterruptMode)

```cangjie
public operator func ==(other: InterruptMode): Bool
```

**功能：** 对焦点模型枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[InterruptMode](#enum-interruptmode)|是|-|焦点模型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果焦点模型相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取焦点模型枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|焦点模型枚举值的字符串表示。|
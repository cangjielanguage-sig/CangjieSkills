## enum DisplayState

```cangjie
public enum DisplayState <: Equatable<DisplayState> {
    | StateUnknown
    | StateOff
    | StateOn
    | StateDoze
    | StateDozeSuspend
    | StateVr
    | StateOnSuspend
    | ...
}
```

**功能：** 枚举显示状态。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**父类型：**

- Equatable\<[DisplayState](#enum-displaystate)>

### StateUnknown

```cangjie
StateUnknown
```

**功能：** 未知状态。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### StateOff

```cangjie
StateOff
```

**功能：** 屏幕关闭。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### StateOn

```cangjie
StateOn
```

**功能：** 屏幕开启。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### StateDoze

```cangjie
StateDoze
```

**功能：** 屏幕打盹，但会针对部分重要系统消息进行更新。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### StateDozeSuspend

```cangjie
StateDozeSuspend
```

**功能：** 屏幕打盹且不更新。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### StateVr

```cangjie
StateVr
```

**功能：** VR模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### StateOnSuspend

```cangjie
StateOnSuspend
```

**功能：** 屏幕开启但不更新。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### operator func !=(DisplayState)

```cangjie
public operator func !=(other: DisplayState): Bool
```

**功能：** 不等比较运算符。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DisplayState](#enum-displaystate)|是|-|要比较的另一个DisplayState实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，不相等时返回true。|

### operator func ==(DisplayState)

```cangjie
public operator func ==(other: DisplayState): Bool
```

**功能：** 相等比较运算符。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DisplayState](#enum-displaystate)|是|-|要比较的另一个DisplayState实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，相等时返回true。|
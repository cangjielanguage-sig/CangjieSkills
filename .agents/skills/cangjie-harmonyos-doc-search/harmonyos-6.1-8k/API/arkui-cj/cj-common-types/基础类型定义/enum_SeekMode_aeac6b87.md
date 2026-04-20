## enum SeekMode

```cangjie
public enum SeekMode <: Equatable<SeekMode> {
    | PreviousKeyframe
    | NextKeyframe
    | ClosestKeyframe
    | Accurate
    | ...
}
```

**功能：** 跳转模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[SeekMode](#enum-seekmode)>

### PreviousKeyframe

```cangjie
PreviousKeyframe
```

**功能：** 跳转到前一个最近的关键帧。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### NextKeyframe

```cangjie
NextKeyframe
```

**功能：** 跳转到后一个最近的关键帧。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### ClosestKeyframe

```cangjie
ClosestKeyframe
```

**功能：** 跳转到最近的关键帧。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Accurate

```cangjie
Accurate
```

**功能：** 精准跳转，不论是否为关键帧。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(SeekMode)

```cangjie
public operator func ==(other: SeekMode): Bool
```

**功能：** 判断两个SeekMode枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SeekMode](#enum-seekmode)|是|-|要比较的另一个SeekMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(SeekMode)

```cangjie
public operator func !=(other: SeekMode): Bool
```

**功能：** 判断两个SeekMode枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SeekMode](#enum-seekmode)|是|-|要比较的另一个SeekMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|
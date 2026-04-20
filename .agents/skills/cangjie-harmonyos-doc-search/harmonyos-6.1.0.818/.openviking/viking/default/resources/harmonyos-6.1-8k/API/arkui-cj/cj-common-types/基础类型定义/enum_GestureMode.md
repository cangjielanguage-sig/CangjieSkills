## enum GestureMode

```cangjie
public enum GestureMode <: Equatable<GestureMode> {
    | Sequence
    | Parallel
    | Exclusive
    | ...
}
```

**功能：** 组合手势的识别模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[GestureMode](#enum-gesturemode)>

### Sequence

```cangjie
Sequence
```

**功能：** 顺序识别，按照手势的注册顺序识别手势，直到所有手势识别成功。若有一个手势识别失败，后续手势识别均失败。顺序识别手势组仅有最后一个手势可以响应onActionEnd。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Parallel

```cangjie
Parallel
```

**功能：** 并发识别，注册的手势同时识别，直到所有手势识别结束，手势识别互相不影响。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Exclusive

```cangjie
Exclusive
```

**功能：** 互斥识别，注册的手势同时识别，若有一个手势识别成功，则结束手势识别。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(GestureMode)

```cangjie
public operator func ==(other: GestureMode): Bool
```

**功能：** 判断两个GestureMode枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[GestureMode](#enum-gesturemode)|是|-|要比较的另一个GestureMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(GestureMode)

```cangjie
public operator func !=(other: GestureMode): Bool
```

**功能：** 判断两个GestureMode枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[GestureMode](#enum-gesturemode)|是|-|要比较的另一个GestureMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|
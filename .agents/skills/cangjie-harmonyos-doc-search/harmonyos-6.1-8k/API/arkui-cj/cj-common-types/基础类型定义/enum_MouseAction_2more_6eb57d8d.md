## enum MouseAction

```cangjie
public enum MouseAction <: Equatable<MouseAction> {
    | None
    | Press
    | Release
    | Move
    | Hover
    | ...
}
```

**功能：** 鼠标动作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[MouseAction](#enum-mouseaction)>

### None

```cangjie
None
```

**功能：** 无操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Press

```cangjie
Press
```

**功能：** 鼠标按键按下。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Release

```cangjie
Release
```

**功能：** 鼠标按键松开。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Move

```cangjie
Move
```

**功能：** 鼠标移动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Hover

```cangjie
Hover
```

**功能：** 鼠标悬浮。**说明：** 该枚举值无效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(MouseAction)

```cangjie
public operator func ==(other: MouseAction): Bool
```

**功能：** 判断两个MouseAction枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MouseAction](#enum-mouseaction)|是|-|要比较的另一个MouseAction枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(MouseAction)

```cangjie
public operator func !=(other: MouseAction): Bool
```

**功能：** 判断两个MouseAction枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MouseAction](#enum-mouseaction)|是|-|要比较的另一个MouseAction枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum SliderStyle

```cangjie
public enum SliderStyle <: Equatable<SliderStyle> {
    | OutSet
    | InSet
    | ...
}
```

**功能：** Slider的滑块与滑轨显示样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[SliderStyle](#enum-sliderstyle)>

### OutSet

```cangjie
OutSet
```

**功能：** 滑块在滑轨内。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### InSet

```cangjie
InSet
```

**功能：** 旋钮在内样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(SliderStyle)

```cangjie
public operator func ==(other: SliderStyle): Bool
```

**功能：** 判断两个SliderStyle枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SliderStyle](#enum-sliderstyle)|是|-|要比较的另一个SliderStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(SliderStyle)

```cangjie
public operator func !=(other: SliderStyle): Bool
```

**功能：** 判断两个SliderStyle枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SliderStyle](#enum-sliderstyle)|是|-|要比较的另一个SliderStyle枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|
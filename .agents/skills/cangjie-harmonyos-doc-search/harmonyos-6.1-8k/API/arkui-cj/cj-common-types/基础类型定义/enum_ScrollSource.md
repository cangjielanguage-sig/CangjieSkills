## enum ScrollSource

```cangjie
public enum ScrollSource <: Equatable<ScrollSource> {
    | Drag
    | Fling
    | EdgeEffect
    | OtherUserInput
    | ScrollBar
    | ScrollBarFling
    | Scroller
    | ScrollerAnimation
    | ...
}
```

**功能：** 滑动操作的来源。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ScrollSource](#enum-scrollsource)>

### Drag

```cangjie
Drag
```

**功能：** 拖拽事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Fling

```cangjie
Fling
```

**功能：** 拖拽结束之后的惯性滑动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### EdgeEffect

```cangjie
EdgeEffect
```

**功能：** EdgeEffect.Spring的边缘滚动效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### OtherUserInput

```cangjie
OtherUserInput
```

**功能：** 除拖拽外的其他用户输入，如鼠标滚轮、键盘事件等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### ScrollBar

```cangjie
ScrollBar
```

**功能：** 滚动条的拖拽事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### ScrollBarFling

```cangjie
ScrollBarFling
```

**功能：** 滚动条拖拽结束后的带速度的惯性滑动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Scroller

```cangjie
Scroller
```

**功能：** Scroller的不带动效方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### ScrollerAnimation

```cangjie
ScrollerAnimation
```

**功能：** Scroller的带动效方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(ScrollSource)

```cangjie
public operator func ==(other: ScrollSource): Bool
```

**功能：** 判断两个ScrollSource枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ScrollSource](#enum-scrollsource)|是|-|要比较的另一个ScrollSource枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(ScrollSource)

```cangjie
public operator func !=(other: ScrollSource): Bool
```

**功能：** 判断两个ScrollSource枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ScrollSource](#enum-scrollsource)|是|-|要比较的另一个ScrollSource枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|
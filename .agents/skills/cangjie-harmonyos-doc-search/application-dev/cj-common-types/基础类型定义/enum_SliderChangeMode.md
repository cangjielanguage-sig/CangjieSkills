## enum SliderChangeMode

```cangjie
public enum SliderChangeMode <: Equatable<SliderChangeMode> {
    | Begin
    | Moving
    | End
    | Click
    | ...
}
```

**功能：** Slider拖动或点击时触发事件的状态值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[SliderChangeMode](#enum-sliderchangemode)>

### Begin

```cangjie
Begin
```

**功能：** 鼠标接触或者按下滑块。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Moving

```cangjie
Moving
```

**功能：** 正在拖动滑块过程中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### End

```cangjie
End
```

**功能：** 手势/鼠标离开滑块。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Click

```cangjie
Click
```

**功能：** 点击滑动条使滑块位置移动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(SliderChangeMode)

```cangjie
public operator func ==(other: SliderChangeMode): Bool
```

**功能：** 判断两个SliderChangeMode枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SliderChangeMode](#enum-sliderchangemode)|是|-|要比较的另一个SliderChangeMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(SliderChangeMode)

```cangjie
public operator func !=(other: SliderChangeMode): Bool
```

**功能：** 判断两个SliderChangeMode枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SliderChangeMode](#enum-sliderchangemode)|是|-|要比较的另一个SliderChangeMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|
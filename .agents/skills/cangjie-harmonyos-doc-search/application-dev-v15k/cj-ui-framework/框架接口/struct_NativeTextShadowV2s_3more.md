## struct NativeTextShadowV2<sup>(deprecated)</sup>

```cangjie
public struct NativeTextShadowV2 {
    public NativeTextShadowV2(
        let radius: Float64,
        let offsetX: Float64,
        let offsetY: Float64,
        let color: UInt32,
        let fill: Bool,
        let shadowType: UInt32
    )
}
```

**功能：** 设置文字阴影效果，框架内使用结构体。

> **注意：**
>
> 即将弃用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### NativeTextShadowV2(Float64, Float64, Float64, UInt32, Bool, UInt32)

```cangjie
public NativeTextShadowV2(
    let radius: Float64,
    let offsetX: Float64,
    let offsetY: Float64,
    let color: UInt32,
    let fill: Bool,
    let shadowType: UInt32
)
```

**功能：** 创建NativeTextShadowV2类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|radius|Float64|是|-|阴影模糊半径。<br/>取值范围：[0, +∞)<br/>单位：px<br/>说明：<br/>设置小于0的值时，按值为0处理。<br/>如需使用vp单位的数值可用vp2px进行转换。|
|offsetX|Float64|是|-|阴影的X轴偏移量。<br/>单位：px|
|offsetY|Float64|是|-|阴影的Y轴偏移量。<br/>单位：px|
|color|UInt32|是|-|阴影的颜色。|
|fill|Bool|是|-|阴影是否内部填充。|
|shadowType|UInt32|是|-|阴影类型。|

## struct NativeTextTimerShadow<sup>(deprecated)</sup>

```cangjie
public struct NativeTextTimerShadow {
    public NativeTextTimerShadow(
        let radius: Float64,
        let offsetX: Float64,
        let offsetY: Float64,
        let color: UInt32,
        let fill: Bool,
        let shadowType: UInt32
    )
}
```

**功能：** 设置文字阴影效果，框架内使用结构体。

> **注意：**
>
> 即将弃用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### NativeTextTimerShadow(Float64, Float64, Float64, UInt32, Bool, UInt32)

```cangjie
public NativeTextTimerShadow(
    let radius: Float64,
    let offsetX: Float64,
    let offsetY: Float64,
    let color: UInt32,
    let fill: Bool,
    let shadowType: UInt32
)
```

**功能：** 创建NativeTextTimerShadow类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|radius|Float64|是|-|阴影模糊半径。<br>取值范围：[0, +∞)<br>单位：px。<br>设置小于0的值时，按值为0处理。<br>如需使用vp单位的数值可用vp2px进行转换。|
|offsetX|Float64|是|-|阴影的X轴偏移量。<br>单位：px。|
|offsetY|Float64|是|-|阴影的Y轴偏移量。<br>单位：px。|
|color|UInt32|是|-|阴影的颜色。|
|fill|Bool|是|-|阴影类型。|
|shadowType|UInt32|是|-|阴影是否内部填充。|

## class SizeOptions

```cangjie
public class SizeOptions {
    public SizeOptions(
        public var width!: Length = 0.vp,
        public var height!: Length = 0.vp
    )
}
```

**功能：** 设置宽高尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var width

```cangjie
public var width: Length = 0.vp
```

**功能：** 宽度。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写。

**起始版本：** 12

### var height

```cangjie
public var height: Length = 0.vp
```

**功能：** 高度。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写。

**起始版本：** 12

### SizeOptions(Length, Length)

```cangjie
public SizeOptions(public var width!: Length = 0.vp, public var height!: Length = 0.vp)
```

**功能：** 创建SizeOptions类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:----|:----|:----|:----|:----|
|width|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 宽度。|
|height|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 高度。|
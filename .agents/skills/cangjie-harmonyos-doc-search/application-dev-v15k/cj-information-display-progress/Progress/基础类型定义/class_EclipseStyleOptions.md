### class EclipseStyleOptions

```cangjie
public class EclipseStyleOptions {
    public var enableSmoothEffect: Bool
    public init(enableSmoothEffect!: Bool = true)
}
```

**功能：** Eclipse的样式参数类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var enableSmoothEffect

```cangjie
public var enableSmoothEffect: Bool
```

**功能：** 进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Bool)

```cangjie
public init(enableSmoothEffect!: Bool = true)
```

**功能：** 构造一个EclipseStyleOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enableSmoothEffect|Bool|否|true| **命名参数。** 进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值。|
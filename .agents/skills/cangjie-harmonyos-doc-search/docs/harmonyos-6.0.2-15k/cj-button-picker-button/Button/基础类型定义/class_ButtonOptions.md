### class ButtonOptions

```cangjie
public class ButtonOptions {
    public var shape: ButtonType
    public var stateEffect: Bool
    public var buttonStyle: ButtonStyleMode
    public var controlSize: ControlSize
    public var role: ButtonRole
    public init(
        shape!: ButtonType = ButtonType.Capsule,
        stateEffect!: Bool = true,
        buttonStyle!: ButtonStyleMode = ButtonStyleMode.EMPHASIZED,
        controlSize!: ControlSize = ControlSize.NORMAL,
        role!: ButtonRole = ButtonRole.NORMAL
    )
}
```

**功能：** 配置按钮的显示样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var buttonStyle

```cangjie
public var buttonStyle: ButtonStyleMode
```

**功能：** 描述按钮的样式和重要程度。

**类型：** [ButtonStyleMode](#enum-buttonstylemode)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var controlSize

```cangjie
public var controlSize: ControlSize
```

**功能：** 描述按钮的尺寸。

**类型：** [ControlSize](./cj-common-types.md#enum-controlsize)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var role

```cangjie
public var role: ButtonRole
```

**功能：** 描述按钮的角色。

**类型：** [ButtonRole](#enum-buttonrole)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var shape

```cangjie
public var shape: ButtonType
```

**功能：** 描述按钮的形状。

**类型：** [ButtonType](#enum-buttontype)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var stateEffect

```cangjie
public var stateEffect: Bool
```

**功能：** 按钮按下时是否开启按压态显示效果。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(ButtonType, Bool, ButtonStyleMode, ControlSize, ButtonRole)

```cangjie
public init(
    shape!: ButtonType = ButtonType.Capsule,
    stateEffect!: Bool = true,
    buttonStyle!: ButtonStyleMode = ButtonStyleMode.EMPHASIZED,
    controlSize!: ControlSize = ControlSize.NORMAL,
    role!: ButtonRole = ButtonRole.NORMAL
)
```

**功能：** 创建ButtonOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|shape|[ButtonType](#enum-buttontype)|否|ButtonType.Capsule| **命名参数。** 按钮的形状。|
|stateEffect|Bool|否|true| **命名参数。**  按钮按下时是否开启按压态显示效果，当设置为false时，按压效果关闭。<br>**说明：**<br>当开启按压态显示效果，开发者设置状态样式时，会基于状态样式设置完成后的背景色再进行颜色叠加。|
|buttonStyle|[ButtonStyleMode](#enum-buttonstylemode)|否|ButtonStyleMode.EMPHASIZED| **命名参数。** 描述按钮的样式和重要程度。<br/>**说明：**<br/>按钮重要程度：强调按钮>普通按钮>文字按钮。|
|controlSize|[ControlSize](./cj-common-types.md#enum-controlsize)|否|ControlSize.NORMAL| **命名参数。**  描述按钮的尺寸。|
|role|[ButtonRole](#enum-buttonrole)|否|ButtonRole.NORMAL| **命名参数。** 描述按钮的角色。|
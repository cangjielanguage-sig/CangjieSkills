### class ButtonOptions

```cangjie
public class ButtonOptions {
    public var shape: ?ButtonType
    public var stateEffect: ?Bool
    public var buttonStyle: ?ButtonStyleMode
    public var controlSize: ?ControlSize
    public var role: ?ButtonRole
    public init(
        shape!: ?ButtonType = None,
        stateEffect!: ?Bool = None,
        buttonStyle!: ?ButtonStyleMode = None,
        controlSize!: ?ControlSize = None,
        role!: ?ButtonRole = None
    )
}
```

**功能：** 配置按钮的显示样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var buttonStyle

```cangjie
public var buttonStyle: ?ButtonStyleMode
```

**功能：** 描述按钮的样式和重要程度。

**类型：** ?[ButtonStyleMode](#enum-buttonstylemode)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var controlSize

```cangjie
public var controlSize: ?ControlSize
```

**功能：** 描述按钮的尺寸。

**类型：** ?[ControlSize](./cj-common-types.md#enum-controlsize)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var role

```cangjie
public var role: ?ButtonRole
```

**功能：** 描述按钮的角色。

**类型：** ?[ButtonRole](#enum-buttonrole)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var shape

```cangjie
public var shape: ?ButtonType
```

**功能：** 描述按钮的形状。

**类型：** ?[ButtonType](#enum-buttontype)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var stateEffect

```cangjie
public var stateEffect: ?Bool
```

**功能：** 按钮按下时是否开启按压态显示效果。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?ButtonType, ?Bool, ?ButtonStyleMode, ?ControlSize, ?ButtonRole)

```cangjie
public init(
    shape!: ?ButtonType = None,
    stateEffect!: ?Bool = None,
    buttonStyle!: ?ButtonStyleMode = None,
    controlSize!: ?ControlSize = None,
    role!: ?ButtonRole = None
)
```

**功能：** 创建ButtonOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|shape|?[ButtonType](#enum-buttontype)|否|None|**命名参数。** 按钮的形状。初始值：ButtonType.Capsule|
|stateEffect|?Bool|否|None|**命名参数。** 按钮按下时是否开启按压态显示效果，当设置为false时，按压效果关闭。初始值：true|
|buttonStyle|?[ButtonStyleMode](#enum-buttonstylemode)|否|None|**命名参数。** 描述按钮的样式和重要程度。初始值：ButtonStyleMode.Emphasized|
|controlSize|?[ControlSize](./cj-common-types.md#enum-controlsize)|否|None|**命名参数。** 描述按钮的尺寸。初始值：ControlSize.Normal|
|role|?[ButtonRole](#enum-buttonrole)|否|None|**命名参数。** 描述按钮的角色。初始值：ButtonRole.Normal|
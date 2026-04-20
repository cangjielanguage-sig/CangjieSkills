### class BadgeStyle

```cangjie
public class BadgeStyle {
    public var color: ?ResourceColor
    public var fontSize: ?Length
    public var badgeSize: ?Length
    public var badgeColor: ?ResourceColor
    public var borderColor: ?ResourceColor
    public var borderWidth: ?Length
    public var fontWeight: ?FontWeight
    public init(color!: ?ResourceColor = None, fontSize!: ?Length = None, badgeSize!: ?Length = None,
        badgeColor!: ?ResourceColor = None, borderColor!: ?ResourceColor = None,
        borderWidth!: ?Length = None, fontWeight!: ?FontWeight = None)
}
```

**功能：** 包含Badge组件的样式参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var color

```cangjie
public var color: ?ResourceColor
```

**功能：** 文本颜色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var fontSize

```cangjie
public var fontSize: ?Length
```

**功能：** 文本大小，单位为fp。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var badgeColor

```cangjie
public var badgeColor: ?ResourceColor
```

**功能：** badge的颜色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var badgeSize

```cangjie
public var badgeSize: ?Length
```

**功能：** badge的大小，单位为vp。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var borderColor

```cangjie
public var borderColor: ?ResourceColor
```

**功能：** 底板描边颜色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var borderWidth

```cangjie
public var borderWidth: ?Length
```

**功能：** 底板描边粗细。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var fontWeight

```cangjie
public var fontWeight: ?FontWeight
```

**功能：** 设置文本的字体粗细。

**类型：** ?[FontWeight](./cj-common-types.md#enum-fontweight)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22
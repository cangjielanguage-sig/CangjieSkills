### class ListDividerOptions

```cangjie
public class ListDividerOptions {
    public var strokeWidth: ?Length
    public var color: ?ResourceColor
    public var startMargin: ?Length
    public var endMargin: ?Length
    public init(
        strokeWidth!: ?Length,
        color!: ?ResourceColor = None,
        startMargin!: ?Length = None,
        endMargin!: ?Length = None
    )
}
```

**功能：** ListItem分割线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var color

```cangjie
public var color: ?ResourceColor
```

**功能：** 设置分割线的颜色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var endMargin

```cangjie
public var endMargin: ?Length
```

**功能：** 设置分割线距离列表侧边结束端的距离。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var startMargin

```cangjie
public var startMargin: ?Length
```

**功能：** 设置分割线距离列表侧边起始端的距离。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var strokeWidth

```cangjie
public var strokeWidth: ?Length
```

**功能：** 设置分割线的线宽。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Length, ?ResourceColor, ?Length, ?Length)

```cangjie
public init(
    strokeWidth!: ?Length,
    color!: ?ResourceColor = None,
    startMargin!: ?Length = None,
    endMargin!: ?Length = None
)
```

**功能：** 构造ListItem分割线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

| 参数名         | 类型            | 必填  | 默认值 | 说明               |
|:----------- |:------------- |:--- |:--- |:---------------- |
| strokeWidth | ?[Length](./cj-common-types.md#interface-length)       | 是   | -   | 分割线的线宽。          |
| color       | ?[ResourceColor](./cj-common-types.md#interface-resourcecolor) | 否   | None | 分割线的颜色。          |
| startMargin | ?[Length](./cj-common-types.md#interface-length)       | 否   | None | 分割线距离列表侧边起始端的距离。 |
| endMargin   | ?[Length](./cj-common-types.md#interface-length)       | 否   | None | 分割线距离列表侧边结束端的距离。 |
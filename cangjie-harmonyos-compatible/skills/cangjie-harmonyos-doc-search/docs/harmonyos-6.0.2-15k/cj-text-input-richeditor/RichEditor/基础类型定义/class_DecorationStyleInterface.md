### class DecorationStyleInterface

```cangjie
public class DecorationStyleInterface {
    public var `type`: TextDecorationType = TextDecorationType.None
    public var color: ResourceColor = Color.BLACK
    public var style: TextDecorationStyle = TextDecorationStyle.SOLID
    public init(`type`!: TextDecorationType, color!: ?ResourceColor = None, style!: ?TextDecorationStyle = None)
}
```

**功能：** 实体装饰线样式配置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### var `type`

```cangjie
public var `type`: TextDecorationType = TextDecorationType.None
```

**功能：** 装饰线类型。

**类型：** [TextDecorationStyle](./cj-common-types.md#enum-textdecorationtype)

**读写能力：** 可读写

**起始版本：** 20

#### var color

```cangjie
public var color: ResourceColor = Color.BLACK
```

**功能：** 装饰线颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**起始版本：** 20

#### var style

```cangjie
public var style: TextDecorationStyle = TextDecorationStyle.SOLID
```

**功能：** 装饰线样式。

**类型：** [TextDecorationStyle](./cj-common-types.md#enum-textdecorationstyle)

**读写能力：** 可读写

**起始版本：** 20

#### init(TextDecorationType, ?ResourceColor, ?TextDecorationStyle)

```cangjie
public init(`type`!: TextDecorationType, color!: ?ResourceColor = None, style!: ?TextDecorationStyle = None)
```

**功能：** 创建DecorationStyleInterface类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|`type`|[TextDecorationStyle](./cj-common-types.md#enum-textdecorationtype)|是|-|**命名参数。** 装饰线类型。|
|color|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None|**命名参数。** 装饰线颜色。|
|style|?[TextDecorationStyle](./cj-common-types.md#enum-textdecorationstyle)|否|None|**命名参数。** 装饰线样式。|
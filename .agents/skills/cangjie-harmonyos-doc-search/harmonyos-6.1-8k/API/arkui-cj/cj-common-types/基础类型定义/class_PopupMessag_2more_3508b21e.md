## class PopupMessageOptions

```cangjie
public class PopupMessageOptions {
    public var textColor: ?ResourceColor
    public var font: ?Font
    public init(textColor!: ?ResourceColor = None, font!: ?Font = None)
}
```

**功能：** 弹窗信息文本参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var textColor

```cangjie
public var textColor: ?ResourceColor
```

**功能：** 设置弹窗信息文本颜色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var font

```cangjie
public var font: ?Font
```

**功能：** 设置弹窗信息字体属性。不支持设置family。

**类型：** ?[Font](#class-font)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?ResourceColor, ?Font)

```cangjie
public init(textColor!: ?ResourceColor = None, font!: ?Font = None)
```

**功能：** 构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|textColor|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None|**命名参数。** 弹窗信息文本颜色。初始值为Color(0x000000)。|
|font|?[Font](#class-font)|否|None|**命名参数。** 弹窗信息字体属性。初始值为Font()。|

## class OverlayOffset

```cangjie
public class OverlayOffset {
    public var x: ?Float64
    public var y: ?Float64
    public init(x!: ?Float64 = None, y!: ?Float64 = None)
}
```

**功能：** 设置浮层的偏移量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var x

```cangjie
public var x: ?Float64
```

**功能：** 横向偏移量。

**类型：** ?Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var y

```cangjie
public var y: ?Float64
```

**功能：** 纵向偏移量。

**类型：** ?Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?Float64, ?Float64)

```cangjie
public init(x!: ?Float64 = None, y!: ?Float64 = None)
```

**功能：** 构造浮层偏移量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|?Float64|否|None|**命名参数。** 横向偏移量。初始值为0.0。|
|y|?Float64|否|None|**命名参数。** 纵向偏移量。初始值为0.0。|
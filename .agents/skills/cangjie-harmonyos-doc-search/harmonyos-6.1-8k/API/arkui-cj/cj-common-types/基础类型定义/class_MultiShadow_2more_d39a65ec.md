## class MultiShadowOptions

```cangjie
public open class MultiShadowOptions {
    public var radius: ?Length
    public var offsetX: ?Length
    public var offsetY: ?Length
    protected init(radius: ?Length, offsetX: ?Length, offsetY: ?Length)
}
```

**功能：** 多阴影选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var radius

```cangjie
public var radius: ?Length
```

**功能：** 阴影模糊半径。
单位：vp。
<p>**NOTE**:
<br>小于或等于0的值将作为默认值处理。
</p>

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var offsetX

```cangjie
public var offsetX: ?Length
```

**功能：** 设置阴影的水平偏移量。
单位：vp。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var offsetY

```cangjie
public var offsetY: ?Length
```

**功能：** 设置阴影的垂直偏移量。
单位：vp。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?Length, ?Length, ?Length)

```cangjie
protected init(radius: ?Length, offsetX: ?Length, offsetY: ?Length)
```

**功能：** 构造一个MultiShadowOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| radius | ?[Length](./cj-common-types.md#interface-length) | 是 | - | 半径 |
| offsetX | ?[Length](./cj-common-types.md#interface-length) | 是 | - | X轴偏移 |
| offsetY | ?[Length](./cj-common-types.md#interface-length) | 是 | - | Y轴偏移 |

## class PickerTextStyle

```cangjie
public class PickerTextStyle {
    public var color: ?ResourceColor
    public var font: ?Font
    public init(color!: ?ResourceColor = None, font!: ?Font = None)
}
```

**功能：** 选择器文本样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var color

```cangjie
public var color: ?ResourceColor
```

**功能：** 设置选择器文本颜色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var font

```cangjie
public var font: ?Font
```

**功能：** 设置选择器文本字体。

**类型：** ?[Font](#class-font)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?ResourceColor, ?Font)

```cangjie
public init(color!: ?ResourceColor = None, font!: ?Font = None)
```

**功能：** 构造一个PickerTextStyle对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None|**命名参数。** 设置选择器文本颜色。|
|font|?[Font](#class-font)|否|None|**命名参数。** 设置选择器文本字体。|
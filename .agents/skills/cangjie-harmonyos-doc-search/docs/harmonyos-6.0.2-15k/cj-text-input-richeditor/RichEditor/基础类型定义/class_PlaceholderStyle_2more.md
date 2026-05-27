### class PlaceholderStyle

```cangjie
public class PlaceholderStyle {
    public var font: ?Fonts
    public var fontColor: ?ResourceColor
    public init(font!: ?Fonts = None, fontColor!: ?ResourceColor = None)
}
```

**功能：** 设置提示文本的字体样式.

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### var font

```cangjie
public var font: ?Fonts
```

**功能：** 设置placeholder文本样式。

**类型：** ?[Fonts](./cj-common-types.md#class-fonts)

**读写能力：** 可读写

**起始版本：** 20

#### var fontColor

```cangjie
public var fontColor: ?ResourceColor
```

**功能：** 设置placeholder文本颜色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**起始版本：** 20

#### init(?Fonts, ?ResourceColor)

```cangjie
public init(font!: ?Fonts = None, fontColor!: ?ResourceColor = None)
```

**功能：** 创建PlaceholderStyle类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|font|?[Fonts](./cj-common-types.md#class-fonts)|否|None| **命名参数。** 设置placeholder文本样式。|
|fontColor|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None| **命名参数。** 设置placeholder文本颜色。|

### class RichEditorRange

```cangjie
public open class RichEditorRange {
    public var start: Int32
    public var end: Int32
    public init(start: Int32, end: Int32)
}
```

**功能：** 定义RichEditor的范围。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### var end

```cangjie
public var end: Int32
```

**功能：** 需要更新样式的文本结束位置，省略或者超出文本范围时表示无穷大。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 20

#### var start

```cangjie
public var start: Int32
```

**功能：** 需要更新样式的文本起始位置，省略或者设置负值时表示从0开始。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 20

#### init(Int32, Int32)

```cangjie
public init(start: Int32, end: Int32)
```

**功能：** 创建RichEditorRange类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|Int32|是|-|需要更新样式的文本起始位置，省略或者设置负值时表示从0开始。|
|end|Int32|是|-|需要更新样式的文本结束位置，省略或者超出文本范围时表示无穷大。|
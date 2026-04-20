### class TextDecorationOptions

```cangjie
public class TextDecorationOptions {
    public var decorationType: ?TextDecorationType
    public var color: ?ResourceColor
    public init(decorationType!: ?TextDecorationType, color!: ?ResourceColor = None)
}
```

**功能：** 定义文本装饰选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var decorationType

```cangjie
public var decorationType: ?TextDecorationType
```

**功能：** 装饰类型。

**类型：** ?[TextDecorationType](./cj-common-types.md#enum-textdecorationstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var color

```cangjie
public var color: ?ResourceColor
```

**功能：** 颜色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?TextDecorationType, ?ResourceColor)

```cangjie
public init(decorationType!: ?TextDecorationType, color!: ?ResourceColor = None)
```

**功能：** TextDecorationOptions构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|decorationType|?[TextDecorationType](./cj-common-types.md#enum-textdecorationstyle)|是|-|**命名参数。** 装饰类型。初始值：TextDecorationType.None。|
|color|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|None|**命名参数。** 颜色。初始值：Color.Black。|

### class LeadingMarginPlaceholder

```cangjie
public class LeadingMarginPlaceholder {
    public var pixelMap: PixelMap
    public var size: ?(Length, Length)
    public init(pixelMap!: PixelMap, size!: ?(Length, Length))
}
```

**功能：** 定义段落的首行缩进占位符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var pixelMap

```cangjie
public var pixelMap: PixelMap
```

**功能：** 占位符像素图。

**类型：** [PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var size

```cangjie
public var size: ?(Length, Length)
```

**功能：** 占位符大小。

**类型：** ?([Length](./cj-common-types.md#interface-length), [Length](./cj-common-types.md#interface-length))

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(PixelMap, ?(Length, Length))

```cangjie
public init(pixelMap!: PixelMap, size!: ?(Length, Length))
```

**功能：** LeadingMarginPlaceholder构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pixelMap|[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|是|-|**命名参数。** 占位符像素图。|
|size|?([Length](./cj-common-types.md#interface-length), [Length](./cj-common-types.md#interface-length))|是|-|**命名参数。** 占位符大小。初始值：(0.0.px, 0.0.px)。|
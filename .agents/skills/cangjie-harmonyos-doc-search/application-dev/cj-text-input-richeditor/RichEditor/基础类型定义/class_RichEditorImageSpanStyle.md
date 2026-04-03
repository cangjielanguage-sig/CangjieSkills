### class RichEditorImageSpanStyle

```cangjie
public class RichEditorImageSpanStyle {
    public var size: Option<(Length, Length)>
    public var verticalAlign: ?ImageSpanAlignment
    public var objectFit: ?ImageFit
    public init(
        size!: Option<(Length, Length)> = Option.None,
        verticalAlign!: ?ImageSpanAlignment = Option.None,
        objectFit!: ?ImageFit = Option.None
    )
}
```

**功能：** 定义span图像样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var size

```cangjie
public var size: Option<(Length, Length)>
```

**功能：** 图像大小。

**类型：** Option\<([Length](./cj-common-types.md#interface-length), [Length](./cj-common-types.md#interface-length))>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var verticalAlign

```cangjie
public var verticalAlign: ?ImageSpanAlignment
```

**功能：** 图像垂直对齐。

**类型：** ?[ImageSpanAlignment](./cj-common-types.md#enum-imagespanalignment)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var objectFit

```cangjie
public var objectFit: ?ImageFit
```

**功能：** 图像适应方式。

**类型：** ?[ImageFit](./cj-common-types.md#enum-imagefit)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(Option\<(Length, Length)>, ?ImageSpanAlignment, ?ImageFit)

```cangjie
public init(
    size!: Option<(Length, Length)> = Option.None,
    verticalAlign!: ?ImageSpanAlignment = Option.None,
    objectFit!: ?ImageFit = Option.None
)
```

**功能：** RichEditorImageSpanStyle构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|Option\<([Length](./cj-common-types.md#interface-length), [Length](./cj-common-types.md#interface-length))>|否|Option.None|**命名参数。** 图像大小。|
|verticalAlign|?[ImageSpanAlignment](./cj-common-types.md#enum-imagespanalignment)|否|Option.None|**命名参数。** 图像垂直对齐。初始值：ImageSpanAlignment.Bottom。|
|objectFit|?[ImageFit](./cj-common-types.md#enum-imagefit)|否|Option.None|**命名参数。** 图像适应方式。初始值：ImageFit.Cover。|
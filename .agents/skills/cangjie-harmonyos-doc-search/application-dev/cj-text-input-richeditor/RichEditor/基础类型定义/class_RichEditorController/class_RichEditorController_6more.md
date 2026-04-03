### class RichEditorController

```cangjie
public class RichEditorController <: RichEditorBaseController {
    public init()
}
```

**功能：** 提供RichEditor的控制器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [RichEditorBaseController](#class-richeditorbasecontroller)

#### init()

```cangjie
public init()
```

**功能：** 创建RichEditorController类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### func addTextSpan(?ResourceStr, ?RichEditorTextSpanOptions)

```cangjie
public func addTextSpan(content!: ?ResourceStr, options!: ?RichEditorTextSpanOptions = None): Int32
```

**功能：** 添加文本内容，如果组件光标闪烁，插入后光标位置更新为新插入文本的后面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-|**命名参数。** 文本内容。初始值：""。|
|options|?[RichEditorTextSpanOptions](#class-richeditortextspanoptions)|否|None|**命名参数。** 文本选项。初始值：RichEditorTextSpanOptions()。|

**返回值：**

|类型|说明|
|:---|:---|
|Int32|添加完成的TextSpan所在的位置。|

#### func addImageSpan(?ResourceStr, ?RichEditorImageSpanOptions)

```cangjie
public func addImageSpan(value!: ?ResourceStr, options!: ?RichEditorImageSpanOptions = None): Int32
```

**功能：** 添加图片内容，如果组件光标闪烁，插入后光标位置更新为新插入图片的后面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-|**命名参数。** 图片内容。初始值：""。|
|options|?[RichEditorImageSpanOptions](#class-richeditorimagespanoptions)|否|None|**命名参数。** 图片选项。初始值：RichEditorImageSpanOptions()。|

**返回值：**

|类型|说明|
|:---|:---|
|Int32|添加完成的ImageSpan所在的位置。|

#### func updateSpanStyle(?Int32, ?Int32, ?RichEditorTextStyle)

```cangjie
public func updateSpanStyle(start!: ?Int32 = None, end!: ?Int32 = None, textStyle!: ?RichEditorTextStyle): Unit
```

**功能：** 修改span样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|?Int32|否|None|**命名参数。** 起始位置。初始值：0。|
|end|?Int32|否|None|**命名参数。** 结束位置。初始值：Int32.Max。|
|textStyle|?[RichEditorTextStyle](#class-richeditortextstyle)|是|-|**命名参数。** 文本样式。初始值：RichEditorTextStyle()。|

#### func updateSpanStyle(?Int32, ?Int32, ?RichEditorImageSpanStyle)

```cangjie
public func updateSpanStyle(start!: ?Int32 = None, end!: ?Int32 = None, imageStyle!: ?RichEditorImageSpanStyle): Unit
```

**功能：** 修改span样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|?Int32|否|None|**命名参数。** 起始位置。初始值：0。|
|end|?Int32|否|None|**命名参数。** 结束位置。初始值：Int32.Max。|
|imageStyle|?[RichEditorImageSpanStyle](#class-richeditorimagespanstyle)|是|-|**命名参数。** 图像样式。初始值：RichEditorImageSpanStyle()。|
#### func getSpans(Int32, Int32)

```cangjie
public func getSpans(start!: Int32 = -1, end!: Int32 = -1): ArrayList<RichEditorSpanResult>
```

**功能：** 获取Span信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| start | Int32 | 否 | -1 | **命名参数。**  起始位置，省略或者设置负值时表示从0开始。 |
| end | Int32 | 否 | -1 | **命名参数。**  结束位置，省略或者超出文本范围时表示无穷大。 |

**返回值：**

| 参数名 | 说明 |
| :--- | :--- |
| ArrayList\<[RichEditorSpanResult](#class-richeditorspanresult)> | 存储span信息类型的数组。|

> **说明：**
>
> 连续多次调用 getSpans 获取信息可能存在运行异常，可以通过 try catch 捕获后处理。

#### func setCaretOffset(Int64)

```cangjie
public func setCaretOffset(offset: Int64): Bool
```

**功能：** 设置光标位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| offset | Int64 | 是 | - | 光标偏移位置。超出文本范围时，设置失败。 |

**返回值：**

| 类型 | 说明 |
| :--- | :--- |
| Bool | 光标是否设置成功。 |

#### func updateSpanStyle(Int32, Int32, RichEditorTextStyle)

```cangjie
public func updateSpanStyle(start!: Int32 = 0, end!: Int32 = Int32.Max, textStyle!: RichEditorTextStyle): Unit
```

**功能：** 更新文本、图片或SymbolSpan样式。

> **说明：**
>
> - 若只更新了一个Span的部分内容，则会根据更新部分、未更新部分将该Span拆分为多个Span。
> - 使用该接口更新文本、图片或SymbolSpan样式时默认不会关闭自定义文本选择菜单。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| start | Int32 | 否 | 0 | **命名参数。**  需要更新样式的文本起始位置，省略或者设置负值时表示从0开始。 |
| end | Int32 | 否 | Int32.Max | **命名参数。**  需要更新样式的文本结束位置，省略或者超出文本范围时表示无穷大。 |
| textStyle | [RichEditorTextStyle](#class-richeditortextstyle) | 是 | - | **命名参数。**  文本样式。 |

#### func updateSpanStyle(Int32, Int32, RichEditorImageSpanStyle)

```cangjie
public func updateSpanStyle(start!: Int32 = 0, end!: Int32 = Int32.Max, imageStyle!: RichEditorImageSpanStyle): Unit
```

**功能：** 更新文本、图片或SymbolSpan样式。

> **说明：**
>
> - 若只更新了一个Span的部分内容，则会根据更新部分、未更新部分将该Span拆分为多个Span。
> - 使用该接口更新文本、图片或SymbolSpan样式时默认不会关闭自定义文本选择菜单。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| start | Int32 | 否 | 0 | **命名参数。**  需要更新样式的文本起始位置，省略或者设置负值时表示从0开始。 |
| end | Int32 | 否 | Int32.Max | **命名参数。**  需要更新样式的文本结束位置，省略或者超出文本范围时表示无穷大。 |
| imageStyle | [RichEditorImageSpanStyle](#class-richeditorimagespanstyle) | 是 | - | **命名参数。**  图片样式。 |
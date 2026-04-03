#### func updateParagraphStyle(Int32, Int32, RichEditorParagraphStyle)

```cangjie
public func updateParagraphStyle(start!: Int32 = 0, end!: Int32 = -1, style!: RichEditorParagraphStyle): Unit
```

**功能：** 更新段落的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| start | Int32 | 否 | 0 | **命名参数。**  需要更新样式的段落起始位置，省略或者设置负值时表示从0开始。 |
| end | Int32 | 否 | -1 | **命名参数。**  需要更新样式的文本结束位置，省略或者超出文本范围时表示无穷大。 |
| style | [RichEditorParagraphStyle](#class-richeditorparagraphstyle) | 是 | - | **命名参数。**  段落样式。 |
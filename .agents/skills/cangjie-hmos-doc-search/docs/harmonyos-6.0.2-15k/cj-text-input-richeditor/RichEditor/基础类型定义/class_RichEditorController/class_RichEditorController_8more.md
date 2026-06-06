### class RichEditorController

```cangjie
public class RichEditorController {}
```

**功能：** RichEditor组件的控制器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init()

```cangjie
public init()
```

**功能：** 创建RichEditorController类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func addImageSpan(AppResource, RichEditorImageSpanOptions)

```cangjie
public func addImageSpan(value!: AppResource, options!: RichEditorImageSpanOptions = RichEditorImageSpanOptions()): Int32
```

**功能：** 添加图片内容，如果组件光标闪烁，插入后光标位置更新为新插入图片的后面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| value | [AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource ) | 是 | - | **命名参数。**  图片内容。 |
| options | [RichEditorImageSpanOptions](#class-richeditorimagespanoptions) | 否 | RichEditorImageSpanOptions() | **命名参数。**  图片选项。 |

**返回值：**

| 类型 | 说明 |
| :--- | :--- |
| Int32 | 添加完成的ImageSpan所在的位置。 |

#### func addImageSpan(String, RichEditorImageSpanOptions)

```cangjie
public func addImageSpan(value!: String, options!: RichEditorImageSpanOptions = RichEditorImageSpanOptions()): Int32
```

**功能：** 添加图片内容，如果组件光标闪烁，插入后光标位置更新为新插入图片的后面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| value | String | 是 | - | **命名参数。**  图片内容。 |
| options | [RichEditorImageSpanOptions](#class-richeditorimagespanoptions) | 否 | RichEditorImageSpanOptions() | **命名参数。**  图片选项。 |

**返回值：**

| 类型 | 说明 |
| :--- | :--- |
| Int32 | 添加完成的ImageSpan所在的位置。 |

#### func addTextSpan(String, RichEditorTextSpanOptions)

```cangjie
public func addTextSpan(value!: String, options!: RichEditorTextSpanOptions = RichEditorTextSpanOptions()): Int32
```

**功能：** 添加文本内容，如果组件光标闪烁，插入后光标位置更新为新插入文本的后面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| value | String | 是 | - | **命名参数。**  文本内容。 |
| options | [RichEditorTextSpanOptions](#class-richeditortextspanoptions) | 否 | RichEditorTextSpanOptions() | **命名参数。**  文本选项。 |

**返回值：**

| 类型 | 说明 |
| :--- | :--- |
| Int32 | 添加完成的TextSpan所在的位置。 |

#### func closeSelectionMenu()

```cangjie
public func closeSelectionMenu(): Unit
```

**功能：** 关闭自定义选择菜单或系统默认选择菜单。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func deleteSpans(Int32, Int32)

```cangjie
public func deleteSpans(start!: Int32 = 0, end!: Int32 = Int32.Max): Unit
```

**功能：** 删除指定范围内的文本和图片。

> **说明：**
>
> 当所有参数省略时，删除所有文本和图片。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| start | Int32 | 否 | 0 | **命名参数。**  起始位置，省略或者设置负值时表示从0开始。 |
| end | Int32 | 否 | Int32.Max | **命名参数。**  结束位置，省略或者超出文本范围时表示到结尾。 |

#### func getCaretOffset()

```cangjie
public func getCaretOffset(): Int64
```

**功能：** 获取当前光标所在位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

| 类型 | 说明 |
| :--- | :--- |
| Int64 | 当前光标所在位置。 |
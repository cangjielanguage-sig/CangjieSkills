#### func deleteSpans(?Int32, ?Int32)

```cangjie
public func deleteSpans(start!: ?Int32 = None, end!: ?Int32 = None): Unit
```

**功能：** 删除指定范围内的文本和图片。

> **说明：**
>
> 当所有参数省略时，删除所有文本和图片。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|?Int32|否|None|**命名参数。** 起始位置，省略或者设置负值时表示从0开始。初始值：0。|
|end|?Int32|否|None|**命名参数。** 结束位置，省略或者超出文本范围时表示到结尾。初始值：Int32.Max。|

#### func closeSelectionMenu()

```cangjie
public func closeSelectionMenu(): Unit
```

**功能：** 关闭自定义选择菜单或系统默认选择菜单。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### func updateParagraphStyle(?Int32, ?Int32, ?RichEditorParagraphStyle)

```cangjie
public func updateParagraphStyle(start!: ?Int32 = None, end!: ?Int32 = None, style!: ?RichEditorParagraphStyle): Unit
```

**功能：** 修改span样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|?Int32|否|None|**命名参数。** 起始位置。初始值：0。|
|end|?Int32|否|None|**命名参数。** 结束位置。初始值：-1。|
|style|?[RichEditorParagraphStyle](#class-richeditorparagraphstyle)|是|-|**命名参数。** 段落样式。初始值：RichEditorParagraphStyle()。|

#### func getSpans(?Int32, ?Int32)

```cangjie
public func getSpans(start!: ?Int32 = None, end!: ?Int32 = None): ArrayList<RichEditorSpanResult>
```

**功能：** 获取Span信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|?Int32|否|None|**命名参数。** 起始位置。初始值：-1。|
|end|?Int32|否|None|**命名参数。** 结束位置。初始值：-1。|

**返回值：**

|类型|说明|
|:---|:---|
|ArrayList\<[RichEditorSpanResult](#interface-richeditorspanresult)>|Span内容。|
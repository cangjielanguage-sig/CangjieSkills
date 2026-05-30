### class TextAreaController

```cangjie
public class TextAreaController {
    public init()
}
```

**功能：** TextArea组件的控制器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init()

```cangjie
public init()
```

**功能：** 创建TextAreaController类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func caretPosition(Int32)

```cangjie
public func caretPosition(value: Int32)
```

**功能：** 设置光标位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|光标的位置。|

#### func getCaretOffset()

```cangjie
public func getCaretOffset(): CJCaretOffset
```

**功能：** 返回当前光标所在位置信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[CJCaretOffset](./cj-text-input-search.md#struct-cjcaretoffset)|光标相对输入框的位置。|

#### func getTextContentLineCount()

```cangjie
public func getTextContentLineCount(): Int32
```

**功能：** 获取已编辑文本内容的行数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|已编辑文本内容行数。|

#### func getTextContentRect()

```cangjie
public func getTextContentRect(): CJRectResult
```

**功能：** 获取已编辑文本内容区域相对组件的位置和大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[CJRectResult](./cj-text-input-search.md#struct-cjrectresult)|获取已编辑文本内容区域相对组件的位置和大小。|

#### func setTextSelection(Int32, Int32, SelectionOptions)

```cangjie
public func setTextSelection(
    selectionStart: Int32,
    selectionEnd: Int32,
    options!: SelectionOptions = SelectionOptions()
): Unit
```

**功能：** 组件在获焦状态下，调用该接口设置文本选择区域并高亮显示，且只有在selectionStart小于selectionEnd时，文字才会被选取并高亮显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|selectionStart|Int32|是|-|文本选择区域起始位置，文本框中文字的起始位置为0。<br/>当selectionStart小于0时、按照0处理；当selectionStart大于文字最大长度时、按照文字最大长度处理。|
|selectionEnd|Int32|是|-|文本选择区域结束位置。<br/>当selectionEnd小于0时、按照0处理；当selectionEnd大于文字最大长度时、按照文字最大长度处理。|
|options|[SelectionOptions](#class-selectionoptions)|否|SelectionOptions()| **命名参数。** 选中文字时的配置。|

#### func stopEditing()

```cangjie
public func stopEditing(): Unit
```

**功能：** 退出编辑态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19
### class TextInputController

```cangjie
public class TextInputController {
    public init()
}
```

**功能：** TextInput组件的控制器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init()

```cangjie
public init()
```

**功能：** 创建TextInputController类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func caretPosition(Int32)

```cangjie
public func caretPosition(value: Int32): Unit
```

**功能：** 设置输入光标的位置。当取值小于0时，取0，大于文本长度时，显示在文本末尾。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|从字符串开始到光标所在位置的字符长度。|

#### func getCaretOffset()

```cangjie
public func getCaretOffset(): CJCaretOffset
```

**功能：** 返回当前光标所在位置。

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

> **说明：**
>
> - 初始不输入文本时，返回值中有相对组件的位置信息，高度和宽度都为0。
> - 返回值中的位置信息是第一个字符相对于可编辑组件的位置。
> - 在Search组件中，返回的位置信息是相对Search组件中搜索图标的偏移值。
> - 有输入时返回信息中的宽度是组件编辑的固定宽度。

#### func setTextSelection(Int32, Int32, MenuPolicy)

```cangjie
public func setTextSelection(selectionStart: Int32, selectionEnd: Int32, options!: MenuPolicy = MenuPolicy.Default): Unit
```

**功能：** 组件在获焦状态下，调用该接口设置文本选择区域并高亮显示，且只有在selectionStart小于selectionEnd时，文字才会被选取并高亮显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|selectionStart|Int32|是|-|文本选择区域起始位置，文本框中文字的起始位置为0。<br/>当selectionStart小于0时、按照0处理；当selectionStart大于文字最大长度时、按照文字最大长度处理。|
|selectionEnd|Int32|是|-|文本选择区域结束位置。<br/>当selectionEnd小于0时、按照0处理；当selectionEnd大于文字最大长度时、按照文字最大长度处理。|
|options|[MenuPolicy](./cj-common-types.md#enum-menupolicy)|否|MenuPolicy.Default| **命名参数。** 选中文字时的配置。|

#### func stopEditing()

```cangjie
public func stopEditing(): Unit
```

**功能：** 退出编辑态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 15
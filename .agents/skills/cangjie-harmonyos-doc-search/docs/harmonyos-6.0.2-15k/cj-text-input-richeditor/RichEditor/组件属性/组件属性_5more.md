## 组件属性

除支持通用属性外，还支持以下属性：

### func bindSelectionMenu(RichEditorSpanType, () -> Unit, ResponseType, SelectionMenuOptions)

```cangjie
public func bindSelectionMenu(
    spantype!: RichEditorSpanType = RichEditorSpanType.TEXT,
    content!: () -> Unit,
    responseType!: ResponseType = ResponseType.LongPress,
    options !: SelectionMenuOptions
): This
```

**功能：** 设置自定义选择菜单。

> **说明：**
>
> 自定义菜单超长时，建议内部嵌套[Scroll](cj-scroll-swipe-scroll.md)组件使用，避免键盘被遮挡。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|spantype|[RichEditorSpanType](#enum-richeditorspantype)|否|RichEditorSpanType.TEXT| **命名参数。** 指定选择菜单的类型。|
|content|()->Unit|是|-| **命名参数。** 指定选择菜单的内容。使用时结合[@Builder](../../../Dev_Guide/arkui-cj/paradigm/cj-macro-builder.md)和[bind](./cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。|
|responseType|[ResponseType](./cj-common-types.md#enum-responsetype)|否|ResponseType.LongPress| **命名参数。** 指定选择菜单的响应类型。|
|options|[SelectionMenuOptions](./cj-text-input-richeditor.md#class--selectionmenuoptions)|是|-| **命名参数。** 指定选择菜单的选项。|

### func copyOptions(CopyOptions)

```cangjie
public func copyOptions(copyOptions: CopyOptions): This
```

**功能：** 设置文本内容支持复制粘贴的能力。

> **说明：**
>
> - copyOptions不为CopyOptions.None时，长按组件内容，会弹出文本选择弹框。如果通过bindSelectionMenu等方式自定义文本选择菜单，则会弹出自定义的菜单。
> - 设置copyOptions为CopyOptions.None，复制、剪切功能不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|copyOptions|[CopyOptions](./cj-common-types.md#enum-copyoptions)|是|-|复制粘贴的能力。<br>初始值：CopyOptions.LocalDevice。|

### func customKeyboard(() -> Unit)

```cangjie
public func customKeyboard(builder!: () -> Unit): This
```

**功能：** 定义自定义键盘。

> **说明：**
>
> - 当设置自定义键盘时，输入框激活后不会打开系统输入法，而是加载指定的自定义组件。
> - 自定义键盘的高度可以通过自定义组件根节点的height属性设置，宽度不可设置，使用系统默认值。
> - 自定义键盘采用覆盖原始界面的方式呈现，不会对应用原始界面产生压缩或者上提。
> - 自定义键盘无法获取焦点，但是会拦截手势事件。
> - 默认在输入控件失去焦点时，关闭自定义键盘。
> - 如果设备支持拍摄输入，设置自定义键盘后，该输入框会不支持拍摄输入。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|()->Unit|是|-| **命名参数。** 富文本编辑器的自定义键盘。使用时结合[@Builder](../../../Dev_Guide/arkui-cj/paradigm/cj-macro-builder.md)和[bind](./cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。|

### func placeholder(AppResource, PlaceholderStyle)

```cangjie
public func placeholder(value: AppResource, style!: PlaceholderStyle = PlaceholderStyle()): This
```

**功能：** 设置无输入时的提示文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|无输入时的提示文本。|
|style|[PlaceholderStyle](#class-placeholderstyle)|否|-| **命名参数。** 提示文本的字体样式。|
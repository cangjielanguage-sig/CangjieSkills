### func customKeyboard(() -> Unit, Bool)

```cangjie
public func customKeyboard(value: () -> Unit, options!: Bool = false): This
```

**功能：** 设置自定义键盘。

> **说明：**
>
> - 当设置自定义键盘时，输入框激活后不会打开系统输入法，而是加载指定的自定义组件。
> - 自定义键盘的高度可以通过自定义组件根节点的height属性设置，宽度不可设置，使用系统默认值。
> - 自定义键盘采用覆盖原始界面的方式呈现，当没有开启避让模式或者输入框不需要避让的场景不会对应用原始界面产生压缩或者上提。
> - 自定义键盘无法获取焦点，但是会拦截手势事件。
> - 默认在输入控件失去焦点时，关闭自定义键盘，开发者也可以通过[stopEditing](#func-stopediting)方法控制键盘关闭。
> - 如果设备支持拍摄输入，设置自定义键盘后，该输入框会不支持拍摄输入。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|()->Unit|是|-|自定义键盘。使用时结合[@Builder](../../../Dev_Guide/arkui-cj/paradigm/cj-macro-builder.md)和[bind](./cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。|
|options|Bool|否|false| **命名参数。** 自定义键盘是否支持避让功能。|

### func decoration(TextDecorationType, ResourceColor, TextDecorationStyle)

```cangjie
public func decoration(decorationType!: TextDecorationType = TextDecorationType.None, color!: ResourceColor = Color.BLACK,decorationStyle!: TextDecorationStyle = TextDecorationStyle.SOLID): This
```

**功能：** 设置文本装饰线类型样式及其颜色。密码模式不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|decorationType|[TextDecorationType](./cj-common-types.md#enum-textdecorationtype)|否|TextDecorationType.None| **命名参数。** 文本装饰线样式。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color.BLACK| **命名参数。** 文本装饰线颜色。|
|decorationStyle|[TextDecorationStyle](./cj-common-types.md#enum-textdecorationstyle)|否|TextDecorationStyle.SOLID|文本装饰线样式。|

### func editMenuOptions((Array\<TextMenuItem>) -> Array\<TextMenuItem>, (TextMenuItem, Int32, Int32) -> Bool)

```cangjie
public func editMenuOptions(
    onCreateMenu: (Array<TextMenuItem>)->Array<TextMenuItem>,
    onMenuItemClick: (TextMenuItem, Int32, Int32)->Bool)
: This
```

**功能：** 设置自定义菜单扩展项，允许用户设置扩展项的文本内容、图标、回调方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onCreateMenu|(Array\<[TextMenuItem](./cj-text-input-text.md#class-textmenuitem)>)->Array\<[TextMenuItem](./cj-text-input-text.md#class-textmenuitem)>|是|-|菜单数据模版编辑能力。|
|onMenuItemClick|([TextMenuItem](./cj-text-input-text.md#class-textmenuitem), Int32, Int32)->Bool|是|-|菜单项功能函数。|

### func enableKeyboardOnFocus(Bool)

```cangjie
public func enableKeyboardOnFocus(value: Bool): This
```

**功能：** 设置Search通过点击以外的方式获焦时，是否主动拉起软键盘。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|Search获焦时，是否主动拉起软键盘。true表示主动拉起，false表示不主动拉起。<br>初始值:true。|
### func decoration(TextDecorationType, ResourceColor, TextDecorationStyle)

```cangjie
public func decoration(decorationType!: TextDecorationType = TextDecorationType.None, color!: ResourceColor = Color.BLACK,style!: TextDecorationStyle = TextDecorationStyle.SOLID): This
```

**功能：** 设置文本装饰线类型样式及其颜色。密码模式不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|decorationType|[TextDecorationType](./cj-common-types.md#enum-textdecorationtype)|否|TextDecorationType.None| **命名参数。** 文本装饰线样式。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color.BLACK| **命名参数。** 文本装饰线颜色。|
|style|[TextDecorationStyle](./cj-common-types.md#enum-textdecorationstyle)|否|TextDecorationStyle.SOLID|文本装饰线样式。|

### func editMenuOptions((Array\<TextMenuItem>) -> Array\<TextMenuItem>, (TextMenuItem,Int32,Int32) -> Bool)

```cangjie
public func editMenuOptions(
    onCreateMenu: (Array<TextMenuItem>)->Array<TextMenuItem>,
    onMenuItemClick: (TextMenuItem, Int32, Int32)->Bool): This
```

**功能：** 设置自定义菜单扩展项，允许用户设置扩展项的文本内容、图标、回调方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onCreateMenu|(Array\<[TextMenuItem](./cj-text-input-text.md#class-textmenuitem)>)->Array\<[TextMenuItem](./cj-text-input-text.md#class-textmenuitem)>|是|-|菜单数据模版编辑能力。|
|onMenuItemClick|([TextMenuItem](./cj-text-input-text.md#class-textmenuitem), Int32, Int32)->Bool|是|-|菜单项功能函数。|

### func enableAutoFill(Bool)

```cangjie
public func enableAutoFill(value: Bool): This
```

**功能：** 设置是否启用自动填充。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否启用自动填充。true表示启用，false表示不启用。<br>初始值：true。|

### func enableKeyboardOnFocus(Bool)

```cangjie
public func enableKeyboardOnFocus(value: Bool): This
```

**功能：** 设置TextInput通过点击以外的方式获焦时，是否主动拉起软键盘。获焦默认绑定输入法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|通过点击以外的方式获焦时，是否主动拉起软键盘。<br>初始值：true。|

### func enablePreviewText(Bool)

```cangjie
public func enablePreviewText(value: Bool): This
```

**功能：** 设置是否开启输入预上屏。

> **说明：**
>
> 预上屏内容定义为文字暂存态，目前不支持文字拦截功能，因此不触发[onWillInsert](#func-onwillinsertfloat64-string---bool)、[onDidInsert](#func-ondidinsertfloat64-string---unit)、[onWillDelete](#func-onwilldeletefloat64-int32-string---bool)、[onDidDelete](#func-ondiddeletefloat64-int32-string---unit)回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否开启输入预上屏。<br>初始值：true。|

### func enterKeyType(EnterKeyType)

```cangjie
public func enterKeyType(value: EnterKeyType): This
```

**功能：** 设置输入法回车键类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[EnterKeyType](#enum-enterkeytype)|是|-|输入法回车键类型。<br>初始值：EnterKeyType.Done。|
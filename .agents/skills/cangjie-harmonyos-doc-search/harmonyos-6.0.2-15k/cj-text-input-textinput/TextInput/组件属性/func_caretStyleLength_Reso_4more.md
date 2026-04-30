### func caretStyle(Length, ResourceColor)

```cangjie
public func caretStyle(width!: Length, color!: ResourceColor): This
```

**功能：** 设置光标风格。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 光标尺寸，不支持百分比。<br>初始值：2.vp。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-| **命名参数。** 光标颜色。<br>初始值：0xFF0A59F7。|

### func contentType(ContentType)

```cangjie
public func contentType(value: ContentType): This
```

**功能：** 设置自动填充类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ContentType](./cj-common-types.md#enum-contenttype)|是|-|自动填充类型。|

### func copyOption(CopyOptions)

```cangjie
public func copyOption(value: CopyOptions): This
```

**功能：** 设置输入的文本是否可复制。

> **说明：**
>
> - 设置CopyOptions.None时，当前TextInput中的文字无法被复制或剪切，仅支持粘贴。
> - 设置CopyOptions.None时，不允许拖拽。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[CopyOptions](./cj-common-types.md#enum-copyoptions)|是|-|输入的文本是否可复制。<br>初始值：CopyOptions.LocalDevice，支持设备内复制。|

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
> - 默认在输入控件失去焦点时，关闭自定义键盘，开发者也可以通过[TextInputController](#class-textinputcontroller).[stopEditing](#func-stopediting)方法控制键盘关闭。
> - 如果设备支持拍摄输入，设置自定义键盘后，该输入框会不支持拍摄输入。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|()->Unit|是|-|自定义键盘。使用时结合[@Builder](../../../Dev_Guide/arkui-cj/paradigm/cj-macro-builder.md)和[bind](./cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。|
|options|Bool|否|false| **命名参数。** 自定义键盘是否支持避让功能。|
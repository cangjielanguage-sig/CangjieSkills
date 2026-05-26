### func placeholder(String, PlaceholderStyle)

```cangjie
public func placeholder(value: String, style!: PlaceholderStyle = PlaceholderStyle()): This
```

**功能：** 设置无输入时的提示文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|无输入时的提示文本。|
|style|[PlaceholderStyle](#class-placeholderstyle)|否|-| **命名参数。** 提示文本的字体样式。|

### func enterKeyType(EnterKeyType)

```cangjie
public func enterKeyType(value: EnterKeyType): This
```

**功能：** 设置软键盘输入法回车键类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[EnterKeyType](./cj-text-input-textinput.md#enum-enterkeytype)|是|-| 软键盘输入法回车键类型。</br>初始为EnterKeyType.NEW_LINE。 |

### func caretColor(ResourceColor)

```cangjie
public func caretColor(color: ResourceColor): This
```

**功能：** 设置输入框光标、手柄颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|输入框光标、手柄颜色。</br>初始值：0x007DFF。|

### func enableKeyboardOnFocus(Bool)

```cangjie
public func enableKeyboardOnFocus(enable: Bool): This
```

**功能：** 设置RichEditor通过点击以外的方式获焦时，是否主动拉起软键盘。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enable|Bool|是|-|通过点击以外的方式获焦时，是否主动拉起软键盘。true表示主动拉起软键盘，false表示不主动拉起软键盘。</br>初始值：true。|

### func selectedBackgroundColor(ResourceColor)

```cangjie
public func selectedBackgroundColor(color: ResourceColor): This
```

**功能：** 设置文本选中的底板颜色。如果未设置不透明度，默认为20%不透明度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|文本选中的底板颜色。默认为20%不透明度。|

### func enableDataDetector(Bool)

```cangjie
public func enableDataDetector(enable: Bool): This
```

**功能：** 设置是否进行文本特殊实体识别。

该接口依赖设备底层应具有文本识别能力，否则设置不会生效。

当enableDataDetector设置为true且未指定dataDetectorConfig属性时，系统将默认识别所有类型的实体，并将这些实体的color和decoration更改为预设样式：

```cangjie
color: 0xff007dff,
decoration: DecorationStyleInterface(
  type: TextDecorationType.Underline,
  color: 0xff007dff,
  style: TextDecorationStyle.SOLID
)
```

触摸点击或鼠标右键点击实体时，会根据实体类型弹出对应的实体操作菜单，鼠标左键点击实体会直接响应菜单的第一个选项。

对addBuilderSpan的节点文本，该功能不会生效。

当copyOptions设置为CopyOptions.None时，点击实体弹出的菜单没有选择文本和复制功能。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enable|Bool|是|-|使能文本识别。true表示使能文本特殊实体识别，false表示不使能文本特殊实体识别。</br>初始值：false|
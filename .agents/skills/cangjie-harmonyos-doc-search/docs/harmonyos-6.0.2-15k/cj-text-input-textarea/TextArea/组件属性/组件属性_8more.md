## 组件属性

> **说明：**
>
> [通用属性padding](./cj-universal-attribute-size.md#func-paddinglength)中top的默认值为8.vp，right的默认值为16.vp，bottom的默认值为8.vp，left的默认值为16.vp。

### func \`type\`(TextAreaType)

```cangjie
public func `type`(value: TextAreaType): This
```

**功能：** 设置输入框类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[TextAreaType](#enum-textareatype)|是|-|输入框类型。<br>初始值：TextAreaType.Normal。|

### func barState(BarState)

```cangjie
public func barState(value: BarState): This
```

**功能：** 设置输入框编辑态时滚动条的显示模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[BarState](./cj-common-types.md#enum-barstate)|是|-|输入框编辑态时滚动条的显示模式。<br>初始值：BarState.Auto。|

### func borderStyle(BorderStyle)

```cangjie
public func borderStyle(style: BorderStyle): This
```

**功能：** 设置边框线条样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|[BorderStyle](./cj-common-types.md#enum-borderstyle)|是|-|元素的边框样式。<br>初始值：BorderStyle.Solid。|

### func caretColor(ResourceColor)

```cangjie
public func caretColor(value: ResourceColor): This
```

**功能：** 设置输入框光标颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|输入框光标颜色。<br>初始值：0xFF0A59F7。|

### func caretStyle(Length, ResourceColor)

```cangjie
public func caretStyle(value: Length, color: ResourceColor): This
```

**功能：** 设置光标风格。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|光标尺寸，不支持百分比。<br>初始值：2.vp。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|光标颜色。<br>初始值：0xFF0A59F7。|

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
> - 设置CopyOptions.None时，当前TextArea中的文字无法被复制、剪切和帮写，仅支持粘贴。
> - 设置CopyOptions.None时，不允许拖拽。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[CopyOptions](./cj-common-types.md#enum-copyoptions)|是|-|输入的文本是否可复制。<br>初始值：CopyOptions.LocalDevice，支持设备内复制。|
### func \`type\`(SearchType)

```cangjie
public func `type`(searchType: SearchType): This
```

**功能：** 设置输入框类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|searchType|[SearchType](#enum-searchtype)|是|-|输入框类型。<br>初始值：SearchType.Normal。|

### func cancelButton(CancelButtonStyle, Length, ResourceColor, String)

```cangjie
public func cancelButton(style!: CancelButtonStyle, size!: Length, color!: ResourceColor, src!: String): This
```

**功能：** 设置右侧清除按钮样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|[CancelButtonStyle](#enum-cancelbuttonstyle)|是|-| **命名参数。** 右侧清除按钮样式。<br>初始值：CancelButtonStyle.INPUT。|
|size|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 图标尺寸，不支持百分比。<br>初始值：16.vp。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-| **命名参数。** 图标颜色。<br>初始值：0x99ffffff。|
|src|String|是|-| **命名参数。** 图标/图片源。<br>初始值：''。|

### func cancelButton(CancelButtonStyle, Length, ResourceColor, AppResource)

```cangjie
public func cancelButton(style!: CancelButtonStyle, size!: Length, color!: ResourceColor, src!: AppResource): This
```

**功能：** 设置右侧清除按钮样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|[CancelButtonStyle](#enum-cancelbuttonstyle)|是|-| **命名参数。** 右侧清除按钮样式。<br>初始值：CancelButtonStyle.INPUT。|
|size|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 图标尺寸，不支持百分比。<br>初始值：16.vp。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-| **命名参数。** 图标颜色。<br>初始值：0x99ffffff。|
|src|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 图标/图片源。|

### func caretStyle(Length, ResourceColor)

```cangjie
public func caretStyle(width!: Length, color!: ResourceColor): This
```

**功能：** 设置光标样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 光标尺寸，不支持百分比。<br>初始值：2.00.vp。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-| **命名参数。** 光标颜色。<br>初始值：0xFF0A59F7。|

### func copyOption(CopyOptions)

```cangjie
public func copyOption(copyOption: CopyOptions): This
```

**功能：** 设置输入的文本是否可复制。

> **说明：**
>
> - 设置CopyOptions.None时，当前Search中的文字无法被复制、剪切、翻译和帮写，仅支持粘贴。
> - 设置CopyOptions.None时，不允许拖拽。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|copyOption|[CopyOptions](./cj-common-types.md#enum-copyoptions)|是|-|search组件的复制选项。<br>初始值：CopyOptions.LocalDevice，支持设备内复制。|
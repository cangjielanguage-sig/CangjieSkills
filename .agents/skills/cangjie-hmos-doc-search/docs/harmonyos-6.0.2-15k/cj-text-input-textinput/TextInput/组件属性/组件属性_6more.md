## 组件属性

> **说明：**
>
> - 默认情况下，通用属性[padding](./cj-universal-attribute-size.md)内top为8.vp，right为16.vp，bottom为8.vp，left为16.vp。
> - 输入框开启下划线模式时，通用属性padding内top为12.vp，right为0.vp，bottom为12.vp，left为0.vp。
> - 当输入框设置padding为0时，可设置borderRadius为0避免光标被截断。

### func barState(BarState)

```cangjie
public func barState(value: BarState): This
```

**功能：** 设置内联输入风格编辑态时滚动条的显示模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[BarState](./cj-common-types.md#enum-barstate)|是|-|内联输入风格编辑态时滚动条的显示模式。<br>初始值：BarState.Auto。|

### func cancelButton(CancelButtonStyle, Length, ResourceColor, String)

```cangjie
public func cancelButton(style!: CancelButtonStyle, size!: Length, color!: ResourceColor, src!: String): This
```

**功能：** 设置右侧清除按钮样式。不支持内联模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|[CancelButtonStyle](./cj-text-input-search.md#enum-cancelbuttonstyle)|是|-| **命名参数。** 右侧清除按钮样式。<br>初始值：CancelButtonStyle.INPUT。|
|size|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 图标尺寸，不支持百分比。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-| **命名参数。** 图标颜色。|
|src|String|是|-| **命名参数。** 图标/图片源。|

### func cancelButton(CancelButtonStyle, Length, ResourceColor, AppResource)

```cangjie
public func cancelButton(style!: CancelButtonStyle, size!: Length, color!: ResourceColor, src!: AppResource): This
```

**功能：** 设置右侧清除按钮样式。不支持内联模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|[CancelButtonStyle](./cj-text-input-search.md#enum-cancelbuttonstyle)|是|-| **命名参数。** 右侧清除按钮样式。<br>初始值：CancelButtonStyle.INPUT。|
|size|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 图标尺寸，不支持百分比。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-| **命名参数。** 图标颜色。<br>初始值：0xFF000000。|
|src|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 图标/图片源。<br>初始值：''。|

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

### func caretPosition(Int32)

```cangjie
public func caretPosition(value: Int32): This
```

**功能：** 设置光标位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|光标的位置。第一个字符前的位置是0。|
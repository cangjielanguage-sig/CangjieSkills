### func baselineOffset(Length)

```cangjie
public func baselineOffset(value: Length): This
```

**功能：** 设置文本基线的偏移量。

> **说明：**
>
> - 正数内容向上偏移，负数向下偏移。
> - 设置该值为百分比时，按默认值显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](cj-common-types.md#interface-length)|是|-|文本基线的偏移量。设置该值为百分比时，按默认值显示。<br>初始值：0。|

### func bindSelectionMenu(TextSpanType, () -> Unit, TextResponseType, (Int32,Int32) -> Unit, () -> Unit)

```cangjie
public func bindSelectionMenu(spanType: TextSpanType, content: () -> Unit, responseType: TextResponseType, onAppear!: (Int32, Int32) -> Unit = {_, _ =>}, onDisappear!: () -> Unit = {=>}): This
```

**功能：** 设置自定义选择菜单。

> **说明：**
>
> - bindSelectionMenu长按响应时长为600ms，bindContextMenu长按响应时长为800ms，同时绑定且触发方式均为长按时，优先响应bindSelectionMenu。
> - 自定义菜单超长时，建议内部嵌套[Scroll](./cj-scroll-swipe-scroll.md)组件使用，避免键盘被遮挡。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|spanType|[TextSpanType](#enum-textspantype)|是|-|选择菜单的类型。<br>初始值：TextSpanType.TEXT。|
|content|()->Unit|是|-|选择菜单的内容。使用时结合[@Builder](../../../Dev_Guide/arkui-cj/paradigm/cj-macro-builder.md)和[bind](./cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。|
|responseType|[TextResponseType](#enum-textresponsetype)|是|-|选择菜单的响应类型。<br>初始值：TextResponseType.LONG_PRESS。|
|onAppear|(Int32, Int32)->Unit|否|{ _,_=> }| **命名参数。** 回调函数，自定义选择菜单弹出时触发。|
|onDisappear|()->Unit|否|{ => }| **命名参数。** 回调函数，自定义选择菜单关闭时触发。|

### func copyOption(CopyOptions)

```cangjie
public func copyOption(value: CopyOptions): This
```

**功能：** 设置组件是否支持文本可复制粘贴。

> **说明：**
>
> 默认文本不可复制粘贴。设置copyOptions为CopyOptions.InApp或者CopyOptions.LocalDevice，长按文本，会弹出文本选择菜单，可选中文本并进行复制、全选操作，此时Text会监听onClick事件，手势事件为非冒泡事件，若需要点击Text组件区域响应父组件的点击手势事件，建议在父组件上使用[parallelGesture](./cj-universal-gesture-bind.md#func-parallelgesturegesturetype)绑定手势识别。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[CopyOptions](./cj-common-types.md#enum-copyoptions)|是|-|组件是否支持文本可复制粘贴。<br>初始值：CopyOptions.None。|
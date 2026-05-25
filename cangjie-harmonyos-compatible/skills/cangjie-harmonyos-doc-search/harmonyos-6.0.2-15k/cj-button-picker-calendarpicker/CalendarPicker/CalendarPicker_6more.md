# CalendarPicker

日历选择器组件，提供下拉日历弹窗，可以让用户选择日期。

## 子组件

无

## 创建组件

### init(CalendarOptions)

```cangjie
public init(options!: CalendarOptions = CalendarOptions())
```

**功能：** 构造一个日历选择器组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[CalendarOptions](#class-calendaroptions)|否|CalendarOptions()| **命名参数。** 配置日历选择器组件的参数。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。

## 组件属性

### func edgeAlign(CalendarAlign, Offset)

```cangjie
public func edgeAlign(alignType: CalendarAlign, offset!: Offset = Offset(0, 0)): This
```

**功能：** 设置选择器与入口组件的对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|alignType|[CalendarAlign](#enum-calendaralign)|是|-|对齐方式类型。<br/>初始值：CalendarAlign.END。|
|offset|[Offset](./cj-common-types.md#class-offset)|否|Offset(0, 0)| **命名参数。** 按照对齐类型对齐后，选择器相对入口组件的偏移量。|

### func textStyle(ResourceColor, Length, FontWeight, String, FontStyle)

```cangjie
public func textStyle(
    color!: ResourceColor = 0xff182431,
    size!: Length = 16.fp,
    weight!: FontWeight = FontWeight.Regular,
    family!: String = "HarmonyOS Sans",
    style!: FontStyle = FontStyle.Normal
): This
```

**功能：** 入口区的文本颜色、字号、字体粗细。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|0xff182431| **命名参数。** 设置入口区的文本颜色。|
|size|[Length](./cj-common-types.md#interface-length)|否|16.fp| **命名参数。** 设置入口区的文本尺寸。|
|weight|[FontWeight](./cj-common-types.md#enum-fontweight)|否|FontWeight.Regular| **命名参数。** 设置入口区的文本字体粗细。|
|family|String|否|"HarmonyOS Sans"| **命名参数。** 设置入口区的文本字体列表。|
|style|[FontStyle](./cj-common-types.md#enum-fontstyle)|否|FontStyle.Normal| **命名参数。** 设置入口区的文本文字样式。|

## 组件事件

### func onChange((DateTime) -> Unit)

```cangjie
public func onChange(callback: (DateTime) -> Unit): This
```

**功能：** 回调函数，选择日期时触发该回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(DateTime)->Unit|是|-|选中的日期值。|
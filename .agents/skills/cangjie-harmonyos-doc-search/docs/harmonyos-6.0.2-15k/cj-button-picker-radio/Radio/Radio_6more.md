# Radio

单选框，提供相应的用户交互选择项。

## 子组件

无

## 创建组件

### init(String, String, RadioIndicatorType, Option\<() -> Unit>)

```cangjie
public init(value!: String, group!: String, indicatorType!: RadioIndicatorType = RadioIndicatorType.TICK,
    indicatorBuilder!: Option<() -> Unit> = Option.None)
```

**功能：** 创建单选框组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-| **命名参数。** 当前单选框的值。|
|group|String|是|-| **命名参数。** 当前单选框的所属群组名称，相同group的Radio只能有一个被选中。|
|indicatorType|[RadioIndicatorType](#enum-radioindicatortype)|是|-| **命名参数。** 配置单选框的选中样式。|
|indicatorBuilder|Option\<()->Unit>|是|-| **命名参数。** 配置单选框的选中样式为自定义UI描述。自定义UI描述与Radio组件为中心点对齐显示。indicatorBuilder设置为Option.None时，按照RadioIndicatorType.TICK进行显示。使用时结合[@Builder](../../../Dev_Guide/arkui-cj/paradigm/cj-macro-builder.md)和[bind](./cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。

## 组件属性

### func checked(Bool)

```cangjie
public func checked(value: Bool): This
```

**功能：** 单选框的选中状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|设置单选框的选中状态。<br>初始值：false。<br/>**说明**：<br/>value为true时，表示从未选中变为选中。value为false时，表示从选中变为未选中。|

### func radioStyle(ResourceColor, ResourceColor, ResourceColor)

```cangjie
public func radioStyle(
    checkedBackgroundColor!: ResourceColor = Color(0x007DFF),
    uncheckedBorderColor!: ResourceColor = Color(0x182431),
    indicatorColor!: ResourceColor = Color.WHITE
): This
```

**功能：** 设置单选框选中状态和非选中状态的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|checkedBackgroundColor|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color(0x007DFF)| **命名参数。** 开启状态底板颜色。|
|uncheckedBorderColor|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color(0x182431)| **命名参数。** 关闭状态描边颜色。|
|indicatorColor|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color.WHITE| **命名参数。** 开启状态内部圆饼颜色。indicatorType设置为RadioIndicatorType.TICK和RadioIndicatorType.DOT时，支持修改内部颜色。indicatorType设置为RadioIndicatorType.CUSTOM时，不支持修改内部颜色。|

## 组件事件

### func onChange((Bool) -> Unit)

```cangjie
public func onChange(callback: (Bool) -> Unit): This
```

**功能：** 单选框选中状态改变时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Bool)->Unit|是|-|单选框的状态。|
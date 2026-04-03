#### init(() -> Unit, () -> Unit, Length, ListItemGroupStyle)

```cangjie
public init(header!: () -> Unit = { => }, footer!: () -> Unit = { => }, space!: Length, style!: ListItemGroupStyle)
```

**功能：** 创建ListItemGroupParams对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|header|()->Unit|否|{ => }| **命名参数。** 设置ListItemGroup头部组件。<br/>**说明：**<br/>可以放单个子组件或不放子组件。|
|footer|()->Unit|否|{ => }| **命名参数。** 设置ListItemGroup尾部组件。<br/>**说明：**<br/>可以放单个子组件或不放子组件。|
|space|[Length](cj-common-types.md#interface-Length)|是|-| **命名参数。** 列表项间距。只作用于ListItem与ListItem之间，不作用于header与ListItem、footer与ListItem之间。<br/>初始值：0。<br/>单位：vp。<br/>**说明：**<br/>设置为负数或者大于等于List内容区长度时，按初始值显示。|
|style|[ListItemGroupStyle](#enum-listitemgroupstyle)|是|-| **命名参数。** 设置List组件卡片样式。<br/>初始值：ListItemGroupStyle.NONE<br/>设置为ListItemGroupStyle.NONE时无样式。设置为ListItemGroupStyle.CARD时，建议配合ListItem的ListItemStyle.CARD同时使用，显示默认卡片样式。<br/>卡片样式下，ListItemGroup初始规格：左右外边距12.vp，上下左右内边距4.vp。<br/>卡片样式下，为卡片内的列表选项提供了默认的focus、hover、press、selected和disable样式。<br/>**说明：**<br/>当前卡片模式下，使用默认Axis.Vertical排列方向，如果listDirection属性设置为Axis.Horizontal，会导致显示混乱；List属性alignListItem默认为ListItemAlign.Center，居中对齐显示。|
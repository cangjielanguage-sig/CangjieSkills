# Column

沿垂直方向布局的容器。

## 子组件

可以包含子组件。

## 创建组件

### init()

```cangjie
public init()
```

**功能：** 创建一个不包含子组件的Column容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(() -> Unit)

```cangjie
public init(child: () -> Unit)
```

**功能：** 创建一个可包含子组件的Column容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|child|()->Unit|是|-|Column 容器的子组件。|

### init(Length, () -> Unit)

```cangjie
public init(space: Length, child: () -> Unit)
```

**功能：** 创建一个纵向布局元素垂直方向间距为space且可以包含子组件的Column容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|space|[Length](cj-common-types.md#interface-length)|是|-|纵向布局元素垂直方向间距。<br> space为负数或者[justifyContent](#func-justifycontentflexalign)设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时不生效。 <br> 初始值：0 <br> 单位：vp <br> **说明：** <br> space为大于等于0的数字。|
|child|()->Unit|是|-|Column 容器的子组件。|

### init(Length)

```cangjie
public init(space: Length)
```

**功能：** 创建一个纵向布局元素垂直方向间距为space且可以包含子组件的Column容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|space|[Length](cj-common-types.md#interface-length)|是|-|纵向布局元素垂直方向间距。<br> space为负数或者[justifyContent](#func-justifycontentflexalign)设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时不生效。<br> 初始值：0 <br> 单位：vp <br> **说明：** <br> 可选值为大于等于0的数字。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。

## 组件属性

### func alignItems(HorizontalAlign)

```cangjie
public func alignItems(value: HorizontalAlign): This
```

**功能：** 设置子组件在水平方向上的对齐格式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[HorizontalAlign](cj-common-types.md#enum-horizontalalign)|是|-|子组件在水平方向上的对齐格式。<br> 初始值：HorizontalAlign.Center|

### func justifyContent(FlexAlign)

```cangjie
public func justifyContent(value: FlexAlign): This
```

**功能：** 设置子组件在垂直方向上的对齐格式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

> **说明：**
>
> Column布局时若子组件不设置[flexShrink](cj-universal-attribute-flexlayout.md#func-flexshrinkfloat64)则默认不会压缩子组件，即所有子组件主轴大小累加可超过容器主轴。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FlexAlign](cj-common-types.md#enum-flexalign)|是|-|设置子组件在垂直方向上的对齐格式。 <br> 初始值：FlexAlign.Start|
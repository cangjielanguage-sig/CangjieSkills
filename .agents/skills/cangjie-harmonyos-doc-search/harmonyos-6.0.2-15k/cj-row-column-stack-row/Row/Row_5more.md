# Row

沿水平方向布局的容器。

## 子组件

可以包含子组件。

## 创建组件

### init(() -> Unit)

```cangjie
public init(child: () -> Unit)
```

**功能：** 创建一个包含子组件的Row容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init()

```cangjie
public init()
```

**功能：** 创建一个Row容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(Length)

```cangjie
public init(space: Length)
```

**功能：** 创建一个横向布局元素间距为space的Row容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|space|[Length](cj-common-types.md#interface-length)|是|-|横向布局元素间距。<br>space为负数或者justifyContent设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时不生效。<br> 初始值：0，单位：vp <br> **说明：** 可选值为大于等于0的数字。|

### init(Length, () -> Unit)

```cangjie
public init(space: Length, child: () -> Unit)
```

**功能：** 创建一个横向布局元素间距为space的Row容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|space|[Length](cj-common-types.md#interface-length)|是|-|横向布局元素间距。<br>space为负数或者justifyContent设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时不生效。<br> 初始值：0，单位：vp <br> **说明：** 可选值为大于等于0的数字。|
|child|()->Unit|是|-|容器内的子组件。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。

## 组件属性

### func alignItems(VerticalAlign)

```cangjie
public func alignItems(algin: VerticalAlign): This
```

**功能：** 设置子组件在垂直方向上的对齐格式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algin|[VerticalAlign](cj-common-types.md#enum-verticalalign)|是|-|在垂直方向上子组件的对齐格式。<br> 初始值：VerticalAlign.Center|

### func justifyContent(FlexAlign)

```cangjie
public func justifyContent(algin: FlexAlign): This
```

**功能：** 设置子组件在水平方向上的对齐格式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algin|[FlexAlign](cj-common-types.md#enum-flexalign)|是|-|子组件在水平方向上的对齐格式。<br> 初始值：FlexAlign.Start|

> **说明：**
>
> Row布局时若子组件不设置[flexShrink](cj-universal-attribute-flexlayout.md#func-flexshrinkfloat64)则默认不会压缩子组件，即所有子组件主轴大小累加可超过容器主轴。
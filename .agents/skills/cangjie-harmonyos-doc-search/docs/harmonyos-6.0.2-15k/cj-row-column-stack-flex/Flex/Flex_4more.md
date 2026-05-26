# Flex

Flex是以弹性方式布局子组件的容器组件，提供更加有效的方式对容器内的子元素进行排列、对齐和分配剩余空间。

具体指南请参考[弹性布局](../../../Dev_Guide/arkui-cj/cj-layout-development-flex-layout.md)。

> **说明：**
>
> - Flex组件在渲染时存在二次布局过程，因此在对性能有严格要求的场景下建议使用[Column](cj-row-column-stack-column.md)、[Row](cj-row-column-stack-row.md)代替。
> - Flex组件主轴默认不设置时撑满父容器，[Column](cj-row-column-stack-column.md)、[Row](cj-row-column-stack-row.md)组件主轴不设置时默认是跟随子节点大小。
> - 主轴长度可设置为auto使Flex自适应子组件布局，自适应时，Flex长度受constraintSize属性以及父容器传递的最大最小长度限制且constraintSize属性优先级更高。

## 子组件

可以包含子组件。

## 创建组件

### Flex(FlexParams)

```cangjie
public Flex(value: FlexParams)
```

**功能：** 创建一个Flex容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FlexParams](#class-flexparams)|是|-|子组件在Flex容器上排列、对齐方式。|

### init(FlexParams, () -> Unit)

```cangjie
public init(value: FlexParams, child: () -> Unit)
```

**功能：** 创建一个可包含子组件的Flex容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FlexParams](#class-flexparams)|是|-|子组件在Flex容器上排列、对齐方式。|
|child|()->Unit|是|-|声明容器内的子组件。|

### init(() -> Unit)

```cangjie
public init(child: () -> Unit)
```

**功能：** 创建一个可包含子组件的Flex容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|child|()->Unit|是|-|声明容器内的子组件。|

### init(FlexOptions)

```cangjie
public init(value: FlexOptions)
```

**功能：** 创建一个Flex容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FlexOptions](#class-flexoptions)|是|-|弹性布局子组件参数。|

### init(FlexOptions, () -> Unit)

```cangjie
public init(value: FlexOptions, child: () -> Unit)
```

**功能：** 创建一个可包含子组件的Flex容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FlexOptions](#class-flexoptions)|是|-|弹性布局子组件参数。|
|child|()->Unit|是|-|声明容器内的子组件。|

## 通用属性/通用事件

通用属性：除文本样式外，其余全部支持；对于自身独有 alignItems 属性的容器组件，通用属性 align 不生效。

通用事件：全部支持。
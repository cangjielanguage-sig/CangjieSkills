# Flex

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

Flex是以弹性方式布局子组件的容器组件，提供更加有效的方式对容器内的子元素进行排列、对齐和分配剩余空间。

具体指南请参考[弹性布局](../../arkui-cj/cj-layout-development-flex-layout.md)。

> **说明：**
>
> - Flex组件在渲染时存在二次布局过程，因此在对性能有严格要求的场景下建议使用[Column](cj-row-column-stack-column.md)、[Row](cj-row-column-stack-row.md)代替。
> - Flex组件主轴默认不设置时撑满父容器，[Column](cj-row-column-stack-column.md)、[Row](cj-row-column-stack-row.md)组件主轴不设置时默认是跟随子节点大小。
> - 主轴长度可设置为auto使Flex自适应子组件布局，自适应时，Flex长度受constraintSize属性以及父容器传递的最大最小长度限制且constraintSize属性优先级更高。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

可以包含子组件。

## 创建组件

### init(?FlexDirection, ?FlexWrap, ?FlexAlign, ?ItemAlign, ?FlexAlign, () -> Unit)

```cangjie
public init(direction!: ?FlexDirection = None, wrap!: ?FlexWrap = None,
    justifyContent!: ?FlexAlign = None, alignItems!: ?ItemAlign = None,
    alignContent!: ?FlexAlign = None, child!: () -> Unit = {=>})
```

**功能：** 创建一个Flex容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|direction|?[FlexDirection](./cj-common-types.md#enum-flexdirection)|否|None| **命名参数。** 初始值: FlexDirection.Row 子组件在Flex容器上排列的方向，即主轴的方向。|
|wrap|?[FlexWrap](./cj-common-types.md#enum-flexwrap)|否|None| **命名参数。** 初始值: FlexWrap.NoWrap Flex容器是单行/列还是多行/列排列。|
|justifyContent|?[FlexAlign](./cj-common-types.md#enum-flexalign)|否|None| **命名参数。** 初始值: FlexAlign.Start 所有子组件在Flex容器主轴上的对齐格式。|
|alignItems|?[ItemAlign](./cj-common-types.md#enum-itemalign)|否|None| **命名参数。** 初始值: ItemAlign.Start 所有子组件在Flex容器交叉轴上的对齐格式。|
|alignContent|?[FlexAlign](./cj-common-types.md#enum-flexalign)|否|None| **命名参数。** 初始值: FlexAlign.Start 交叉轴中有额外的空间时，多行内容的对齐方式。仅在wrap为Wrap或WrapReverse下生效。|
|child|()->Unit|否|{=>}| **命名参数。** 声明容器内的子组件。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。
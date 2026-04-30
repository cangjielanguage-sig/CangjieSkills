## func markAnchor(Length, Length)

```cangjie
public func markAnchor(x!: Length, y!: Length): This
```

**功能：** 设置元素在位置定位时的锚点。从position或offset的位置上，进一步偏移。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** x轴坐标。|
|y|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** y轴坐标。|

> - **说明：**
>
> - 设置.position(x: value1, y: value2).markAnchor(x: value3, y: value4)，效果等于设置.position(x: value1 - value3, y: value2 - value4)，offset同理。单独使用markAnchor，设置.markAnchor(x: value1, y: value2)，效果等于设置.offset(x: -value1, y: -value2)。

## func offset(Length, Length)

```cangjie
public open func offset(x!: Length, y!: Length): This
```

**功能：** 相对偏移，组件相对原本的布局位置进行偏移。offset属性不影响父容器布局，仅在绘制时调整位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** x轴坐标。|
|y|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** y轴坐标。|

> - **说明：**
>
> - Position类型基于组件自身左上角偏移，Edges类型基于组件自身四边偏移。 offset属性设置 (x: x, y: y) 与设置 (left: x, top: y) 以及 (right: -x, bottom: -y) 效果相同, 类型LocalizedEdges支持镜像模式：LTR模式下start 等同于x，RTL模式下等同于-x。

## func position(Length, Length)

```cangjie
public func position(x!: Length, y!: Length): This
```

**功能：** 绝对定位，确定子组件相对父组件的位置。当父容器为Row/Column/Flex时，设置position的子组件不占位。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** x轴坐标。|
|y|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** y轴坐标。|

> - **说明：**
>
> - Position类型基于父组件左上角确定位置。
> - 适用于置顶显示、悬浮按钮等组件在父容器中位置固定的场景。
> - 不支持在宽高为零的布局容器上设置。
> - 当父容器为[RelativeContainer](./cj-row-column-stack-relativecontainer.md#relativecontainer), 且子组件设置了alignRules属性, 则子组件的position属性不生效。
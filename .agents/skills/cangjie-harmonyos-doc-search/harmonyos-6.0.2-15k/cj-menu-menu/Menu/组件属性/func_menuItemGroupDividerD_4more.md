### func menuItemGroupDivider(?DividerStyleOptions)

```cangjie
public func menuItemGroupDivider(options: ?DividerStyleOptions): This
```

**功能：** 设置menuItemGroup上下分割线的样式，不设置该属性则默认展示分割线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|?[DividerStyleOptions](./cj-common-types.md#class-dividerstyleoptions)|是|-|设置menuItemGroup顶部和底部分割线样式。<br/>-strokeWidth：分割线的线宽, 初始值：1.px。<br/>-color：分割线的颜色, 初始值： 0x33000000。<br/>-startMargin：分割线与menuItemGroup侧边起端的距离, 初始值：16。<br/>-endMargin：分割线与menuItemGroup侧边结束端的距离, 初始值：16。|

### func radius(Length)

```cangjie
public func radius(value: Length): This
```

**功能：** 设置Menu边框圆角半径。

> **说明：**
>
> 水平方向两个圆角半径之和的最大值大于菜单宽度，或垂直方向两个圆角半径之和的最大值大于菜单高度时，菜单四个圆角均采用菜单默认圆角半径值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|Menu边框圆角半径。<br/>初始值：20.vp。|

### func radius(BorderRadiuses)

```cangjie
public func radius(value: BorderRadiuses): This
```

**功能：** 设置Menu边框圆角半径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[BorderRadiuses](./cj-common-types.md#class-borderradiuses)|是|-|Menu边框圆角半径。|

### func subMenuExpandingMode(SubMenuExpandingMode)

```cangjie
public func subMenuExpandingMode(mode: SubMenuExpandingMode): This
```

**功能：** 设置Menu子菜单展开样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[SubMenuExpandingMode](#enum-submenuexpandingmode)|是|-|Menu子菜单展开样式。<br/>初始值：SubMenuExpandingMode.SIDE_EXPAND|
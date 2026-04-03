# 外描边设置

设置组件外描边（outline）样式。外描边绘制在组件的外侧，不影响布局，不会占用组件本身大小。

![outlineTest](figures/outlineTest.PNG)

## func outline(Length, ResourceColor, Length, OutlineStyle)

```cangjie
public func outline(
    width!: Length,
    color!: ResourceColor = Color.BLACK,
    radius!: Length = 0.vp,
    style!: OutlineStyle = OutlineStyle.SOLID
): This
```

**功能：** 设置外描边样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| width | [Length](cj-common-types.md#interface-length) | 是 |\- | **命名参数。**  外描边宽度，不支持百分比。<br>**说明：**  width为必设项，否则不显示外描边。|
| color | [ResourceColor](cj-common-types.md#interface-resourcecolor) | 否  | Color.BLACK | **命名参数。**  外描边颜色。|
| radius | [Length](cj-common-types.md#interface-length) | 否 | 0.vp | **命名参数。**  外描边圆角半径，不支持百分比。<br>**说明：** 最大生效值：组件width/2 + outlineWidth或组件height/2 + outlineWidth。|
| style | [OutlineStyle](cj-common-types.md#enum-outlinestyle) | 否 | OutlineStyle.SOLID | **命名参数。**  外描边样式。|

## func outlineColor(ResourceColor)

```cangjie
public func outlineColor(value: ResourceColor): This
```

**功能：** 设置元素的外描边颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| value | [ResourceColor](cj-common-types.md#interface-resourcecolor) | 是 | \- | 元素的外描边颜色。<br> 初始值：Color.BLACK |

## func outlineColor(ResourceColor, ResourceColor, ResourceColor, ResourceColor)

```cangjie
public func outlineColor(
    top!: ResourceColor = Color.BLACK, right!: ResourceColor = Color.BLACK, bottom!: ResourceColor = Color.BLACK, left!: ResourceColor = Color.BLACK): This
```

**功能：** 设置元素的外描边颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| top | [ResourceColor](cj-common-types.md#interface-resourcecolor) | 否 | Color.BLACK | **命名参数。**  上侧外描边颜色。|
| right | [ResourceColor](cj-common-types.md#interface-resourcecolor) | 否 | Color.BLACK | **命名参数。**  右侧外描边颜色。|
| bottom | [ResourceColor](cj-common-types.md#interface-resourcecolor) | 否 | Color.BLACK | **命名参数。**  下侧外描边颜色。 |
| left | [ResourceColor](cj-common-types.md#interface-resourcecolor) | 否 | Color.BLACK | **命名参数。**  左侧外描边颜色。|

## func outlineRadius(Length)

```cangjie
public open func outlineRadius(value: Length): This
```

**功能：** 设置元素的外描边圆角半径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| value | [Length](cj-common-types.md#interface-length) | 是 | \- |元素的外描边圆角半径，不支持百分比。 <br> 初始值：0。 <br> 最大生效值：组件width/2 + outlineWidth或组件height/2 + outlineWidth。|
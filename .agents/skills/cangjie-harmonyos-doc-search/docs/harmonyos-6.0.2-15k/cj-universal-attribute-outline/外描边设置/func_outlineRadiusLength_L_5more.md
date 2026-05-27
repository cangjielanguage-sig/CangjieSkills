## func outlineRadius(Length, Length, Length, Length)

```cangjie
public func outlineRadius(
    topLeft!: Length = 0.vp, topRight!: Length = 0.vp, bottomLeft!: Length = 0.vp, bottomRight!: Length = 0.vp): This
```

**功能：** 设置元素的外描边圆角半径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| topLeft | [Length](cj-common-types.md#interface-length) | 否 | 0.vp | **命名参数。**  左上角圆角半径。|
| topRight | [Length](cj-common-types.md#interface-length) | 否  | 0.vp | **命名参数。**  右上角圆角半径。|
| bottomLeft | [Length](cj-common-types.md#interface-length) | 否 | 0.vp | **命名参数。**  左下角圆角半径。|
| bottomRight | [Length](cj-common-types.md#interface-length) | 否 | 0.vp | **命名参数。**  右下角圆角半径。|

## func outlineStyle(OutlineStyle)

```cangjie
public open func outlineStyle(value: OutlineStyle): This
```

**功能：** 设置元素的外描边样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| value | [OutlineStyle](cj-common-types.md#enum-outlinestyle) | 是 | \- | 元素的外描边样式。<br>初始值：OutlineStyle.SOLID|

## func outlineStyle(OutlineStyle, OutlineStyle, OutlineStyle, OutlineStyle)

```cangjie
public func outlineStyle(
    top!: OutlineStyle = OutlineStyle.SOLID, right!: OutlineStyle = OutlineStyle.SOLID, bottom!: OutlineStyle = OutlineStyle.SOLID, left!: OutlineStyle = OutlineStyle.SOLID): This
```

**功能：** 设置元素的外描边样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| top | [OutlineStyle](cj-common-types.md#enum-outlinestyle) | 否 | OutlineStyle.SOLID | **命名参数。**  上侧外描边样式。|
| right | [OutlineStyle](cj-common-types.md#enum-outlinestyle) | 否 | OutlineStyle.SOLID | **命名参数。**  右侧外描边样式。|
| bottom | [OutlineStyle](cj-common-types.md#enum-outlinestyle) | 否 | OutlineStyle.SOLID | **命名参数。**  下侧外描边样式。|
| left | [OutlineStyle](cj-common-types.md#enum-outlinestyle) | 否 | OutlineStyle.SOLID | **命名参数。**  左侧外描边样式。|

## func outlineWidth(Length)

```cangjie
public open func outlineWidth(value: Length): This
```

**功能：** 设置元素的外描边宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| value | [Length](cj-common-types.md#interface-length) | 是 | \- | 元素的外描边宽度。初始值：0 。<br> **说明：** 不支持百分比。<br> 外描边效果width为必设项。|

## func outlineWidth(Length, Length, Length, Length)

```cangjie
public func outlineWidth(
    top!: Length = 0.vp, right!: Length = 0.vp, bottom!: Length = 0.vp, left!: Length = 0.vp): This
```

**功能：** 设置外描边的宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| top | [Length](cj-common-types.md#interface-length) | 否 | 0.vp | **命名参数。**  上侧外描边宽度。|
| right | [Length](cj-common-types.md#interface-length) | 否 | 0.vp | **命名参数。**  右侧外描边宽度。|
| bottom | [Length](cj-common-types.md#interface-length) | 否 | 0.vp | **命名参数。**  下侧外描边宽度。|
| left | [Length](cj-common-types.md#interface-length) | 否 | 0.vp | **命名参数。**  左侧外描边宽度。|
# 边框设置

设置组件边框样式。

## func border(Length, ResourceColor, Length, BorderStyle)

```cangjie
public func border(width!: Length, color!: ResourceColor = Color.BLACK, radius!: Length = 0.vp, style!: BorderStyle = BorderStyle.Solid): This
```

**功能：** 设置边框样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :---------- | :---------- | :------- | :-------- | :--------------------------------------------------|
| width | [Length](./cj-common-types.md#interface-length) | 是 | - | **命名参数。**  边框宽度。|
| color | [ResourceColor](./cj-common-types.md#interface-resourcecolor)   | 否  | Color.BLACK | **命名参数。**  边框颜色。|
| radius | [Length](./cj-common-types.md#interface-length)  | 否 | 0.vp | **命名参数。**  边框圆角半径。|
| style | [BorderStyle](./cj-common-types.md#enum-borderstyle) | 否 | BorderStyle.Solid | **命名参数。**  边框样式。|

## func borderStyle(BorderStyle)

```cangjie
public func borderStyle(style: BorderStyle): This
```

**功能：** 设置元素的边框线条样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :--------| :---------- | :------- | :------ | :------- |
| style | [BorderStyle](./cj-common-types.md#enum-borderstyle) | 是 | - | 元素的边框样式。<br>初始值：BorderStyle.Solid。|

## func borderWidth(Length)

```cangjie
public func borderWidth(width: Length): This
```

**功能：** 设置边框的宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :-------- | :---------- | :------- | :------ | :------- |
| width | [Length](./cj-common-types.md#interface-length)  | 是 | - | 设置元素的边框宽度，不支持百分比。|

## func borderWidth(EdgeWidths)

```cangjie
public func borderWidth(edgeWidths: EdgeWidths): This
```

**功能：** 设置边框的宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :------- | :---------- | :------- | :------ | :------- |
| edgeWidths | [EdgeWidths](./cj-universal-attribute-border.md#class-edgewidths) | 是 | - | 设置元素的边框宽度，不支持百分比。|

## func borderColor(ResourceColor)

```cangjie
public func borderColor(color: ResourceColor): This
```

**功能：** 设置边框的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :------- | :---------- | :---------- | :------- | :------ |
| color |[ResourceColor](./cj-common-types.md#interface-resourcecolor)| 是 | -| 元素的边框颜色。<br>初始值：Color.BLACK。|

## func borderRadius(Length)

```cangjie
public open func borderRadius(radius: Length): This
```

**功能：** 设置边框的圆角。圆角大小受组件尺寸限制，最大值为组件宽或高的一半。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :------ | :---------- | :------- | :-------- | :---------|
| radius | [Length](./cj-common-types.md#interface-length)  | 是 | - | 元素的边框圆角半径，支持百分比，百分比依据组件宽度。设置圆角后，可搭配[clip](./cj-universal-attribute-shapclip.md#func-clipbool)属性进行裁剪，避免子组件超出组件自身。|
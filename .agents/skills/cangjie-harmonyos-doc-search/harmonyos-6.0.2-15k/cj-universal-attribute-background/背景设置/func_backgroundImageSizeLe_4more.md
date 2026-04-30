## func backgroundImageSize(Length, Length)

```cangjie
public func backgroundImageSize(width!: Length = 0.vp, height!: Length = 0.vp): This
```

**功能：** 设置组件背景图片的宽高。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 名称     | 类型        | 必填     | 默认值     | 说明                                              |
|:--------|:------------| :------- | :-------- |:------------------------------------------------|
| width | [Length](./cj-common-types.md#interface-length)  | 否 | 0.vp | **命名参数。**  背景图片的宽度。|
| height | [Length](./cj-common-types.md#interface-length)  | 否 | 0.vp | **命名参数。**  背景图片的高度。 |

> **说明：**
>
> - 如果只设置一个属性，则第二个属性保持图片原始宽高比进行调整。默认保持原图的比例不变，width和height取值范围： [0, +∞)。
> - width和height均设置为小于或等于0的值时，按值为0显示。当width和height中只有一个值未设置或者设置为小于等于0的值时，另一个会根据图片原始宽高比进行调整。

## func backgroundImagePosition(Length, Length)

```cangjie
public func backgroundImagePosition(x!: Length = 0.vp, y!: Length = 0.vp): This
```

**功能：** 设置背景图的位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 名称 | 类型  | 必填 | 默认值 |      说明       |
|:----|:------|:---|:----|:--------------|
| x  | [Length](./cj-common-types.md#interface-length) | 否 | 0.vp | **命名参数。**  相对于组件左上角的x坐标。 |
| y  | [Length](./cj-common-types.md#interface-length) | 否 | 0.vp | **命名参数。**  相对于组件左上角的y坐标。 |

> **说明：**
>
> x和y值设置百分比时，偏移量是相对组件自身宽高计算的。

## func backgroundImagePosition(Alignment)

```cangjie
public func backgroundImagePosition(align: Alignment): This
```

**功能：** 设置背景图的位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 名称 | 类型  | 必填 | 默认值   | 说明                   |
|:----|:------|:---|:------|:--------------------------------|
| align | [Alignment](./cj-common-types.md#enum-alignment) | 是  | - | 背景图在组件中显示位置。 |

## func BackgroundBlurStyle(BlurStyle, Option\<BackgroundBlurStyleOptions>)

```cangjie
public func backgroundBlurStyle(value!: BlurStyle, options!: Option<BackgroundBlurStyleOptions> = None): This
```

**功能：** 为当前组件提供一种在背景和内容之间的模糊能力，通过枚举值的方式封装了不同的模糊半径、蒙版颜色、蒙版透明度、饱和度、亮度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)|是|-| **命名参数。** 背景模糊样式。模糊样式中封装了模糊半径、蒙版颜色、蒙版透明度、饱和度、亮度五个参数。|
|options|[BackgroundBlurStyleOptions](./cj-universal-attribute-background.md#class-backgroundblurstyleoptions)|否|None| **命名参数。** 背景模糊选项。|
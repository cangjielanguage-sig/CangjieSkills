# 背景设置

设置组件的背景样式。

## func backdropBlur(Float64)

```cangjie
public func backdropBlur(value: Float64): This
```

**功能：** 为组件添加背景模糊效果，可以自定义设置模糊半径和灰阶参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 名称    | 类型     | 必填     | 默认值     |  说明     |
|:-------| :---------- | :------- | :-------- |:--------|
| value  | Float64  | 是 | - | 为当前组件添加背景模糊效果，入参为模糊半径，模糊半径越大越模糊，为0时不模糊。 |

> **说明：**
>
> blur和backdropBlur是实时模糊接口，会每帧进行实时渲染，性能负载较高。当模糊内容和模糊半径都不需要变化时，建议使用[静态模糊接口](../apis/ArkGraphics2D/cj-apis-effect_kit.md#func-blurfloat32)。

## func backgroundColor(ResourceColor)

```cangjie
public open func backgroundColor(color: ResourceColor): This
```

**功能：** 设置组件背景颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 名称    | 类型     | 必填     | 默认值     |  说明     |
|:-------| :---------- | :------- | :-------- |:--------|
| color | [ResourceColor](./cj-common-types.md#interface-resourcecolor)  | 是 | - | 组件的背景色。 |

> **说明：**
>
> 当通过[backgroundBlurStyle](./cj-universal-attribute-background.md#func-backgroundblurstyleblurstyle-optionbackgroundblurstyleoptions)中的inactiveColor指定背景色时，不建议再通过[backgroundColor](./cj-universal-attribute-background.md#func-backgroundcolorresourcecolor)设置背景色。

## func backgroundImage(AppResource, ImageRepeat)

```cangjie
public func backgroundImage(src!: AppResource, repeat!: ImageRepeat = ImageRepeat.NoRepeat): This
```

**功能：** 设置组件的背景图片。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 名称    | 类型          | 必填     | 默认值     | 说明                                      |
|:--------|:--------------| :------- | :-------- |:----------------------------------------|
| src  | [AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)  | 是 | - | **命名参数。**  图片地址，支持网络图片资源和本地图片资源地址和Base64，不支持svg类型的图片。 |
| repeat  | [ImageRepeat](./cj-common-types.md#enum-imagerepeat) | 否 | ImageRepeat.NoRepeat | **命名参数。**  设置背景图片的重复样式，默认不重复。当设置的背景图片为透明底色图片，且同时设置了backgroundColor时，二者叠加显示，背景颜色在最底部。|

## func backgroundImage(String, ImageRepeat)

```cangjie
public func backgroundImage(src!: String, repeat!: ImageRepeat = ImageRepeat.NoRepeat): This
```

**功能：** 设置组件的背景图片。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 名称     | 类型          | 必填     | 默认值     | 说明                                      |
|:--------|:--------------| :------- | :-------- |:----------------------------------------|
| src | String | 是 | - | **命名参数。**  图片地址，支持网络图片资源和本地图片资源地址和Base64，不支持svg类型的图片。 |
| repeat  | [ImageRepeat](./cj-common-types.md#enum-imagerepeat) | 否 | ImageRepeat.NoRepeat | **命名参数。**  背景图片的重复样式，默认不重复。当设置的背景图片为透明底色图片，且同时设置了backgroundColor时，二者叠加显示，背景颜色在最底部。|

## func backgroundImageSize(ImageSize)

```cangjie
public func backgroundImageSize(imageSize: ImageSize): This
```

**功能：** 设置组件背景图片的宽高。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 名称 | 类型| 必填 | 默认值     | 说明                                |
|:----|:---------------|:---| :-------- |:----------------------------------|
|imageSize | [ImageSize](./cj-common-types.md#enum-imagesize) | 是  | - | 背景图像的高度和宽度。<br>初始值：ImageSize.Auto。|
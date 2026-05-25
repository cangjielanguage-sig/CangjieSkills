# 组件内容填充方式

用于决定在组件的宽高动画过程中，如何将动画最终的组件内容绘制在组件上。

## func renderFit(RenderFit)

```cangjie
public func renderFit(fitMode: RenderFit): This
```

**功能：** 设置宽高动画过程中的组件内容填充方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| fitMode | [RenderFit](#enum-renderfit)  | 是  | - | 宽高动画过程中的组件内容填充方式。 <br/>初始值：RenderFit.TOP_LEFT。|

> **说明：**
>
> 对于TEXTURE和SURFACE类型的[XComponent](./cj-rendering-drawing-xcomponent.md)组件，当不设置renderFit属性时，取默认值为RenderFit.RESIZE_FILL。
> 对于SURFACE类型的XComponent组件，当组件背景色为不透明的纯黑色时，其renderFit通用属性仅支持设置为RenderFit.RESIZE_FILL，不推荐设置为其他的RenderFit枚举值。
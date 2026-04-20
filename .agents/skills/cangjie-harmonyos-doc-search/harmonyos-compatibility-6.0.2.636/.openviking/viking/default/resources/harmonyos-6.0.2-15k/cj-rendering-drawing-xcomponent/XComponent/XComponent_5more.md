# XComponent

提供用于图形绘制和媒体数据写入的Surface，XComponent负责将其嵌入到视图中，支持应用自定义Surface位置和大小。具体指南请参考[自定义渲染 (XComponent)](../../../Dev_Guide/arkui-cj/cj-common-components-xcomponent.md)文档。

## 子组件

无

## 创建组件

### init(String, XComponentType, XComponentController)

```cangjie
public init(id!: String, `type`!: XComponentType, controller!: XComponentController)
```

**功能：** 创建一个XComponent组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|String|是|-| **命名参数。** 组件的唯一标识，支持最大的字符串长度128。|
|\`type`|[XComponentType](./cj-common-types.md#enum-xcomponenttype)|是|-| **命名参数。** 用于指定XComponent组件类型。|
|controller|[XComponentController](#class-xcomponentcontroller)|是|-| **命名参数。** 给组件绑定一个控制器，通过控制器调用组件方法，仅XComponent类型为"SURFACE"时有效。|

## 通用属性/通用事件

通用属性：部分支持。

> **说明：**
>
> - 不支持foregroundColor、obscured和pixelStretchEffect属性，并且\`type`为SURFACE类型时也不支持动态属性设置、自定义绘制、背景设置(backgroundColor除外)、图像效果(shadow除外)、maskShape和foregroundEffect属性。
> - 对于TEXTURE和SURFACE类型的XComponent组件，当不设置[renderFit](cj-universal-attribute-renderfit.md)属性时，取初始值为RenderFit.RESIZE_FILL。
> - 对于SURFACE类型的XComponent组件，当组件背景色为不透明的纯黑色时，其[renderFit](cj-universal-attribute-renderfit.md)通用属性仅支持设置为RenderFit.RESIZE_FILL，设置为其他的RenderFit枚举值显示异常。

通用事件：\`type`为SURFACE或TEXTURE时，支持通用事件。

## 组件属性

### func enableSecure(Bool)

```cangjie
public func enableSecure(isSecure: Bool): This
```

**功能：** 防止组件内自绘制内容被截屏、录屏。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isSecure|Bool|是|-|是否开启隐私图层模式。|

> **说明：**
>
> 仅\`type`为SURFACE时有效。
# QRCode

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

一个用于显示单个二维码的组件。

> **说明：**
>
> 二维码组件的像素点数量与内容有关。当组件尺寸过小时，可能出现无法展示内容的情况，此时需要适当调整组件尺寸。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

无

## 创建组件

### init(?ResourceStr)

```cangjie
public init(value: ?ResourceStr)
```

**功能：** 创建用于显示单个二维码组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-|二维码内容字符串。最大支持512个字符，若超出，则截取前512个字符。初始值："undefined"。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：支持[点击事件](cj-universal-event-click.md)、[触摸事件](cj-universal-event-touch.md)、[挂载卸载事件](cj-universal-event-appear.md)。

## 组件属性

### func color(?ResourceColor)

```cangjie
public func color(value: ?ResourceColor): This
```

**功能：** 设置二维码颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|二维码颜色。初始值：0xff000000，且不跟随系统深浅色模式切换而修改。|

### func contentOpacity(?Float64)

```cangjie
public func contentOpacity(value: ?Float64): This
```

**功能：** 设置二维码内容颜色的不透明度。不透明度最小值为0.0，最大值为1.0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Float64|是|-|二维码内容颜色的不透明度。初始值：1.0。取值范围：[0.0, 1.0]，超出取值范围按初始值处理。|

### func contentOpacity(?AppResource)

```cangjie
public func contentOpacity(value: ?AppResource): This
```

**功能：** 设置二维码内容颜色的不透明度。不透明度最小值为0，最大值为1。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[AppResource](../LocalizationKit/cj-apis-resource.md#class-appresource)|是|-|二维码内容颜色的不透明度。<br>初始值：1.0。|
# Image

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

Image为图片组件，常用于在应用中显示图片。支持png、jpg、jpeg、bmp、svg、webp、gif和heif类型的图片格式。

> 说明：
>
> - 使用快捷组合键对Image组件复制时，Image组件必须处于[获焦状态](./cj-universal-attribute-focus.md#func-focusontouchbool)。Image组件默认不获焦，需将[focusable](cj-apis-window.md#var-focusable)属性设置为true，即可使用TAB键将焦点切换到组件上，再将[focusOnTouch](./cj-universal-attribute-focus.md#func-focusontouchbool)属性设置为true，即可实现点击获焦。
> - 图片格式支持SVG图源，SVG标签文档请参考[SVG标签说明](../ImageKit/cj-apis-image.md#svg标签说明)。
> - 动图的播放依赖于Image节点的可见性变化，其默认行为是不播放的。当节点可见时，通过回调启动动画，当节点不可见时，停止动画。可见性状态的判断是通过[onVisibleAreaChange](./cj-universal-event-visibleareachange.md#func-onvisibleareachangearrayfloat64-bool-float64---unit)事件触发的，当可见阈值ratios大于0时，表明Image处于可见状态。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 权限列表

使用网络图片时，需要在 module.json5 对应的"requestPermissions"中添加网络使用权限ohos.permission.INTERNET。

```json
"requestPermissions": [
    { "name": "ohos.permission.INTERNET"}
]
```

## 子组件

无

## 创建组件

### init(?ResourceStr)

```cangjie
public init(src: ?ResourceStr)
```

**功能：** 通过图片数据源获取图片，用于后续渲染展示。

> **说明：**
>
> - Image组件加载图片失败或图片尺寸为0时，图片组件大小自动为0，不跟随父组件的布局约束。
> - Image组件默认按照居中裁剪，例如组件宽高设置相同，原图长宽不等，此时按照中间区域进行裁剪。
> - Image加载成功且组件不设置宽高时，其显示大小自适应父组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-|图片的数据源。<br>初始值：""|

### init(?PixelMap)

```cangjie
public init(src: ?PixelMap)
```

**功能：** 通过图片数据源获取图片，用于后续渲染展示。

  > **说明：**
  >
  > - Image组件加载图片失败或图片尺寸为0时，图片组件大小自动为0，不跟随父组件的布局约束。
  > - Image组件默认按照居中裁剪，例如组件宽高设置相同，原图长宽不等，此时按照中间区域进行裁剪。
  > - Image加载成功且组件不设置宽高时，其显示大小自适应父组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|?[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|是|-|图片的数据源。<br/>PixelMap格式为像素图，常用于图片编辑的场景。|

## 通用属性/通用事件

通用属性：全部支持。

> **说明：**
>
> Image组件不支持设置通用属性[foregroundColor](./cj-universal-attribute-foregroundcolor.md#func-foregroundcolorresourcecolor)，可以通过Image组件的[fillColor](#func-fillcolorresourcecolor)属性设置填充颜色。

通用事件：全部支持。
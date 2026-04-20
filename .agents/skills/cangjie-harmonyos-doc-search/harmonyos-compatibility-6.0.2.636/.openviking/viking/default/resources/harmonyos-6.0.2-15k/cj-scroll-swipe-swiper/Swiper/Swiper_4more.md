# Swiper

滑块视图容器，提供子组件滑动轮播显示的能力。

> **说明：**
>
> Swiper组件内包含了[PanGesture](./cj-universal-gesture-pangesture.md)拖动手势事件，用于滑动轮播子组件。[disableSwipe](#func-disableswipebool)属性设为true会取消内部的PanGesture事件监听。

## 子组件

可以包含子组件。

> **说明：**
>
> - 子组件类型：系统组件和自定义组件，支持渲染控制类型（[if/else](../../../Dev_Guide/arkui-cj/rendering_control/cj-rendering-control-ifelse.md)、[ForEach](../../../Dev_Guide/arkui-cj/rendering_control/cj-rendering-control-foreach.md)和[LazyForEach](../../../Dev_Guide/arkui-cj/rendering_control/cj-rendering-control-lazyforeach.md)）。不建议子组件中混用懒加载组件（包括LazyForEach）和非懒加载组件，或者子组件中使用多个懒加载组件，否则可能导致懒加载组件预加载能力失效等问题。不建议在组件动画过程中对数据源进行操作，否则会导致布局出现异常。
> - Swiper子组件的[visibility](./cj-universal-attribute-visibility.md#func-visibilityvisibility)属性设置为Visibility.None，且Swiper的displayCount属性设置为'auto'时，对应子组件在视窗内不占位，但不影响导航点个数；visibility属性设置为Visibility.None或者Visibility.Hidden时，对应子组件不显示，但依然会在视窗内占位。
> - 当Swiper子组件设置了[offset](./cj-universal-attribute-location.md#func-offsetlength-length)属性时，会按照子组件的层级进行绘制，层级高的子组件会覆盖层级低的子组件。例如，Swiper包含3个子组件，其中第3个子组件设置了offset({ x : 100 })，那么在横向循环滑动中，第3个子组件会覆盖第1个子组件，此时可设置第1个子组件的[zIndex](./cj-universal-attribute-zorder.md#func-zindexint32)属性值大于第3个子组件，使第1个子组件层级高于第3个子组件。

## 创建组件

### init(SwiperController, () -> Unit)

```cangjie
public init(controller: SwiperController, subcomponent: () -> Unit)
```

**功能：** 创建一个包含Swiper控制器和子组件的Swiper对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|controller|[SwiperController](#class-swipercontroller)|是|-|给组件绑定一个控制器，用来控制组件翻页。|
|subcomponent|()->Unit|是|-|Swiper容器的子组件。|

### init(() -> Unit)

```cangjie
public init(subcomponent: () -> Unit)
```

**功能：** 创建一个可包含子组件的Swiper容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|subcomponent|()->Unit|是|-|Swiper容器的子组件。|

## 通用属性/通用事件

通用属性：全部支持。

> **说明：**
>
> Swiper组件[通用属性clip](./cj-universal-attribute-shapclip.md#func-clipbool)的初始值为true。

通用事件：全部支持。
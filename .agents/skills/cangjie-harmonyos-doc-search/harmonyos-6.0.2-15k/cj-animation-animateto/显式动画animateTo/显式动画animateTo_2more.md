# 显式动画（animateTo）

提供全局animateTo显式动画接口来指定由于闭包代码导致的状态变化插入过渡动效。同[属性动画](./cj-animation-animation.md)，布局类改变宽高的动画，内容都是直接到终点状态。例如文字、[Canvas](./cj-canvas-drawing-canvas.md)的内容等。如果期望内容跟随宽高变化，可以使用[renderFit](./cj-universal-attribute-renderfit.md)属性配置。

## func animateTo(AnimateParam,() -> Unit)

```cangjie
public func animateTo(animation: AnimateParam, callback: () -> Unit): Unit
```

**功能：** 提供全局animateTo显式动画接口来指定由于闭包代码导致的状态变化插入过渡动效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

> **说明：**
>
> - 不推荐在[aboutToAppear](./cj-custom-component-lifecycle.md#func-aboutToappear)、[aboutToDisappear](./cj-custom-component-lifecycle.md#func-aboutTodisappear)中调用动画。
> - 如果在[aboutToAppear](./cj-custom-component-lifecycle.md#func-aboutToappear)中调用动画，自定义组件内的build还未执行，内部组件还未创建，动画时机过早，动画属性没有初值无法对组件产生动画。
> - 执行[aboutToDisappear](./cj-custom-component-lifecycle.md#func-aboutTodisappear)时，组件即将销毁，不能在aboutToDisappear里面做动画。
> - 在组件出现和消失时，可以通过[组件内转场](./cj-animation-transition.md)添加动画效果。
> - 组件内转场不支持的属性，可以参考[示例2](#示例代码2动画执行结束后组件消失)，使用animateTo实现动画执行结束后组件消失的效果。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|animation|[AnimateParam](#class-animateparam)|是|-|设置动画效果相关参数。|
|callback |() -> Unit|是|-|指定动效的闭包函数，在闭包函数中导致的状态变化系统会自动插入过渡动画。|
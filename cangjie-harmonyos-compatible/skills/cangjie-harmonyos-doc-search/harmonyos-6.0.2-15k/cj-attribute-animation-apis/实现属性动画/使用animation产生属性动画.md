## 使用animation产生属性动画

相比于animateTo接口需要把要执行动画的属性的修改放在闭包中，[animationStart](../../API_Reference/source_zh_cn/arkui-cj/cj-animation-animation.md#func-animationstart)和[animationEnd](../../API_Reference/source_zh_cn/arkui-cj/cj-animation-animation.md#func-animationend)接口无需使用闭包，把animationStart接口加在组件的第一个属性，animationEnd接口加在组件的最后一个属性即可。animationStart和animationEnd只要检测到其绑定的可动画属性发生变化，就会自动添加属性动画，animateTo则必须在动画闭包内改变可动画属性的值从而生成动画。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var animate: Bool = false
    //第一步：声明相关状态变量
    @State
    var rotateValue: Float32 = 0.0
    @State
    var translateX: Float32 = 0.0
    @State
    var opacityValue: Float32 = 1.0

    //第二步：将状态变量设置到相关可动画属性接口
    func build() {
        Row {
            //组件一
            Column {
            }.animationStart(AnimateParam(curve: Curve.Smooth)).opacity(Float64(this.opacityValue)).rotate(
                this.rotateValue).backgroundColor(0x317AF7).justifyContent(FlexAlign.Center).width(100.vp).height(
                100.vp).borderRadius(30.vp).onClick {
                evt =>
                this.animate = !this.animate
                if (this.animate) {
                    this.rotateValue = 90.0
                } else {
                    this.rotateValue = 0.0
                }
                if (this.animate) {
                    this.opacityValue = 0.6
                } else {
                    this.opacityValue = 1.0
                }
                if (this.animate) {
                    this.translateX = 50.0
                } else {
                    this.translateX = 0.0
                }
            }.animationEnd()

            //组件二
            Column {
            }.animationStart(AnimateParam(curve: Curve.Smooth)).justifyContent(FlexAlign.Center).width(100.vp).height(
                100.vp).backgroundColor(0xD94838).borderRadius(30.vp).opacity(Float64(this.opacityValue)).translate(
                x: Float64(this.translateX)).animationEnd()
        }.width(100.percent).height(100.percent).justifyContent(FlexAlign.Center)
    }
}
```

![animation6](./figures/animation6.gif)

> **说明：**
>
> - 在对组件的位置大小的变化做动画的时候，由于布局属性的改变会触发测量布局，性能开销大。[scale](../../API_Reference/source_zh_cn/arkui-cj/cj-universal-attribute-transform.md#func-scalefloat32-float32-float32-length-length)属性的改变不会触发测量布局，性能开销小。因此，在组件位置大小持续发生变化的场景，如跟手触发组件大小变化的场景，推荐适用scale。
>
> - 属性动画应该作用于始终存在的组件，对于将要出现或者将要消失的组件的动画应该使用[转场动画](./cj-transition-overview.md)。
>
> - 尽量不要使用动画结束回调。属性动画是对已经发生的状态进行的动画，不需要开发者去处理结束的逻辑。如果要使用结束回调，一定要正确处理连续操作的数据管理。
# 组件可见区域变化事件

组件可见区域变化事件是组件在屏幕中的显示区域面积变化时触发的事件，提供了判断组件是否完全或部分显示在屏幕中的能力，适用于广告曝光埋点之类的场景。

## func onVisibleAreaChange(Array\<Float64>, (Bool, Float64)->Unit)

```cangjie
public func onVisibleAreaChange(raitos: Array<Float64>, callback: (Bool, Float64)->Unit): This
```

**功能：** 组件可见区域变化时触发的事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|raitos|Array\<Float64>|是|-|阈值数组。其中，每个阈值代表组件可见面积（即组件在屏幕显示区的面积，只计算父组件内的面积，超出父组件部分不会计算）与组件自身面积的比值。当组件可见面积与自身面积的比值接近阈值时，均会触发该回调。每个阈值的取值范围为[0.0, 1.0]，如果开发者设置的阈值超出该范围，则会实际取值0.0或1.0。**说明：** 当数值接近边界0和1时，将会按照误差不超过0.001的规则进行舍入。例如，0.9997会被近似为1。|
|callback|(Bool, Float64)->Unit|是|-|组件可见区域变化事件的回调。参数一：表示组件的可见面积与自身面积的比值与上一次变化相比的情况，比值变大为true，比值变小为false。参数二：触发回调时，组件可见面积与自身面积的比值。|

> **说明：**
>
> - 仅提供自身节点相对于所有祖先节点（直到window边界）的相对裁切面积与自身面积的比值及其变化趋势。
> - 不支持兄弟组件对自身节点的遮挡计算，不支持所有祖先的兄弟节点对自身节点的遮挡计算，如[Stack](../../../Dev_Guide/arkui-cj/cj-layout-development-stack-layout.md#层叠布局-stack)、[Z序控制](../../../Dev_Guide/arkui-cj/cj-layout-development-stack-layout.md#z序控制)等。
> - 不支持非挂树节点的可见面积变化计算。例如，预加载的节点、通过[overlay](./cj-universal-attribute-overlay.md#func-overlaystring-alignment-contentoffset)能力挂载的自定义节点。
# 自定义事件分发

在处理触屏事件时，会在触屏事件触发前进行按压点和组件区域的触摸测试，来收集需要响应触屏事件的组件，再基于触摸测试结果分发相应的触屏事件。在父节点，开发者可以通过onChildTouchTest决定如何让子节点去做触摸测试，影响子组件的触摸测试，最终影响后续的触屏事件分发，具体影响参考[TouchTestStrategy](#enum-touchteststrategy)枚举说明。

> **说明：**
>
> onClick、旋转、捏合手势经过自定义事件分发后可能会因为触摸热区没有命中导致事件不响应。

## func onChildTouchTest((Array\<TouchTestInfo>) -> TouchResult)

```cangjie
public func onChildTouchTest(callback: (Array<TouchTestInfo>) -> TouchResult): This
```

**功能：** 设置自定义子节点的触摸测试事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Array\<[TouchTestInfo](#class-touchtestinfo)>)->[TouchResult](#class-touchresult)|是|-|回调函数，自定义子节点进行触摸测试时触发。<br/>参数：包含子节点信息的数组。<br/>返回值：自定义事件分发结果。|
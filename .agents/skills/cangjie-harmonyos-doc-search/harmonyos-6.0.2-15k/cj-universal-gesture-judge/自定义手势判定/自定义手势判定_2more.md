# 自定义手势判定

为组件提供自定义手势判定能力。开发者可根据需要，在手势识别期间，决定是否响应手势。

## func onGestureJudgeBegin((GestureInfo, BaseGestureEvent) -> GestureJudgeResult)

```cangjie
public func onGestureJudgeBegin(callback: (GestureInfo, BaseGestureEvent) -> GestureJudgeResult): This
```

**功能：** 给组件绑定自定义手势判定回调，当绑定到该组件的手势被接受时，会触发用户定义的回调来获取结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureInfo](#class-gestureinfo), [BaseGestureEvent](#class-basegestureevent))->[GestureJudgeResult](#enum-gesturejudgeresult)|是|-|给组件绑定自定义手势判定回调，当绑定到该组件的手势被接受时，会触发用户定义的回调来获取结果。|
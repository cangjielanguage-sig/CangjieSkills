## func onGestureRecognizerJudgeBegin((BaseGestureEvent, GestureRecognizer, Array\<GestureRecognizer>) -> GestureJudgeResult)

```cangjie
public func onGestureRecognizerJudgeBegin(callback: (BaseGestureEvent, GestureRecognizer, Array<GestureRecognizer>) -> GestureJudgeResult): This
```

**功能：** 给组件绑定自定义手势识别器判定回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([BaseGestureEvent](./cj-universal-gesture-judge.md#class-basegestureevent),[GestureRecognizer](#class-gesturerecognizer),Array\<[GestureRecognizer](#class-gesturerecognizer)>)->[GestureJudgeResult](./cj-universal-gesture-judge.md#enum-gesturejudgeresult)|是|-|给组件绑定自定义手势识别器判定回调，当绑定到该组件的手势被接受时，会触发用户定义的回调来获取结果。<br>参数一：当前基础手势事件信息。<br>参数二：当前即将要响应的识别器对象。<br>参数三：响应链上的其他手势识别器对象。<br>返回值：手势是否裁决成功的判定结果。|
# 手势拦截增强

为组件提供手势拦截能力。开发者可根据需要，将系统内置手势和比其优先级高的手势做并行化处理，并可以动态控制手势事件的触发。

## func shouldBuiltInRecognizerParallelWith((GestureRecognizer, Array\<GestureRecognizer>) -> GestureRecognizer)

```cangjie
public func shouldBuiltInRecognizerParallelWith(callback: (GestureRecognizer, Array<GestureRecognizer>) -> GestureRecognizer): This
```

**功能：** 提供系统内置手势与响应链上其他组件的手势设置并行关系的回调事件，当该组件进行触摸碰撞测试时，会触发用户定义的回调来形成手势并行关系。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([GestureRecognizer](#class-gesturerecognizer),Array\<[GestureRecognizer](#class-gesturerecognizer)>)->[GestureRecognizer](#class-gesturerecognizer)|是|-|提供系统内置手势与响应链上其他组件的手势设置并行关系的回调事件，当该组件进行触摸碰撞测试时，会触发用户定义的回调来形成手势并行关系。<br>参数一：当前组件的系统内置手势识别器，当前版本只提供内置的[PAN_GESTURE](./cj-universal-gesture-judge.md#pan_gesture)类型的手势识别器。<br>参数二：响应链上更高优先级的其他组件相同类别的手势识别器。<br>返回值：与current识别器绑定并行关系的某个手势识别器。|

## func onGestureRecognizerJudgeBegin((BaseGestureEvent, GestureRecognizer, Array\<GestureRecognizer>) -> GestureJudgeResult, Bool)

```cangjie
public func onGestureRecognizerJudgeBegin(callback: (BaseGestureEvent, GestureRecognizer, Array<GestureRecognizer>) -> GestureJudgeResult, exposeInnerGesture: Bool): This
```

**功能：** 给组件绑定自定义手势识别器判定回调。

新增exposeInnerGesture参数作为是否将回调暴露给ArkUI系统组合组件的内置组件的标识，当该标识置为true时，将回调暴露给cangjie系统组合组件的内置组件。

对于不需要将回调暴露给cangjie系统组合组件内置组件的场景，建议采用原有[onGestureRecognizerJudgeBegin](#func-ongesturerecognizerjudgebeginbasegestureevent-gesturerecognizer-arraygesturerecognizer---gesturejudgeresult)接口。若要求将回调暴露给cangjie系统组合组件的内置组件，建议使用该接口并将exposeInnerGesture设置为true。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([BaseGestureEvent](./cj-universal-gesture-judge.md#class-basegestureevent),[GestureRecognizer](#class-gesturerecognizer),Array\<[GestureRecognizer](#class-gesturerecognizer)>)->[GestureJudgeResult](./cj-universal-gesture-judge.md#enum-gesturejudgeresult)|是|-|给组件绑定自定义手势识别器判定回调，当绑定到该组件的手势被接受时，会触发用户定义的回调来获取结果。<br>参数一：当前基础手势事件信息。<br>参数二：当前即将要响应的识别器对象。<br>参数三：响应链上的其他手势识别器对象。<br>返回值：手势是否裁决成功的判定结果。|
|exposeInnerGesture|Bool|是|-|暴露内部手势标识。<br>初始值：false。<br>**说明：**<br>如果是组合组件，此参数设置true，则会在current参数回调出组合组件内部的手势识别器。当前仅支持[Tabs](./cj-navigation-switching-tabs.md#tabs)，其他组件请不要设置此参数。设置为false时，功能与原接口[onGestureRecognizerJudgeBegin](#func-ongesturerecognizerjudgebeginbasegestureevent-gesturerecognizer-arraygesturerecognizer---gesturejudgeresult)相同。|
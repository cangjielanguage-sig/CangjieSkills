# 运动模糊

设置组件由缩放大小或位移变化引起的运动过程中的动态模糊效果。需要与动画的AnimateParam的onFinish参数配合使用。

## func motionBlur(MotionBlurOptions)

```cangjie
public func motionBlur(value: MotionBlurOptions): This
```

**功能：** 在当前组件由缩放大小或位移变化引起的运动过程中，增加动态模糊效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

> **说明：**
>
> - 不建议在组件内转场、共享元素转场、组件内隐式元素转场、粒子动画场景下使用该属性，否则会有非预期效果。
> - 该属性需要在开始状态将motionBlur的参数radius设置为0，否则冷启动时会有非预期效果。
> - 该属性需要与动画的AnimateParam的onFinish参数配合使用，需要在运动模糊动画结束后将motionBlur的参数radius置为0，否则会有非预期效果。
> - 在使用该属性过程中，不要在使用过程中频繁更改同一个组件的模糊半径，否则会有非预期效果。比如示例中的动画，频繁点击会出现模糊效果偶尔失效的情况。
> - 运动模糊锚点坐标需要与动画缩放的锚点保持一致，否则会有非预期效果。
> - 模糊半径建议设置1以内，否则会有非预期效果。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[MotionBlurOptions](#class-motionbluroptions)|是|-|定义运动模糊参数。|
# 共享元素转场（sharedTransition）

可以通过设置组件的 sharedTransition 属性将该元素标记为共享元素并设置对应的共享元素转场动效。sharedTransition仅发生在页面路由（router）跳转时。

## func sharedTransition(String, SharedTransitionOptions)

```cangjie
public func sharedTransition(id: String, options!: SharedTransitionOptions): This
```

**功能：** 设置共享元素转场。

> **说明：**
>
> type为SharedTransitionEffectType.Exchange时motionPath才会生效。type为SharedTransitionEffectType.Exchange时，效果为对匹配的共享元素产生位置、大小的过渡（可通过配置组件的border观察），不支持内容的过渡效果。例如，Text组件在两个页面上使用不同的fontSize属性值，即绘制内容有大小差异，在sharedTransition动画结束后的最后一帧，Text的fontSize效果会突变为跳转目标页fontSize的效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|String|是|-|两个页面中id值相同且不为空字符串的组件即为共享元素，在页面转场时可显示共享元素转场动效。|
|options|[SharedTransitionOptions](#sharedtransitionoptions)|是|-| **命名参数。** 共享元素转场动画参数。type为SharedTransitionEffectType.Exchange时motionPath才会生效。|
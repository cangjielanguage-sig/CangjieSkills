# 组件内转场（transition）

组件内转场主要通过transition属性配置转场参数，在组件插入和删除时显示过渡动效，主要用于容器组件中的子组件插入和删除时，提升用户体验。

> **说明：**
>
> 当前有两种方式触发组件的transition：
>
> - 当组件插入或删除时（如if条件改变、ForEach新增删除组件），会递归的触发所有新插入/删除的组件的transition效果。
> - 当组件[Visibility](./cj-universal-attribute-visibility.md)属性在可见和不可见之间改变时，只触发该组件的transition效果。

## func transition()

```cangjie
public func transition(): This
```

**功能：** 设置组件插入显示和删除隐藏的过渡效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## func transition(TransitionEffect)

```cangjie
public func transition(effect: TransitionEffect): This
```

**功能：** 设置组件插入显示和删除隐藏的过渡效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|effect|[TransitionEffect](#class-transitioneffect)|是|-|以函数的形式指定转场效果。|

## func transition(TransitionEffect, (Bool)->Unit)

```cangjie
public func transition(effect: TransitionEffect, onFinish: (Bool) -> Unit)
```

**功能：** 设置组件插入显示和删除隐藏的过渡效果和转场动画结束回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|effect|[TransitionEffect](#class-transitioneffect)|是|-|以函数的形式指定转场效果。|
|onFinish|(Bool) -> Unit|是|-|组件转场动画的结束回调类型。<br/>该参数为true表示该转场回调是出现动画的结束回调，该参数为false表示该转场回调是消失动画的结束回调。|
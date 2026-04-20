# 组件内转场（transition）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

组件内转场主要通过transition属性配置转场参数，在组件插入和删除时显示过渡动效，主要用于容器组件中的子组件插入和删除时，提升用户体验。

> **说明：**
>
> 当前有两种方式触发组件的transition：
>
> - 当组件插入或删除时（如if条件改变、ForEach新增删除组件），会递归的触发所有新插入/删除的组件的transition效果。
> - 当组件[Visibility](./cj-universal-attribute-visibility.md)属性在可见和不可见（[Visibility.Hidden](./cj-common-types.md#enum-visibility)或[Visibility.None](./cj-common-types.md#enum-visibility)）之间改变时，只触发该组件的transition效果。在[Visibility.Visible](./cj-common-types.md#enum-visibility)与[Visibility.None](./cj-common-types.md#enum-visibility)之间切换时，若直接设置为Visibility.None，会导致组件布局大小为0，此时无法观察到transition效果。而当在动画中修改visiblity属性为[Visibility.None](./cj-common-types.md#enum-visibility)时，组件布局为0是带动画的，将呈现transition与布局动画的叠加效果，形成双动画的复合表现。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## func transition(?TransitionEffect)

```cangjie
func transition(value: ?TransitionEffect): T
```

**功能：** 设置组件插入显示和删除隐藏的过渡效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[TransitionEffect](#class-transitioneffect)|是|-|设置组件插入显示和删除隐藏的过渡效果。|

**返回值：**

|类型|说明|
|:----|:----|
|T|返回组件实例。|

## func transition(?TransitionEffect, ?TransitionFinishCallback)

```cangjie
func transition(value: ?TransitionEffect, onFinish: ?TransitionFinishCallback): T
```

**功能：** 设置组件插入显示和删除隐藏的过渡效果和转场动画结束回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[TransitionEffect](#class-transitioneffect)|是|-|设置组件插入显示和删除隐藏的过渡效果。|
|onFinish|?[TransitionFinishCallback](./cj-common-types.md#type-transitionfinishcallback)|是|-|组件转场动画的结束回调类型。<br>该参数为true表示该转场回调是出现动画的结束回调，该参数为false表示该转场回调是消失动画的结束回调。|

**返回值：**

|类型|说明|
|:----|:----|
|T|返回组件实例。|
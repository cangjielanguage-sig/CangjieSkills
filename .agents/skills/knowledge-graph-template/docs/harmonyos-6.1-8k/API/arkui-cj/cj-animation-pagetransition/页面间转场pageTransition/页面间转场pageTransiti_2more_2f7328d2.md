# 页面间转场（pageTransition）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

当路由（[Router](./cj-apis-uicontext-router.md)）进行切换时，可以通过在[pageTransition](./cj-custom-component-lifecycle.md#func-pagetransition)函数中自定义页面入场和页面退场的转场动效。详细指导请参考[页面转场动画](../../arkui-cj/cj-page-transition-animation.md)。

> **说明：**
>
> 为了实现更好的转场效果，推荐使用Navigation组件和[模态转场](../../arkui-cj/cj-modal-transition.md)。

## 导入模块

```cangjie
import kit.ArkUI.*
```
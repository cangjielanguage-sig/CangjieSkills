## type配置为RouteType.Push或RouteType.Pop

type为RouteType.Push表示仅对页面栈的push操作生效，type为RouteType.Pop表示仅对页面栈的pop操作生效。

```cangjie
// page A
protected func pageTransition(): Unit {
    // 定义页面进入时的效果，从右侧滑入，时长为1200ms，页面栈发生push操作时该效果才生效
    PageTransitionEnter(PageTransitionOptions(`type`: RouteType.Push, duration: 1200)).slide(SlideEffect.Right)
    // 定义页面进入时的效果，从左侧滑入，时长为1200ms，页面栈发生pop操作时该效果才生效
    PageTransitionEnter(PageTransitionOptions(`type`: RouteType.Pop, duration: 1200)).slide(SlideEffect.Left)
    // 定义页面退出时的效果，向左侧滑出，时长为1000ms，页面栈发生push操作时该效果才生效
    PageTransitionExit(PageTransitionOptions(`type`: RouteType.Push, duration: 1000)).slide(SlideEffect.Left)
    // 定义页面退出时的效果，向右侧滑出，时长为1000ms，页面栈发生pop操作时该效果才生效
    PageTransitionExit(PageTransitionOptions(`type`: RouteType.Pop, duration: 1000)).slide(SlideEffect.Right)
}
```

```cangjie
// page B
protected func pageTransition(): Unit {
    // 定义页面进入时的效果，从右侧滑入，时长为1000ms，页面栈发生push操作时该效果才生效
    PageTransitionEnter(PageTransitionOptions(`type`: RouteType.Push, duration: 1000)).slide(SlideEffect.Right)
    // 定义页面进入时的效果，从左侧滑入，时长为1000ms，页面栈发生pop操作时该效果才生效
    PageTransitionEnter(PageTransitionOptions(`type`: RouteType.Pop, duration: 1000)).slide(SlideEffect.Left)
    // 定义页面退出时的效果，向左侧滑出，时长为1200ms，页面栈发生push操作时该效果才生效
    PageTransitionExit(PageTransitionOptions(`type`: RouteType.Push, duration: 1200)).slide(SlideEffect.Left)
    // 定义页面退出时的效果，向右侧滑出，时长为1200ms，页面栈发生pop操作时该效果才生效
    PageTransitionExit(PageTransitionOptions(`type`: RouteType.Pop, duration: 1200)).slide(SlideEffect.Right)
}
```

以上代码则完整的定义了所有可能的页面转场样式。假设页面跳转配置为多实例模式，即页面栈中允许存在重复的页面。可能出现的4种场景对应的页面转场效果如下表。

|路由操作|页面A转场效果|页面B转场效果|
|:---|:---|:---|
|router.pushUrl，从页面A跳转到新增的页面B|页面退出，PageTransitionExit且type为RouteType.Push的转场样式生效，向左侧滑出屏幕|页面进入，PageTransitionEnter且type为RouteType.Push的转场样式生效，从右侧滑入屏幕|
|router.back，从页面B返回到页面A|页面进入，PageTransitionEnter且type为RouteType.Pop的转场样式生效，从左侧滑入屏幕|页面退出，PageTransitionExit且type为RouteType.Pop的转场样式生效，向右侧滑出屏幕|
|router.pushUrl，从页面B跳转到新增的页面A|页面进入，PageTransitionEnter且type为RouteType.Push的转场样式生效，从右侧滑入屏幕|页面退出，PageTransitionExit且type为RouteType.Push的转场样式生效，向左侧滑出屏幕|
|router.back，从页面A返回到页面B|页面退出，PageTransitionExit且type为RouteType.Pop的转场样式生效，向右侧滑出屏幕|页面进入，PageTransitionEnter且type为RouteType.Pop的转场样式生效，从左侧滑入屏幕|

> **说明：**
>
> - 由于每个页面的页面转场样式都可由开发者独立配置，而页面转场涉及到两个页面，开发者应考虑两个页面的页面转场效果的衔接，如时长尽量保持一致。
> - 如果没有定义匹配的页面转场样式，则该页面使用系统默认的页面转场样式。
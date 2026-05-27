## type配置为RouteType.None

type为RouteType.None表示对页面栈的push、pop操作均生效，type的默认值为RouteType.None。

```cangjie
// page A
protected func pageTransition(): Unit {
    // 定义页面进入时的效果，从左侧滑入，时长为1200ms，无论页面栈发生push还是pop操作均可生效
    PageTransitionEnter(PageTransitionOptions(`type`: RouteType.None, duration: 1200)).slide(SlideEffect.Left)
    // 定义页面退出时的效果，向左侧滑出，时长为1000ms，无论页面栈发生push还是pop操作均可生效
    PageTransitionExit(PageTransitionOptions(`type`: RouteType.None, duration: 1000)).slide(SlideEffect.Left)
}
```

```cangjie
// page B
protected func pageTransition(): Unit {
    // 定义页面进入时的效果，从右侧滑入，时长为1000ms，无论页面栈发生push还是pop操作均可生效
    PageTransitionEnter(PageTransitionOptions(`type`: RouteType.None, duration: 1000)).slide(SlideEffect.Right)
    // 定义页面退出时的效果，向右侧滑出，时长为1200ms，无论页面栈发生push还是pop操作均可生效
    PageTransitionExit(PageTransitionOptions(`type`: RouteType.None, duration: 1200)).slide(SlideEffect.Right)
}
```

假设页面跳转配置为多实例模式，即页面栈中允许存在重复的页面。可能出现的4种场景对应的页面转场效果如下表。

|路由操作|页面A转场效果|页面B转场效果|
|:---|:---|:---|
|router.pushUrl，从页面A跳转到新增的页面B|页面退出，PageTransitionExit生效，向左侧滑出屏幕|页面进入，PageTransitionEnter生效，从右侧滑入屏幕|
|router.back，从页面B返回到页面A|页面进入，PageTransitionEnter生效，从左侧滑入屏幕|页面退出，PageTransitionExit生效，向右侧滑出屏幕|
|router.pushUrl，从页面B跳转到新增的页面A|页面进入，PageTransitionEnter生效，从左侧滑入屏幕|页面退出，PageTransitionExit生效，向右侧滑出屏幕|
|router.back，从页面A返回到页面B|页面退出，PageTransitionExit生效，向左侧滑出屏幕|页面进入，PageTransitionEnter生效，从右侧滑入屏幕|

如果希望pushUrl进入的页面总是从右侧滑入，back时退出的页面总是从右侧滑出，则上表中的第3、4种情况不满足要求，那么需要完整的定义4个页面转场效果。
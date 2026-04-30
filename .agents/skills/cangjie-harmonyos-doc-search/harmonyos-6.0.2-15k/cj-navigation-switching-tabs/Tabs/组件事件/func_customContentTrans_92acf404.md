### func customContentTransition((Int32, Int32) -> Option\<TabContentAnimatedTransition>)

```cangjie
public func customContentTransition(callback: (from: Int32, to: Int32) -> Option<TabContentAnimatedTransition>): This
```

**功能：** 自定义Tabs页面切换动画。

使用说明：

1、当使用自定义切换动画时，Tabs组件自带的默认切换动画会被禁用，同时，页面也无法跟手滑动。<br>
2、当设置为Option.None时，表示不使用自定义切换动画，仍然使用组件自带的默认切换动画。<br>
3、当前自定义切换动画不支持打断。<br>
4、目前自定义切换动画只支持两种场景触发：点击页签和调用TabsController.changeIndex()接口。<br>
5、当使用自定义切换动画时，Tabs组件支持的事件中，除了onGestureSwipe，其他事件均支持。<br>
6、onChange和onAnimationEnd事件的触发时机需要特殊说明：如果在第一次自定义动画执行过程中，触发了第二次自定义动画，那么在开始第二次自定义动画时，就会触发第一次自定义动画的onChange和onAnimationEnd事件。<br>
7、当使用自定义动画时，参与动画的页面布局方式会改为Stack布局。如果开发者未主动设置相关页面的zIndex属性，那么所有页面的zIndex值是一样的，页面的渲染层级会按照在组件树上的顺序（即页面的index值顺序）确定。因此，开发者需要主动修改页面的zIndex属性，来控制页面的渲染层级。<br>

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int32, Int32)->Option\<[TabContentAnimatedTransition](#class-tabcontentanimatedtransition)>|是|-|自定义Tabs页面切换动画开始时触发的回调。<br>参数：<br>from：动画开始时，当前页面的index值，索引从0开始。<br>to：动画开始时，目标页面的index值，索引从0开始。<br>返回值：自定义切换动画相关信息。|
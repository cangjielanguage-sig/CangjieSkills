### func onContentWillChange((Int32, Int32) -> Bool)

```cangjie
public func onContentWillChange(callback: (currentIndex: Int32, comingIndex: Int32) -> Bool): This
```

**功能：** 自定义Tabs页面切换拦截事件能力，新页面即将显示时触发该回调。

满足以下任一条件，即可触发该事件：

1、滑动TabContent切换新页面时触发。

2、通过TabsController.changeIndex接口切换新页面时触发。

3、通过动态修改index属性值切换新页面时触发。

4、通过点击TabBar页签切换新页面时触发。

5、TabBar页签获焦后，通过键盘左右方向键等切换新页面时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int32, Int32)->Bool|是|-|自定义Tabs页面切换拦截事件能力，新页面即将显示时触发的回调。<br>参数：<br>currentIndex：当前显示页面的index索引，索引从0开始计算。<br>comingIndex：将要显示的新页面的index索引。<br>返回值：<br>当回调函数callback的返回值为true时，Tabs可以切换到新页面。<br>当回调函数callback的返回值为false时，Tabs无法切换到新页面，仍然显示原来页面内容。|

### func onGestureSwipe((Int32, event: TabsAnimationEvent) -> Unit)

```cangjie
public func onGestureSwipe(callback: (index: Int32, event: TabsAnimationEvent) -> Unit): This
```

**功能：** 在页面跟手滑动过程中，逐帧触发该回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int32, [TabsAnimationEvent](#class-tabsanimationevent))->Unit|是|-|在页面跟手滑动过程中，逐帧触发的回调。<br>参数：<br>index：当前显示元素的索引，索引从0开始。<br>event：动画相关信息，只返回主轴方向上当前显示元素相对于Tabs起始位置的位移。|

### func onTabBarClick((Int32) -> Unit)

```cangjie
public func onTabBarClick(callback: (index: Int32) -> Unit): This
```

**功能：** Tab页签点击后触发的事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int32)->Unit|是|-|Tab页签点击后触发的事件。<br>参数：<br>index：被点击的index索引，索引从0开始计算。|
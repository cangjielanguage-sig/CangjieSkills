### func onAnimationEnd((Int32, TabsAnimationEvent) -> Unit)

```cangjie
public func onAnimationEnd(callback: (index: Int32, event: TabsAnimationEvent) -> Unit): This
```

**功能：** 切换动画结束时触发该回调。当Tabs切换动效结束时触发，包括动画过程中手势中断。参数为动画结束后的index值。当[animationDuration](#func-animationdurationfloat32)为0时动画关闭，不触发该回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int32, [TabsAnimationEvent](#class-tabsanimationevent))->Unit|是|-|切换动画结束时触发的回调。<br>参数：<br>index：当前显示元素的索引，索引从0开始。<br>event：动画相关信息，只返回主轴方向上当前显示元素相对于Tabs起始位置的位移。|

### func onAnimationStart((Int32, Int32, TabsAnimationEvent) -> Unit)

```cangjie
public func onAnimationStart(callback: (index: Int32, targetIndex: Int32, event: TabsAnimationEvent) -> Unit): This
```

**功能：** 切换动画开始时触发该回调。参数为动画开始前的index值（不是最终结束动画的index值）。当[animationDuration](#func-animationdurationfloat32)为0时动画关闭，不触发该回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int32, Int32,[TabsAnimationEvent](#class-tabsanimationevent))->Unit|是|-|切换动画开始时触发的回调。<br>参数：<br>index：当前显示元素的索引，索引从0开始。<br>targetIndex：切换动画目标元素的索引，索引从0开始。<br>event：动画相关信息，包括主轴方向上当前显示元素和目标元素相对Tabs起始位置的位移，以及离手速度。|

### func onChange((Int32) -> Unit)

```cangjie
public func onChange(callback: (index: Int32) -> Unit): This
```

**功能：** Tab页签切换后触发的事件。

满足以下任一条件，即可触发该事件：

1、滑动页面进行页面切换时，组件滑动动画结束后触发。<br>

2、通过[控制器](#class-tabscontroller)调用[changeIndex](#func-changeindexint32)接口，Tab页签切换后触发。<br>

3、动态修改[状态变量](../../../Dev_Guide/arkui-cj/state_management/cj-macro-state.md)构造的index属性值，Tab页签切换后触发。<br>

4、点击TabBar页签，Tab页签切换后触发。

> **说明：**
>
> 使用自定义页签时，在onChange事件中，联动可能会导致滑动页面切换后才执行页签联动，引起自定义页签切换效果延迟。建议在[onAnimationStart](#func-onanimationstartint32-int32-tabsanimationevent---unit)中监听并刷新当前索引，以确保动效能够及时触发。具体实现可参考[示例1](#示例1自定义页签切换联动)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Int32)->Unit|是|-|Tab页签切换事件回调。<br>参数：<br>当前显示的index索引，索引从0开始计算。|
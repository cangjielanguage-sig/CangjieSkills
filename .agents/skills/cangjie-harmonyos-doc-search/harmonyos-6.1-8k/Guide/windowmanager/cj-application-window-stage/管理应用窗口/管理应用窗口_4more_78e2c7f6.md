# 管理应用窗口

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

## 基本概念

- 窗口沉浸式能力：指对状态栏、导航栏等系统窗口进行控制，减少状态栏导航栏等系统界面的突兀感，从而使用户获得最佳体验的能力。
  沉浸式能力只在应用主窗口作为全屏窗口时生效。通常情况下，应用子窗口（弹窗、悬浮窗口等辅助窗口）和处于自由窗口下的应用主窗口无法使用沉浸式能力。

- 悬浮窗：全局悬浮窗口是一种特殊的应用窗口，具备在应用主窗口和对应Ability退至后台后仍然可以在前台显示的能力。
  悬浮窗口可以用于应用退至后台后，使用小窗继续播放视频，或者为特定的应用创建悬浮球等快速入口。应用在创建悬浮窗口前，需要申请对应的权限。

## 场景介绍

在`Stage`模型下，管理应用窗口的典型场景有：

- 设置应用主窗口属性及目标页面

- 设置应用子窗口属性及目标页面

- 体验窗口沉浸式能力

- 设置悬浮窗

- 监听窗口不可交互与可交互事件

以下分别介绍具体开发方式。

## 接口说明

上述场景涉及的常用接口如下表所示。更多API说明请参见[API参考](../reference/arkui-cj/cj-apis-window.md)。

| 实例名         | 接口名                                                       | 描述                                                         |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| WindowStage    | func getMainWindow(): Window | 获取`WindowStage`实例下的主窗口。<br/>此接口仅可在`Stage`模型下使用。 |
| WindowStage    | loadContent(path: String): Unit | 为当前`WindowStage`的主窗口加载具体页面。<br>其中path为要加载到窗口中的页面内容的路径。<br/>此接口仅可在`Stage`模型下使用。 |
| WindowStage    | createSubWindow(name: String): Window | 创建子窗口。<br/>此接口仅可在`Stage`模型下使用。             |
| window静态方法 | createWindow(config: Configuration): Window | 创建子窗口或者系统窗口。<br/>-`config`：创建窗口时的参数。             |
| Window         | setWindowBrightness(brightness: Float32): Unit | 设置屏幕亮度值。                                             |
| Window         | setWindowTouchable(isTouchable: Bool): Unit | 设置窗口是否为可触状态。true表示可触；false表示不可触。 |
| Window         | moveWindowTo(x: Int32, y: Int32): Unit | 移动当前窗口位置。                                           |
| Window         | resize(width: UInt32, height: UInt32): Unit | 改变当前窗口大小。                                           |
| Window         | setWindowLayoutFullScreen(isLayoutFullScreen: Bool): Unit | 设置主窗口或子窗口的布局是否为沉浸式布局。true表示沉浸式布局；false表示非沉浸式布局。|
| Window         | setWindowSystemBarEnabled(names: Array\<SystemBarType>): Unit | 设置主窗口状态栏、三键导航栏的可见模式，状态栏通过status控制、三键导航栏通过navigation控制。<br>例如，该参数设置为[SystemBarType.Status,&nbsp;SystemBarType.Navigation]，则全部显示；设置为[]，则不显示。|
| Window         | setWindowSystemBarProperties(systemBarProperties: SystemBarProperties): Unit | 设置窗口内导航栏、状态栏属性。<br/>`systemBarProperties`：导航栏、状态栏的属性集合。 |
| Window         | func showWindow(): Unit             | 显示当前窗口。                                               |
| Window         | func destroyWindow(): Unit     | 销毁当前窗口。                                               |
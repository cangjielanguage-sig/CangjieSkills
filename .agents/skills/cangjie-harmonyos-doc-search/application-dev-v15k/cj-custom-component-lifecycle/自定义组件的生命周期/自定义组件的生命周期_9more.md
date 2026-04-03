# 自定义组件的生命周期

自定义组件的生命周期回调函数用于通知用户该自定义组件的生命周期，这些回调函数是私有的，在运行时由开发框架在特定的时间进行调用，不能从应用程序中手动调用这些回调函数。不要在多个窗口复用同一个自定义组件节点，其生命周期可能会紊乱。

## 导入模块

```cangjie
import kit.UIKit.*
```

## func aboutToAppear()

```cangjie
protected open func aboutToAppear()
```

**功能：** aboutToAppear函数在创建自定义组件的新实例后，在执行其build()函数之前执行。允许在aboutToAppear函数中改变状态变量，更改将在后续执行build()函数中生效。实现自定义布局的自定义组件的aboutToAppear生命周期在布局过程中触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## func aboutToDisappear()

```cangjie
protected open func aboutToDisappear()
```

**功能：** aboutToDisappear函数在自定义组件析构销毁之前执行。不允许在aboutToDisappear函数中改变状态变量，特别是@Link变量的修改可能会导致应用程序行为不稳定。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## func aboutToReuse(ReuseParams)

```cangjie
protected open func aboutToReuse(params: ReuseParams)
```

**功能：** 当一个可复用的自定义组件从复用缓存中重新加入到节点树时，触发aboutToReuse生命周期回调，并将组件的构造参数传递给aboutToReuse。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 参数类型  | 描述 |
| :--- | :--- | :--- |
| params | ReuseParams | 自定义组件的构造参数。 |

## func onBackPress()

```cangjie
protected open func onBackPress(): Bool
```

**功能：** 当用户点击返回按钮时触发，仅@Entry装饰的自定义组件生效。返回true表示页面自己处理返回逻辑，不进行页面路由；返回false表示使用默认的路由返回逻辑。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## func onDidBuild()

```cangjie
protected open func onDidBuild()
```

**功能：** onDidBuild函数在执行自定义组件的build()函数之后执行，开发者可以在这个阶段进行埋点数据上报等不影响实际UI的功能。不建议在onDidBuild函数中更改状态变量、使用animateTo等功能，这可能会导致不稳定的UI表现。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## func onPageHide()

```cangjie
protected open func onPageHide()
```

**功能：** 页面每次隐藏时触发一次，包括路由过程、应用进入后台等场景，仅@Entry装饰的自定义组件生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## func onPageShow()

```cangjie
protected open func onPageShow()
```

**功能：** 页面每次显示时触发一次，包括路由过程、应用进入前台等场景，仅@Entry装饰的自定义组件生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12
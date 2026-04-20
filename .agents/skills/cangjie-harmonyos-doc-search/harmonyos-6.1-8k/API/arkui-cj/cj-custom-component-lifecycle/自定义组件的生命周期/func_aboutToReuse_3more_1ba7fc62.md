## func aboutToReuse(ReuseParams)

```cangjie
protected open func aboutToReuse(_: ReuseParams): Unit
```

**功能：** 当一个可复用的自定义组件从复用缓存中重新加入到节点树时，触发aboutToReuse生命周期回调，并将组件的构造参数传递给aboutToReuse。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[ReuseParams](./cj-common-types.md#class-reuseparams)|是|-|自定义组件的构造参数。|

## func aboutToRecycle()

```cangjie
protected open func aboutToRecycle(): Unit
```

**功能：** 组件的生命周期回调，在可复用组件从组件树上被加入到复用缓存之前调用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

## func pageTransition()

```cangjie
protected open func pageTransition(): Unit
```

**功能：** 进入此页面或移动到其他页面时实现动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22
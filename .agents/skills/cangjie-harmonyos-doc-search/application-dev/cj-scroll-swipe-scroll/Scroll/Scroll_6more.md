# Scroll

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。

> **说明：**
>
> - 该组件嵌套List子组件滚动时，若List不设置宽高，则默认全部加载，在对性能有要求的场景下建议指定List的宽高。
> - 该组件滚动的前提是主轴方向大小小于内容大小。
> - Scroll组件[通用属性clip](./cj-universal-attribute-shapclip.md#func-clipbool)的默认值为true。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

支持单个子组件。

## 创建组件

### init()

```cangjie
public init()
```

**功能：** 创建一个Scroll容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(() -> Unit)

```cangjie
public init(child: () -> Unit)
```

**功能：** 创建一个包含子组件的Scroll容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|child|() -> Unit|是|-|声明容器内的子组件。|

### init(?Scroller, () -> Unit)

```cangjie
public init(scroller: ?Scroller, child: () -> Unit)
```

**功能：** 创建一个包含子组件的Scroll容器，并绑定一个滚动条控制器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scroller|?[Scroller](./cj-scroll-swipe-scroll.md#class-scroller)|是|-|滚动条控制器。初始值：Scroller()。|
|child|() -> Unit|是|-|声明容器内的子组件。|

## 通用属性/通用事件

通用属性：除了支持通用属性外，还支持[滚动组件通用属性](./cj-scroll-swipe-common.md#组件属性)。

通用事件：除了支持通用事件外，还支持[滚动组件通用事件](./cj-scroll-swipe-common.md#组件事件)。

> **说明：**
>
> 不支持滚动组件通用事件中的[onWillScroll](./cj-scroll-swipe-common.md#func-onwillscrolloptionfloat64scrollstatescrollsource---unit)、[onDidScroll](./cj-scroll-swipe-common.md#func-ondidscrollonscrollcallback)事件。

## 组件属性

### func scrollable(?ScrollDirection)

```cangjie
public func scrollable(scrollDirection: ?ScrollDirection): This
```

**功能：** 设置滚动方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scrollDirection|?[ScrollDirection](./cj-common-types.md#enum-scrolldirection)|是|-|滚动方向。初始值：ScrollDirection.Vertical。|
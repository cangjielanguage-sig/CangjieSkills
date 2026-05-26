# Scroll

可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。

> **说明：**
>
> - 该组件嵌套List子组件滚动时，若List不设置宽高，则默认全部加载，在对性能有要求的场景下建议指定List的宽高。
> - 该组件滚动的前提是主轴方向大小小于内容大小。
> - Scroll组件[通用属性clip](./cj-universal-attribute-shapclip.md#func-clipbool)的默认值为true。

## 子组件

支持单个子组件。

## 创建组件

### init()

```cangjie
public init()
```

**功能：** 创建一个Scroll容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(() -> Unit)

```cangjie
public init(child: () -> Unit)
```

**功能：** 创建一个包含子组件的Scroll容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|child|()->Unit|是|-|声明容器内的子组件。|

### init(Scroller, () -> Unit)

```cangjie
public init(scroller: Scroller, child: () -> Unit)
```

**功能：** 创建一个包含子组件的Scroll容器，并绑定一个滚动条控制器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scroller|[Scroller](#class-scroller)|是|-|滚动条控制器。|
|child|()->Unit|是|-|声明容器内的子组件。|

## 通用属性/通用事件

通用属性：支持通用属性和[滚动组件通用属性](./cj-scroll-swipe-common.md)。

通用事件：支持通用事件和[滚动组件通用事件](./cj-scroll-swipe-common.md)。

> **说明：**
>
> 不支持滚动组件通用事件中的[onWillScroll](./cj-scroll-swipe-common.md#func-onwillscrollfloat64scrollstatescrollsource---float64)、[onDidScroll](./cj-scroll-swipe-common.md#func-ondidscrollfloat64-scrollstate---unit)事件。
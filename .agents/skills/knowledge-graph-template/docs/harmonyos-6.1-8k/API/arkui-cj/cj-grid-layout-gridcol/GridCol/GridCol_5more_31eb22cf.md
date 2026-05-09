# GridCol

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

栅格子组件，必须作为栅格容器组件([GridRow](./cj-grid-layout-gridrow.md))的子组件使用。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

可以包含单个子组件。

## 创建组件

### init(?Int32, ?Int32, ?Int32, () -> Unit)

```cangjie
public init(span!: ?Int32 = None, offset!: ?Int32 = None, order!: ?Int32 = None, child!: () -> Unit = {=>})
```

**功能：** 创建一个栅格布局子组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|span|?Int32|否|None| **命名参数。** 栅格子组件占用栅格容器组件([GridRow](./cj-grid-layout-gridrow.md))的列数。<br>span为0表示该元素不参与布局计算，即不会被渲染。<br>初始值：1。|
|offset|?Int32|否|None| **命名参数。** 栅格子组件相对于前一个栅格子组件偏移的列数。<br>初始值：0。|
|order|?Int32|否|None| **命名参数。** 元素的序号，根据栅格子组件的序号，从小到大对栅格子组件做排序。<br>初始值：0。|
|child|() -> Unit|否|{=>}| **命名参数。** GridCol容器的子组件。|

### init(?GridColOptions, ?GridColOptions, ?GridColOptions, () -> Unit)

```cangjie
public init(
    span!: ?GridColOptions,
    offset!: ?GridColOptions,
    order!: ?GridColOptions,
    child!: () -> Unit = {=>}
)
```

**功能：** 创建栅格子组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|span|?[GridColOptions](#class-gridcoloptions)|是|-| **命名参数。** 占用列数。<br>初始值：GridColOptions(1)|
|offset|?[GridColOptions](#class-gridcoloptions)|是|-| **命名参数。** 相对于前一个栅格子组件偏移的列数。<br>初始值：GridColOptions(0)|
|order|?[GridColOptions](#class-gridcoloptions)|是|-| **命名参数。** 元素的序号，根据栅格子组件的序号，从小到大对栅格子组件做排序。<br>初始值：GridColOptions(0)|
|child|() -> Unit|否|{=>}| **命名参数。** GridCol 容器的子组件。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。
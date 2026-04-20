# GridItem

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

网格容器中单项内容容器。

> **说明：**
>
> - 仅支持作为[Grid](./cj-scroll-swipe-grid.md)组件的子组件使用。
> - 当GridItem配合[LazyForEach](cj-state-rendering-lazyforeach.md)使用时，GridItem子组件在GridItem创建时创建。配合[if/else](../../arkui-cj/rendering_control/cj-rendering-control-ifelse.md)、[ForEach](../../arkui-cj/rendering_control/cj-rendering-control-foreach.md)使用时，或父组件为Grid时，GridItem子组件在GridItem布局时创建。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

可以包含单个子组件。

## 创建组件

### init()

```cangjie
public init()
```

**功能：** 创建网格容器中单项内容组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(() -> Unit)

```cangjie
public init(child: () -> Unit)
```

**功能：** 创建一个可包含子组件的网格容器单项内容组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|child|() -> Unit|是|-|GridItem 容器的子组件。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。

## 组件属性

### func columnEnd(?Int32)

```cangjie
public func columnEnd(value: ?Int32): This
```

**功能：** 设置当前元素终点列号。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Int32|是|-|当前元素终点列号，与columnStart配套使用。|

### func columnStart(?Int32)

```cangjie
public func columnStart(value: ?Int32): This
```

**功能：** 设置当前元素起始列号。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Int32|是|-|当前元素起始列号，与columnEnd配套使用。|

### func rowEnd(?Int32)

```cangjie
public func rowEnd(value: ?Int32): This
```

**功能：** 设置当前元素终点行号。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Int32|是|-|当前元素终点行号，与rowStart配套使用。|

### func rowStart(?Int32)

```cangjie
public func rowStart(value: ?Int32): This
```

**功能：** 设置当前元素起始行号。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Int32|是|-|当前元素起始行号，与rowEnd配套使用。|
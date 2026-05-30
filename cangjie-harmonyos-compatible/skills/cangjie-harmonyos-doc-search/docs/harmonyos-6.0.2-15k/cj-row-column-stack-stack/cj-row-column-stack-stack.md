# Stack

堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

## 子组件

可以包含子组件。

## 创建组件

### Stack(() -> Unit)

```cangjie
public Stack(child: () -> Unit)
```

**功能：** 创建一个包含子组件的Stack容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|child|()->Unit|是|-|声明容器内的子组件。|

### init()

```cangjie
public init()
```

**功能：** 创建一个Stack容器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(Alignment)

```cangjie
public init(alignContent: Alignment)
```

**功能：** 创建一个Stack容器，子组件对齐方式是alignContent。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|alignContent|[Alignment](cj-common-types.md#enum-alignment)|是|-|设置子组件在容器内的对齐方式。 <br> 初始值：Alignment.Center|

### init(Alignment, () -> Unit)

```cangjie
public init(alignContent: Alignment, child: () -> Unit)
```

**功能：** 创建一个包含子组件的Stack容器，子组件对齐方式是alignContent。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|alignContent|[Alignment](cj-common-types.md#enum-alignment)|是|-|设置子组件在容器内的对齐方式。<br> 初始值：Alignment.Center|
|child|()->Unit|是|-|声明容器内的子组件。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。

## 组件属性

### func alignContent(Alignment)

```cangjie
public func alignContent(value: Alignment): This
```

**功能：** 设置所有子组件在容器内的对齐方式。该属性与[通用属性align](cj-universal-attribute-location.md#func-alignalignment)同时设置时，后设置的属性生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Alignment](cj-common-types.md#enum-alignment)|是|-|所有子组件在容器内的对齐方式。 <br> 初始值：Alignment.Center|

### func alignment(Alignment)<sup>(deprecated)</sup>

```cangjie
public func alignment(value: Alignment): This
```

**功能：** 设置所有子组件在容器内的对齐方式。已废弃，使用alignContent代替。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Alignment](cj-common-types.md#enum-alignment)|是|-|子组件在容器内的对齐方式。|

## 示例代码

Stack的alignContent设置为Alignment.Bottom条件下子组件显示效果。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Stack(Alignment.Bottom) {
            Text("First child, show in bottom").width(90.percent).height(100.percent).backgroundColor(0xd2cab3).align(
                Alignment.Top)
            Text("Second child, show in top").width(70.percent).height(60.percent).backgroundColor(0xc1cbac).align(
                Alignment.Top)
        }.width(100.percent).height(150).margin(top: 5)
    }
}
```

![stack](figures/stack.png)

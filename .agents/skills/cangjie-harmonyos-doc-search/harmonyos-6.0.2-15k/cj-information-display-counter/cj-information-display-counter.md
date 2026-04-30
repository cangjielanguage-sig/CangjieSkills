# Counter

计数器组件，提供相应的增加或者减少的计数操作。

## 子组件

可以包含子组件。

## 创建组件

### init(() -> Unit)

```cangjie
public init(content: () -> Unit)
```

**功能：** 创建计数器组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|()->Unit|是|-|定义计数器组件和内容区。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。

## 组件属性

### func enableDec(Bool)

```cangjie
public func enableDec(value: Bool): This
```

**功能：** 设置减少按钮禁用或使能。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|减少按钮禁用或使能。<br>true表示按钮使能。<br>false表示按钮禁用。<br>初始值：true。|

### func enableInc(Bool)

```cangjie
public func enableInc(value: Bool): This
```

**功能：** 设置增加按钮禁用或使能。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|增加按钮禁用或使能。<br>true表示+按钮使能。<br>false表示+按钮禁用。<br>组件初始值：true。|

## 组件事件

### func onDec(() -> Unit)

```cangjie
public func onDec(callback: () -> Unit): This
```

**功能：** 监听数值减少时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，Counter数值减少时触发。|

### func onInc(() -> Unit)

```cangjie
public func onInc(callback: () -> Unit): This
```

**功能：** 监听数值增加触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，Counter数值增加时触发。|

## 示例代码

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var value: Int64 = 0
    func build() {
        Column {
            Counter() {Text(this.value.toString())}.margin(100.0).height(10.percent).onInc {
                this.value++
            }.onDec {
                this.value--
            }
        }
    }
}
```

![counter](figures/counter.gif)

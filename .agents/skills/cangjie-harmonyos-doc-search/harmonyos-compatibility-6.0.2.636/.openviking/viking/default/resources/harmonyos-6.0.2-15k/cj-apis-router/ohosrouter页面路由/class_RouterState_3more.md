## class RouterState

```cangjie
public class RouterState {
    public RouterState(
        public var index!: Int32,
        public var name!: String,
        public var path!: String,
        public var params!: String
    )
}
```

**功能：** 页面状态信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var index

```cangjie
public var index: Int32
```

**功能：** 表示当前页面在页面栈中的索引。从栈底到栈顶，index从1开始递增。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var name

```cangjie
public var name: String
```

**功能：** 表示当前页面的名称，即对应文件名。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var params

```cangjie
public var params: String
```

**功能：** 表示当前页面携带的参数。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var path

```cangjie
public var path: String
```

**功能：** 表示当前页面的路径。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### RouterState(Int32, String, String, String)

```cangjie
public RouterState(
    public var index!: Int32,
    public var name!: String,
    public var path!: String,
    public var params!: String
)
```

**功能：** 构造一个RouterState类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-| **命名参数。** 表示当前页面在页面栈中的索引。从栈底到栈顶，index从1开始递增。|
|name|String|是|-| **命名参数。** 表示当前页面的名称，即对应文件名。|
|path|String|是|-| **命名参数。** 表示当前页面的路径。|
|params|String|是|-| **命名参数。** 表示当前页面携带的参数。|

## enum RouterMode

```cangjie
public enum RouterMode {
    | Standard
    | Single
}
```

**功能：** 路由跳转模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Single

```cangjie
Single
```

**功能：** 单实例模式。如果目标页面的url已经存在于页面栈中，则该url页面移动到栈顶。如果目标页面的url在页面栈中不存在同url页面，则按照默认的多实例模式进行跳转。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Standard

```cangjie
Standard
```

**功能：** 多实例模式，也是默认情况下的跳转模式。目标页面会被添加到页面栈顶，无论栈中是否存在相同url的页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## 示例代码

### 示例1（页面跳转）

该示例实现了页面间的跳转。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import kit.LocalizationKit.*

@Entry
@Component
class EntryView {
    @State
    var active: Bool = false
    func build() {
        Column() {
            Image(@r(app.media.startIcon)).width(50).height(50).onClick {
                e => Router.push(url: "Page1")
            }.sharedTransition("sharedImage",
                options: SharedTransitionOptions(duration: 800, curve: Curve.Linear, delay: 100))
        }
    }
}
```

<!-- run -->

```cangjie
// page1.cj
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class Page1 {
    func build() {
        Column() {
            Text("This is Page1")
            Button("back()").onClick({
                evt => Router.back()
            })
        }
    }
}
```
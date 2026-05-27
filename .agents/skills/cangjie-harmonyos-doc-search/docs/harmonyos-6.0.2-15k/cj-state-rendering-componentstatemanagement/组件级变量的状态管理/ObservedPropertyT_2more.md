## ObservedProperty\<T>

### class ObservedProperty

```cangjie
public open class ObservedProperty<T> <: ObservedPropertyAbstract {
    public init(info: String, initValue: T)
}
```

**功能：** 用于封装和管理一个可观察的属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- ObservedPropertyAbstract

#### init(String, T)

```cangjie
public init(info: String, initValue: T)
```

**功能：** ObservedProperty类的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|info|String|是|-|构造初始化信息。|
|initValue|T|是|-|构造初始化值。|

#### func get()

```cangjie
public func get(): T
```

**功能：** 读取同步属性的数据。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|T|同步属性的数据。|

**示例：**

```cangjie
AppStorage.setOrCreate<Int64>("propA", 47)
let prop1: ObservedProperty<Int64> = AppStorage.`prop`<Int64>("propA")
prop1.get() // 47
```

#### func set(T)

```cangjie
public open func set(newValue: T): Unit
```

**功能：** 设置同步属性的数据。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|newValue|T|是|-|要设置的数据。|

**示例：**

```cangjie
AppStorage.setOrCreate<Int64>("propA", 47)
let prop1: ObservedProperty<Int64> = AppStorage.`prop`<Int64>("propA")
prop1.set(1); //  prop1.get()=1
```

## 示例代码

状态更新时的注意事项：不允许在spawn表达式中对状态变量进行并发修改，会导致并发安全问题。建议当需要修改状态变量时，采用`concurrency`包提供的`launch`方法，将状态更新的步骤放回主线程中运行，以保证并发安全。如下实例演示如何在spawn表达式中更新变量状态：

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var text: String = "begin"

    func build() {
        Column(30) {
            Button(text).onClick {
                evt => changeText({
                    p: String =>
                    // 使用launch表达式在主线程中更新状态变量
                    launch {
                        text = p
                    }
                })
            }
        }.width(100.percent)
    }

    private func changeText(callback: (String) -> Unit): Unit {
        spawn {
            while (true) {
                callback("blink 0")
                sleep(Duration.millisecond * 100)
                callback("blink 1")
                sleep(Duration.millisecond * 100)
            }
        }
    }
}
```
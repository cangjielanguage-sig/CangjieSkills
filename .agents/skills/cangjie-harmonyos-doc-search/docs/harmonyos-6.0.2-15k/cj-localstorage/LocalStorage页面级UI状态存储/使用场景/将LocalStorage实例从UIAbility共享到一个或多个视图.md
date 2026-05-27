### 将LocalStorage实例从UIAbility共享到一个或多个视图

上面的实例中，LocalStorage的实例仅仅在一个@Entry装饰的组件和其所属的子组件（一个页面）中共享，如果希望其在多个视图中共享，可以在所属UIAbility中创建LocalStorage实例。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

internal import ohos.base.AppLog
internal import ohos.ability.AbilityStage
internal import ohos.ability.LaunchReason
import kit.UIKit.*

let storage = LocalStorage()
let temp = storage.setOrCreate("PropA", 47)

class MainAbility <: UIAbility {
    public init() {
        super()
        registerSelf()
    }

    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("MainAbility OnCreated.${want.abilityName}")
        match (launchParam.launchReason) {
            case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
            case _ => ()
        }
    }

    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        AppLog.info("MainAbility onWindowStageCreate.")
        windowStage.loadContent("EntryView")
    }
}
```

> **说明：**
>
> 在UI页面通过storage接口获取共享的LocalStorage实例。

在下面的用例中，EntryView页面中的propA通过storage获取到共享的LocalStorage实例。单击Button跳转到Page页面，单击Change propA改变propA的值，back回EntryView页面后，页面中propA的值也同步修改。

<!-- run -->

```cangjie
// index.cj

package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

//通过storage获取共享的LocalStorage实例
@Entry[storage]
@Component
class EntryView {
    @LocalStorageLink["PropA"]
    var propA: Int64 = 1
    func build() {
        Row() {
            Column() {
                Text("${this.propA}").fontSize(50).fontWeight(FontWeight.Bold)
                Button("To page").onClick({evt => Router.push(url: "Page");})
            }.width(100.percent)
        }.height(100.percent)
    }
}
```

<!-- run -->

```cangjie
//page.cj

package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

//通过storage获取共享的LocalStorage实例
@Entry[storage]
@Component
class Page {
    @LocalStorageLink["PropA"]
    var propA: Int64 = 2
    func build() {
        Row() {
            Column() {
                Text("${this.propA}").fontSize(50).fontWeight(FontWeight.Bold)
                Button("Change propA").onClick({evt => this.propA = 100})
                Button("Back EntryView").onClick({evt => Router.push(url: "EntryView");})
            }
        }
    }
}
```

> **说明：**
>
> 对于开发者更建议使用这个方式来构建LocalStorage的实例，并且在创建LocalStorage实例的时候就写入默认值，因为默认值可以作为运行异常的备份，也可以用作页面的单元测试。
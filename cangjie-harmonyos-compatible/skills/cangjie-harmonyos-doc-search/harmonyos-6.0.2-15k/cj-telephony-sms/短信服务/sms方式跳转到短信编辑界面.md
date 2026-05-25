## sms方式跳转到短信编辑界面

### 使用场景

通过sms短信协议，可以创建指向短信收件人的超链接，方便用户通过网页或应用中的超链接直接跳转到短信应用。同时，支持在`sms:`的相关字段中定义短信的收件人、发送内容等，节省用户编辑短信的时间。

### sms协议格式

sms协议标准格式如下：

```text
sms:106XXXXXXXXXX?body=发送短信内容
```

- `sms:`：sms scheme，必填。
- `106XXXXXXXXXX`：收件人号码，选填。如果存在多个地址，用英文逗号分隔。
- `?`：短信内容声明开始符号。如果带短信内容参数，则必填。
- `body-value`：发送内容参数，选填。

### 拉起方开发步骤

#### 从网页拉起

网页中的超链接需要满足sms协议。示例如下：

```html
<a href="sms:106XXXXXXXXXX?body=%E5%8F%91%E9%80%81%E7%9F%AD%E4%BF%A1%E5%86%85%E5%AE%B9">发送短信</a>
```

实际开发时，需要将收件人号码替换为真实的号码，短信内容可以根据需要进行配置。

#### 从应用拉起

保证sms字符串传入uri参数即可，可通过MainAbility获取AbilityContext。

```cangjie
// index.cj
import ohos.component.*
import ohos.state_manage.*
import ohos.state_macro_manage.*
import kit.AbilityKit.*
import ohos.base.*

var ctx = None<UIAbilityContext>

@Entry
@Component
class EntryView {
    func build() {
        Column() {
            Button('发送短信').onClick {
                evt =>
                let exampleUrl = "sms:106XXXXXXXXXX?body=%E5%8F%91%E9%80%81%E7%9F%AD%E4%BF%A1%E5%86%85%E5%AE%B9"

                let want = Want(
                    bundleName: 'com.ohos.mms',
                    action: 'ohos.want.action.viewData',
                    uri: exampleUrl
                )
                ctx.getOrThrow().startAbility(want)
            }
        }
    }
}
```

```cangjie
// main_ability.cj
import kit.AbilityKit.{LaunchReason, LaunchParam, Want, UIAbility}
import kit.ArkUI.WindowStage
import kit.UIKit.AppLog

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
        // declared in index.cj
        ctx = this.context
    }
}
```
# 强密码填充

密码保险箱可以在用户需要输入一个新密码时，自动生成一个高强度的密码。用户选择使用生成的强密码时可以将这个密码填充到新密码输入框。

**触发条件及注意事项：**

- **已设置锁屏密码**并且开启密码保险箱自动保存和填入账号和密码开关。
- 界面中必须同时存在type为InputType.USER_NAME（表示用户名输入框）和InputType.NEW_PASSWORD（表示新密码输入框）的TextInput输入框组件。具体类型请参见[输入框类型说明](./cj-quick-match.md#约束与限制)。
- TextInput组件的enableAutoFill属性的值为true（默认true）。
- 用户在界面中首次点击新密码输入框时触发强密码弹窗，用户点击使用密码按钮可以将弹窗中显示的强密码自动填充到新密码输入框。
- 开发者可以根据[一定的规则和建议](./cj-add-strong-password-suggestions.md)指定强密码生成规则。

## 注册

![autofill register](./figures/autofill-register.png)

示例代码如下：

```cangjie
import ohos.component.*
import ohos.state_macro_manage.*
import ohos.state_manage.*

@Builder
func pageMap(name: String) {
    if (name == "register_result_page") {
        RegisterResultPage()
    }
}

@Entry
@Component
class RegisterExample {
    var pathInfos: NavPathStack = NavPathStack()
    @State
    var ReserveAccount: String = ""
    @State
    var ReservePassword: String = ""
    @State
    var enAbleAutoFill: Bool = true

    public func onBackPress() {
        // 当非成功登录、返回等页面跳转时，将enAbleAutoFill设置为false，密码保险箱将不启用自动填充功能
        this.enAbleAutoFill = false
        return false
    }

    public func build() {
        Navigation(this.pathInfos) {
            Column() {
                Text("注册账号").fontSize(24).fontColor(0x000000).fontWeight(FontWeight.Medium).margin(top: 24,
                    bottom: 16)

                TextInput(placeholder: "用户名").placeholderColor(0x182431).width(100.percent).opacity(0.6).
                    placeholderFont(size: 16, weight: FontWeight.Regular).margin(top: 16).setType(InputType.USER_NAME) // 账号框使用USER_NAME属性
                        .
                    onChange({
                    value => this.ReserveAccount = value
                })

                TextInput(placeholder: "新密码").showPasswordIcon(true).placeholderColor(0x182431).width(100.percent).
                    opacity(0.6).placeholderFont(size: 16, weight: FontWeight.Regular).margin(top: 16).setType(
                    InputType.NEW_PASSWORD) // 密码框使用 new Password 属性,可以触发生成强密码
                        .enableAutoFill(this.enAbleAutoFill).passwordRules(
                    'begin:[upper],special:[yes],len:[maxlen:32,minlen:12]').onChange(
                    {
                    value => this.ReservePassword = value
                })

                Button("页面跳转").width(100.percent).height(40).borderRadius(20).margin(top: 24).enabled(
                    (this.ReserveAccount != "") && (this.ReservePassword != "")).onClick(
                    {
                    => this.pathInfos.pushPath(NavPathInfo("register_result_page", "register_result_page test"))
                })

                Button('页面跳转(跳转前关闭autofill)').width(100.percent).height(40).borderRadius(20).margin(top: 24).
                    enabled((this.ReserveAccount != "") && (this.ReservePassword != "")).onClick(
                    {
                        =>
                        this.enAbleAutoFill = false
                        this.pathInfos.pushPath(NavPathInfo("register_result_page", "register_result_page test"))
                    }
                )
            }
        }.navDestination(bind<String>(pageMap, this)).height(100.percent).width(100.percent)
    }
}

@Component
class RegisterResultPage {
    var pathInfos: NavPathStack = NavPathStack()

    public func build() {
        NavDestination() {
            Column() {
                Text("Result Page").fontSize(24).fontColor(0x000000).fontWeight(FontWeight.Medium).margin(top: 24,
                    bottom: 16)
            }.width(100.percent).height(100.percent)
        }.onReady({
            context => this.pathInfos = context.pathStack
        })
    }
}
```
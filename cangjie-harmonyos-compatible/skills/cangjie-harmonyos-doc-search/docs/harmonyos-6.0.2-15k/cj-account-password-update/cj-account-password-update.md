# 账号密码更新

应用界面触发账号密码自动保存时，若密码保险箱中已存在同应用下与本次使用账号相同的账号，则弹出密码更新提示框，用户点击更新按钮，即可更新密码保险箱内对应账号的密码。

![update account password](./figures/update-account-password.png)

应用触发修改密码或使用已经保存过的账号手动登录时，均会触发密码更新功能。

登录的布局介绍请参见[账号密码登录](./cj-save-account-passwords.md#账号密码登录)，以下仅介绍修改账号密码的标准适配场景。

**触发条件及注意事项同[账号密码保存](./cj-save-account-passwords.md)功能。**

## 修改账号密码

![change account password](./figures/change-account-password.png)

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
                Text("修改密码").fontSize(24).fontColor(0x000000).fontWeight(FontWeight.Medium).margin(top: 24,
                    bottom: 16)

                TextInput(placeholder: "用户名").placeholderColor(0x182431).width(100.percent).opacity(0.6).
                    placeholderFont(size: 16, weight: FontWeight.Regular).margin(top: 16).setType(InputType.USER_NAME) // 账号框使用USER_NAME属性
                        .
                    onChange({
                    value => this.ReserveAccount = value
                })

                TextInput(placeholder: "密码").showPasswordIcon(true).placeholderColor(0x182431).width(100.percent).
                    opacity(0.6).placeholderFont(size: 16, weight: FontWeight.Regular).margin(top: 16).setType(
                    InputType.Password).onChange({
                    value => this.ReservePassword = value
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

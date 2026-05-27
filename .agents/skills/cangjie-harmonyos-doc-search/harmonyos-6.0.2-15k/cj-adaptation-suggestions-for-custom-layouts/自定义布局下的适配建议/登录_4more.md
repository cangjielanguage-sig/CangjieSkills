## 登录

应用在设置“登录”页面时，需要“用户名/账号名”、“密码”在同一个界面，具体详情请参见[账号密码保存-登录](./cj-save-account-passwords.md#账号密码登录)、[账号密码填充-登录](./cj-account-password-autofill.md#登录)。

## 注册

应用在设置“注册”页面时，需要“用户名/账号名”、“新密码”在同一个界面，具体详情请参见[账号密码保存-注册](./cj-save-account-passwords.md#账号密码注册)、[强密码填充-注册](./cj-strong-password-autofill.md#注册)。

## 修改密码

应用在设置“修改密码”页面时，需要“用户名/账号名”、“旧密码”、“新密码”在同一个界面，具体详情请参见[账号密码更新-修改账号密码](./cj-account-password-update.md#修改账号密码)、[账号密码填充-修改密码](./cj-account-password-autofill.md#修改密码)。

## 登录、注册失败

当应用成功登录或注册后，应将账号密码保存至密码保险箱。若登录或注册未成功，通过页面路由（router）跳转返回时，建议应用将enableAutofill属性设置为false，以避免保存错误信息。

示例代码如下：

```cangjie
import ohos.base.*
import ohos.component.*
import ohos.state_manage.*
import ohos.state_macro_manage.*

extend Text {
    func commonTitleStyles() {
        this.fontSize(24).fontColor(0x000000).fontWeight(FontWeight.Medium).margin(top: 18)
    }
}

extend TextInput {
    func commonInputStyles() {
        this.placeholderColor(0x182431).width(100.percent).opacity(0.6).placeholderFont(size: 16,
            weight: FontWeight.Regular)
    }
}

@Entry
@Component
class LoginExample {
    var pathInfos: NavPathStack = NavPathStack()
    @State
    var ReserveAccount: String = ""
    @State
    var ReservePassword: String = ""
    // 保存填充功能初始值：true
    @State
    var enAbleAutoFill: Bool = true

    public func onBackPress() {
        // 当非成功登录、返回等页面跳转时，将enAbleAutoFill设置为false，密码保险箱将不启用自动填充功能
        this.enAbleAutoFill = false
        return false
    }

    @Builder
    func pageMap(name: String) {
        if (name == "home_page") {
            HomePage()
        }
    }

    public func build() {
        Navigation(this.pathInfos) {
            Column(16) {
                Text("账户登录").commonTitleStyles()

                TextInput(placeholder: "账号").commonInputStyles().setType(InputType.USER_NAME) // 账号框使用USER_NAME属性
                    .enableAutoFill(
                    this.enAbleAutoFill) // 保存填充功能属性
                        .onChange({
                    value => this.ReserveAccount = value
                })

                TextInput(placeholder: "密码").commonInputStyles().showPasswordIcon(true).setType(InputType.Password) // 密码框使用Password属性
                    .
                    enableAutoFill(this.enAbleAutoFill) // 保存填充功能属性
                        .onChange({
                    value => this.ReservePassword = value
                })

                Button('登录', ButtonOptions(shape: ButtonType.Capsule, stateEffect: false)).borderRadius(20).width(
                    100.percent).enabled((this.ReserveAccount != '') && (this.ReservePassword != '')).onClick(
                    {
                        => // 成功登录时页面跳转将enAbleAutoFill设置为true，密码保险箱使能
                        this.enAbleAutoFill = true
                        this.pathInfos.pushPath(NavPathInfo('home_page', ''))
                    }
                )
            }.padding(16)
        }.navDestination(bind<String>(pageMap, this)).height(100.percent).width(100.percent)
    }
}

@Component
class HomePage {
    var pathInfos: NavPathStack = NavPathStack()

    public func build() {
        NavDestination() {
            Column() {
                Text("Home Page").commonTitleStyles()
            }.width(100.percent).height(100.percent)
        }.onReady {
            context => this.pathInfos = context.pathStack
        }
    }
}
```
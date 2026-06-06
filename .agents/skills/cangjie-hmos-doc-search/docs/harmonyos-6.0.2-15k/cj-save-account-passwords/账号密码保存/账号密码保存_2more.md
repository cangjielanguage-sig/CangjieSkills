# 账号密码保存

密码保险箱在应用的登录、注册、修改密码等场景中具备自动保存用户名和密码的能力。

保存后的用户名和密码可以在下次登录、修改密码时自动填充到界面上的对应输入框，用户可以在密码保险箱内对已保存的用户名和密码进行查看、修改、添加备注、删除。

当应用界面触发账号密码自动保存时，若密码保险箱中不存在同应用下的相同账号，系统将弹出账号密码保存提示框，用户点击“保存密码”按钮后，本次使用的账号和密码将被保存至密码保险箱。

![save account password](./figures/save-account-password.png)

当应用触发账号登录或注册时，均可触发保存功能，以下分别介绍两种布局的标准适配场景。

**触发条件及注意事项：**

1. **已设置锁屏密码**，并且开启密码保险箱中“自动保存及填入账号和密码”的开关。
2. 界面中TextInput输入框组件的enableAutoFill属性的值应为true（默认为true）。
3. 密码保险箱的自动保存功能只适用用户名和密码保存场景，在界面中必须同时存在用户名和密码的TextInput输入框组件。具体类型请参见[输入框类型说明](./cj-quick-match.md#约束与限制)。

    用户名输入框应设置type属性为InputType.USER_NAME。

    密码输入框应设置type属性为InputType.Password或InputType.NEW_PASSWORD。

    其中，InputType.Password表示普通密码输入框，适用于登录界面的密码和修改密码界面的旧密码，InputType.NEW_PASSWORD表示新密码输入框，适用于注册界面和修改密码界面的新密码。

4. 用户名和密码输入框中需要输入内容，不能为空也不能超长。用户名长度不能超过128字符，密码长度不能超过256字符。
5. 页面跳转时触发保存功能。
6. 在只有type为InputType.USER_NAME和InputType.Password的两个TextInput组件时，如果使用[账号密码填充-修改密码](./cj-account-password-autofill.md#修改密码)自动填充了用户名和密码并没有修改，则不会触发保存和更新功能。

## 账号密码登录

![account sign in](./figures/account-sign-in.png)

示例代码如下：

```cangjie
import ohos.component.*
import ohos.state_macro_manage.*
import ohos.state_manage.*

@Builder
func pageMap(name: String) {
    if (name == "home_page") {
        HomePage()
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

    public func build() {
        Navigation(this.pathInfos) {
            Column(16) {
                Text("账户登录").fontSize(24).fontColor(0x000000).fontWeight(FontWeight.Medium).margin(top: 24,
                    bottom: 16)

                TextInput(placeholder: "用户名").placeholderColor(0x182431).width(100.percent).opacity(0.6).
                    placeholderFont(size: 16, weight: FontWeight.Regular).margin(top: 16).setType(InputType.USER_NAME) // 账号框使用USER_NAME属性
                        .
                    onChange({
                    value => this.ReserveAccount = value
                })

                TextInput(placeholder: "密码").showPasswordIcon(true).placeholderColor(0x182431).width(100.percent).
                    opacity(0.6).placeholderFont(size: 16, weight: FontWeight.Regular).margin(top: 16).setType(
                    InputType.Password) // 密码框使用Password属性
                        .onChange({
                    value => this.ReservePassword = value
                })

                Button('登录').width(100.percent).enabled((this.ReserveAccount != '') && (this.ReservePassword != '')).
                    onClick({
                    => this.pathInfos.pushPath(NavPathInfo("home_page", "home_page_test"))
                })
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
                Text("Home Page").fontSize(24).fontColor(0x000000).fontWeight(FontWeight.Medium).margin(top: 24,
                    bottom: 16)
            }.width(100.percent).height(100.percent)
        }.onReady {
            context => this.pathInfos = context.pathStack
        }
    }
}
```
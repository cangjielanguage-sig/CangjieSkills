# 账号密码填充

密码保险箱可以在登录或修改密码时，自动填充已保存的用户名和密码。

**触发条件及注意事项：**

- **已设置锁屏密码**并且开启密码保险箱自动保存和填入账号和密码开关。
- 界面中必须同时存在type为InputType.USER_NAME（表示用户名输入框）和InputType.Password（表示普通密码输入框）的TextInput输入框组件。

    具体类型请参见[输入框类型说明](./cj-quick-match.md#约束与限制)。

- TextInput组件的enableAutoFill属性的值为true（默认true）。
- 密码保险箱中已保存过当前应用的用户名和密码。
- 用户在界面中首次点击用户名输入框或密码输入框时触发自动填充弹窗。

## 登录

![autofill login](./figures/autofill-login.png)

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
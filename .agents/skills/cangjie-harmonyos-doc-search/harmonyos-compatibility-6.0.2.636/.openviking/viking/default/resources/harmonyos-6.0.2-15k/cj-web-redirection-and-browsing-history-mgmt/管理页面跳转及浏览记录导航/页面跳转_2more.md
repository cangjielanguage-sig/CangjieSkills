## 页面跳转

当点击网页中的链接需要跳转到应用内其他页面时，可以通过使用Web组件的[onLoadIntercept()](../../API_Reference/source_zh_cn/arkui-cj/cj-web-web.md#func-onloadinterceptwebresourcerequest---bool)接口来实现。

在下面的示例中，应用首页index.cj加载前端页面route.html，在前端route.html页面点击超链接，可跳转到应用的profile_page.cj页面。

- 应用首页index.cj页面代码：

    ```cangjie
    // index.cj
    import ohos.state_macro_manage.*
    import kit.LocalizationKit.{__GenerateResource__}
    import kit.ArkWeb.WebviewController
    import kit.UIKit.{Web, BusinessException, Router}

    @Entry
    @Component
    class EntryView {
        let webController = WebviewController()

        func build() {
            Column {
                Web(src: @rawfile("route.html"), controller: this.webController).onLoadIntercept {
                    event =>
                    let urlStr: String = event.getRequestUrl()
                    if (urlStr.indexOf('native://') == 0) {
                        // 跳转其他界面
                        Router.pushUrl(url: urlStr[9..]) {
                            value => match (value) {
                                case Some(v) => AppLog.info("pushUrl callback value: ${v}")
                                case _ => return
                            }
                        }
                        return true
                    }
                    return false
                }
            }
        }
    }
    ```

- route.html前端页面代码：

    ```html
    <!-- resource/rawfile/route.html -->
    <!DOCTYPE html>
    <html>
    <body>
        <div>
            <a href="native://ProfilePage">个人中心</a>
        </div>
    </body>
    </html>
    ```

- 跳转页面profile_page.cj代码：

    ```cangjie
    import ohos.state_macro_manage.*

    @Entry
    @Component
    class ProfilePage {
        func build() {
            Column {
                Text("Hello World").fontSize(20)
            }
        }
    }
    ```

## 跨应用跳转

Web组件可以实现点击前端页面超链接跳转到其他应用。

在下面的示例中，点击call.html前端页面中的超链接，跳转到电话应用的拨号界面。

- 应用侧代码：

    1. 获取context

        ```cangjie
        // main_ability.cj
        import kit.AbilityKit.{LaunchReason, LaunchParam, Want, UIAbility, UIAbilityContext}
        import kit.UIKit.AppLog

        var globalAbilityContext: Option<UIAbilityContext> = Option<UIAbilityContext>.None

        class MainAbility <: UIAbility {
            public init() {
                super()
                registerSelf()
            }

            public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
                AppLog.info("MainAbility OnCreated.${want.abilityName}")

                // 获取context
                globalAbilityContext = Option<UIAbilityContext>.Some(this.context)

                match (launchParam.launchReason) {
                    case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
                    case _ => ()
                }
            }

            // ...
        }
        ```

    2. 跳转到拨号界面

        ```cangjie
        // index.cj
        import ohos.state_macro_manage.*
        import kit.LocalizationKit.{__GenerateResource__}
        import kit.ArkWeb.WebviewController
        import kit.UIKit.{Web, BusinessException}
        import kit.AbilityKit.UIAbilityContext
        import kit.TelephonyKit.TelephonyCall

        @Entry
        @Component
        class EntryView {
            let webController = WebviewController()

            // 获取context
            func getContext(): UIAbilityContext {
                match (globalAbilityContext) {
                    case Some(context) => context
                    case _ => throw Exception("can not get globalcontext")
                }
            }

            func build() {
                Column {
                    Web(src: @rawfile("call.html"), controller: this.webController).onLoadIntercept {
                        event =>
                        try {
                            let urlStr: String = event.getRequestUrl()
                            // 判断链接是否为拨号链接
                            if (urlStr.indexOf('tel://') == 0) {
                                // 跳转拨号界面
                                TelephonyCall.makeCall(getContext(), urlStr[6..])
                                return true
                            }
                            return false
                        } catch (e: BusinessException) {
                            AppLog.error("makeCall ErrorCode: ${e.code},  Message: ${e.message}")
                        }
                        return false
                    }
                }
            }
        }
        ```

- 前端页面call.html代码：

    ```html
    <!-- resources/rawfile/call.html -->
    <!DOCTYPE html>
    <html>
    <body>
        <div>
        <a href="tel://xxx xxxx xxx">拨打电话</a> <!-- xxx xxxx xxx 需替换成有效的电话号码 -->
        </div>
    </body>
    </html>
    ```
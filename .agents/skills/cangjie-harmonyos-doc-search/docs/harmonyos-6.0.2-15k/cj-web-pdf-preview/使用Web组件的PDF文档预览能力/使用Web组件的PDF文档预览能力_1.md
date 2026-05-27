# 使用Web组件的PDF文档预览能力

Web组件提供了在网页中预览PDF的能力。应用可以通过Web组件的[src](../../API_Reference/source_zh_cn/arkui-cj/cj-web-web.md#web)参数和[loadUrl()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-loadurlstring)接口中传入PDF文件，来加载PDF文档。根据PDF文档来源不同，可以分为三种常用场景：加载网络PDF文档、加载本地PDF文档、加载应用内resource资源PDF文档。

PDF文档预览加载过程中，若涉及网络文档获取，请在module.json5中配置网络访问权限，添加方法请参见[在配置文件中声明权限](../security/AccessToken/cj-declare-permissions.md)。

```json
"requestPermissions":[
  {
    "name" : "ohos.permission.INTERNET"
  }
]
```

在下面的示例中，Web组件创建时指定默认加载的网络PDF文档 `www.example.com/test.pdf`，该地址为示例，使用时需替换为真实可访问地址:

```cangjie
// index.cj
import ohos.state_macro_manage.*
import kit.ArkWeb.WebviewController
import kit.UIKit.Web

@Entry
@Component
class EntryView {
    let webController = WebviewController()

    func build() {
        Column {
            /*
             * src设置方式：
             * 方式一 加载网络PDF文档："https://www.example.com/test.pdf"
             * 方式二 加载本地应用沙箱内PDF文档： abilityContext.filesDirectory + "/test.pdf"
             * 方式三 应用内resource资源PDF文档： "resource://rawfile/test.pdf"
             * 方式四 应用内resource资源PDF文档： @rawfile(“test.pdf”)
             */
            Web(src: "https://www.example.com/test.pdf", controller: this.webController).domStorageAccess(true)
        }
    }
}
```

上述示例中，由于PDF预览页面对于侧边导航栏是否展开会根据用户操作使用`window.localStorage`进行持久化记录，所以需开启文档对象模型存储[domStorageAccess](../../API_Reference/source_zh_cn/arkui-cj/cj-web-web.md#func-domstorageaccessbool)权限:

```cangjie
Web().domStorageAccess(true)
```

在Web组件创建时，指定默认加载的PDF文档。在默认PDF文档加载完成后，如果需要变更此Web组件显示的PDF文档，可以通过调用[loadUrl()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-loadurlappresource)接口加载指定的PDF文档。[Web组件](../../API_Reference/source_zh_cn/arkui-cj/cj-web-web.md#web)的第一个参数变量src不能通过状态变量（例如：@State）动态更改地址，如需更改，请通过[loadUrl()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#func-loadurlappresource)重新加载。

同时包含三种PDF文档加载预览场景:

- 预览加载网络PDF文件。

    ```cangjie
    Web(src: "https://www.example.com/test.pdf", controller: this.webController)
        .domStorageAccess(true)
    ```

- 预览加载应用沙箱内PDF文件，需要开启应用中文件系统的访问[fileAccess](../../API_Reference/source_zh_cn/arkui-cj/cj-web-web.md#func-fileaccessbool)权限。

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

    2. 开启应用中文件系统的访问

        ```cangjie
        Web(src: globalAbilityContext.getOrThrow().filesDirectory + "/test.pdf", controller: this.webController)
            .domStorageAccess(true)
            .fileAccess(true)
        ```
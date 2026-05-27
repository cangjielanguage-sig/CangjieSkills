### 处理传入的链接

在应用的UIAbility（如EntryAbility）的onCreate()或者onNewWant()生命周期回调中添加如下代码，以处理传入的链接。

```cangjie
import encoding.url.*
import kit.AbilityKit.{UIAbility, Want, LaunchParam}

class MainAbility <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        // 从want中获取传入的链接信息。
        // 如传入的url为：link://www.example.com/programs?action=showall
        let uri = want.uri
        if (uri != "") {
            // 从链接中解析query参数，拿到参数后，开发者可根据自己的业务需求进行后续的处理。
            let urlObject = URL.parse(uri)
            let action = urlObject.queryForm.get("action") ?? ""
            // 例如，当action为showall时，展示所有的节目。
            if (action == "showall") {
                // ...
            }
        }
    }
}
```

若要根据链接参数启动UIAbility的指定页面组件，请参见“[启动UIAbility的指定页面](./cj-uiability-intra-device-interaction.md#启动uiability的指定页面)”。

### 验证应用被拉起效果

1. 对应用进行[手动签名](../../Cangjie_Deveco_Studio/source_zh_cn/cj-ide-signing.md)。

    > **说明：**
    >
    > 不能使用DevEco Studio的自动签名功能，必须使用手动签名，否则无法拉起应用。

2. 编译打包，并安装应用至调试设备。
3. 在拉起方应用中通过App Linking拉起此应用，详情请参见“[拉起方实现跳转指导](#拉起方实现跳转指导)”。
4. 查看集成效果，以“扫码直达”服务的美团单车场景为例：

  ![app-linking-startup-meituan](figures/app-linking-startup-meituan.gif)
### 应用代码开启Web调试开关

调试网页前，需要应用侧代码调用[setWebDebuggingAccess()](../../API_Reference/source_zh_cn/apis/ArkWeb/cj-apis-webview.md#static-func-setwebdebuggingaccessbool)接口开启Web调试开关。

如果没有开启Web调试开关，则DevTools无法发现被调试的网页。

1. 在应用代码中开启Web调试开关，具体如下：

    ```cangjie
    // xxx.cj
    import ohos.state_macro_manage.*
    import kit.ArkWeb.WebviewController
    import kit.UIKit.{Web, BusinessException}

    @Entry
    @Component
    class EntryView {
        let webController = WebviewController()

        public func aboutToAppear(): Unit {
            try {
                // 配置Web开启调试模式
                WebviewController.setWebDebuggingAccess(true)
            } catch (e: BusinessException) {
                AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
            }
        }

        func build() {
            Column {
                Web(src: 'www.example.com', controller: this.webController)
            }
        }
    }
    ```

2. 开启调试功能需要在DevEco Studio应用工程hap模块的module.json5文件中增加如下权限，添加方法请参见[在配置文件中声明权限](../security/AccessToken/cj-declare-permissions.md)。

    ```json
    "requestPermissions":[
      {
        "name" : "ohos.permission.INTERNET"
      }
    ]
    ```

### 将设备连接至电脑

请将设备连接至电脑，随后开启开发者模式，为后续的端口转发操作做好准备。

1. 请开启设备上的开发者模式，并启用USB调试功能。

    (1) 终端系统查看“设置 > 系统”中是否有“开发者选项”，如果不存在，可在“设置 > 关于本机”连续七次单击“版本号”，直到提示“开启开发者模式”，点击“确认开启”后输入PIN码（如果已设置），设备将自动重启。

    (2) USB数据线连接终端和电脑，在“设置 > 系统 > 开发者选项”中，打开“USB调试”开关，弹出的“允许USB调试”的弹框，点击“允许”。

2. 使用hdc命令连接上设备。

    打开命令行执行如下命令，查看hdc能否发现设备。

    ```shell
    hdc list targets
    ```

    - 如果命令有返回设备的ID，则说明hdc已连接上设备。

        ![hdc_list_targets_success](figures/devtools_resources_hdc_list_targets_success.png)

    - 如果命令返回 `[Empty]`，则说明hdc还没有发现设备。

        ![hdc_list_targets_empty](figures/devtools_resources_hdc_list_targets_empty.jpg)

3. 进入hdc shell。

    当hdc命令连接上设备后，执行如下命令，进入hdc shell。

    ```shell
    hdc shell
    ```
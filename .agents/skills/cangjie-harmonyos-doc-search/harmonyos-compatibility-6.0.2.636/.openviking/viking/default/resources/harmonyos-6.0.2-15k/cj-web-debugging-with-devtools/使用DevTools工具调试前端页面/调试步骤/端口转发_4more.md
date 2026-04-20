### 端口转发

当应用代码调用setWebDebuggingAccess接口开启Web调试开关后，ArkWeb内核将启动一个domain socket的监听，以此实现DevTools对网页的调试功能。

但是Chrome浏览器无法直接访问到设备上的domain socket， 所以需要将设备上的domain socket转发到电脑上。

1. 先在hdc shell里执行如下命令，查询ArkWeb在设备里创建的domain socket。

    ```shell
    cat /proc/net/unix | grep devtools
    ```

    - 如果前几步操作无误，该命令的执行结果将显示用于查询的domain socket端口。

        ![hdc_grep_devtools_38532](figures/devtools_resources_hdc_grep_devtools_38532.jpg)

    - 如果没有查询到结果， 请再次确认。

        (1) 应用开启了Web调试开关。

        (2) 应用使用Web组件加载了网页。

2. 将查询到的domain socket转发至电脑的TCP 9222端口。

    执行exit退出hdc shell。

    ```shell
    exit
    ```

    在命令行里执行如下命令转发端口。

    ```shell
    hdc fport tcp:9222 localabstract:webview_devtools_remote_38532
    ```

    > **说明：**
    >
    > - "webview_devtools_remote_" 后面的数字，代表ArkWeb所在应用的进程号， 该数字不是固定的。请将数字改为自己查询到的值。
    > - 如果应用的进程号发生变化（例如，应用重新启动），则需要重新进行端口转发。

    命令执行成功示意图：

    ![hdc_fport_38532_success](figures/devtools_resources_hdc_fport_38532_success.jpg)

3. 在命令行里执行如下命令，检查端口是否转发成功。

    ```shell
    hdc fport ls
    ```

    - 如果有返回端口转发的任务，则说明端口转发成功。

        ![hdc_fport_ls_38532](figures/devtools_resources_hdc_fport_ls_38532.png)

    - 如果返回 `[Empty]`， 则说明端口转发失败。

        ![hdc_fport_ls_empty](figures/devtools_resources_hdc_fport_ls_empty.jpg)

### 在Chrome浏览器上打开调试工具页面

1. 在电脑端Chrome浏览器地址栏中输入调试工具地址 chrome://inspect/\#devices 并打开该页面。

2. 修改Chrome调试工具的配置。

   需要从本地的TCP 9222端口发现被调试网页，所以请确保已勾选 "Discover network targets"。然后再进行网络配置。

   (1) 点击 "Configure" 按钮。

   (2) 在 "Target discovery settings" 中添加要监听的本地端口localhost:9222。

   ![chrome_configure](figures/devtools_resources_chrome_configure.jpg)

3. 为了同时调试多个应用，请在Chrome浏览器的调试工具网页内，于“Devices”选项中的“configure”部分添加多个端口号。

   ![debug-effect](figures/debug-domains.png)

### 等待发现被调试页面

如果前面的步骤执行成功，稍后，Chrome的调试页面将显示待调试的网页。

![chrome_inspect](figures/devtools_resources_chrome_inspect.jpg)

### 开始网页调试

![debug-effect](figures/debug-effect.png)
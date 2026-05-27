# hdc

hdc（HarmonyOS Device Connector）是为开发人员提供的用于调试的命令行工具，通过该工具可以在Windows/Linux/macOS系统上与设备进行交互。

hdc分为三部分：

**client：** 运行在电脑端的进程，开发者在执行hdc命令时启动该进程，命令结束后进程退出。

**server：** 运行在电脑端的后台服务进程，用来管理client进程和设备端的daemon进程之间的数据交互，以及设备发现等。

**daemon：** 作为守护进程运行在设备端，用来响应电脑端server发来的请求。

关系如下图所示：

![hdc框图](./figures/hdc_image_005.PNG)

> **说明：**
>
> hdc client在启动时，默认会判断server是否正在运行，如果没有运行则会启动一个新的hdc程序作为server，运行在后台。
>
> hdc server运行时，默认会监听PC的8710端口，开发者可通过设置系统环境变量OHOS_HDC_SERVER_PORT自定义监听的端口号。

## 环境准备

下载并安装[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/)，hdc应用程序可以在DevEco Studio安装位置下：DevEco Studio\sdk\default\openharmony\toolchains目录中查看。

### （可选）命令行直接执行hdc程序

开发者可通过命令行进入SDK的toolchains目录，在目录中执行hdc相关命令进行调试。

为了方便在命令行中直接执行hdc程序，开发者也可以将hdc程序文件路径添加到操作系统命令搜索路径的环境变量中。

例如，Windows系统可以添加到系统环境变量Path中。

### （可选）server监听端口配置

hdc server启动时，默认会监听PC的8710端口，hdc client使用tcp协议通过此端口连接server。如果PC的8710端口已经被使用或者希望使用其他端口，可以通过添加环境变量OHOS_HDC_SERVER_PORT到系统环境变量中来修改server启动时监听的端口号。

例如，添加变量名为：OHOS_HDC_SERVER_PORT，变量值可设置为任意未被占用的端口，如18710。

> **说明：**
>
> 环境变量配置完成后，关闭并重启命令行或其他使用到HarmonyOS SDK的软件。
# 应用文件上传下载

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

应用可以将应用文件上传到网络服务器，也可以从网络服务器下载网络资源文件到本地应用文件目录。

## 上传应用文件

开发者可以使用上传下载模块（[ohos.request](../../reference/BasicServicesKit/cj-apis-request-agent.md)）的上传接口将本地文件上传。文件上传过程使用系统服务代理完成，支持用户设置自定义代理地址。

> **说明：**
>
> 当前上传应用文件功能，仅支持上传应用缓存文件路径（cacheDir）下的文件。
>
> 使用上传下载模块，请参见[声明权限](../../security/AccessToken/cj-declare-permissions.md)：ohos.permission.INTERNET。

以下示例代码演示将应用缓存文件路径下的文件上传至网络服务器的方式：

<!-- compile -->

```cangjie
// pages/xxx.cj
import ohos.callback_invoke.*
import ohos.business_exception.*
import kit.BasicServicesKit.*
import kit.CoreFileKit.*
import kit.PerformanceAnalysisKit.Hilog

func Upload(): Unit {
    // 获取应用文件路径
    let UiStageContext = Global.abilityContext
    let DefaultSandBoxCache = "/data/storage/el2/base/haps/entry/cache"
    // 新建一个本地应用文件
    let filePath = "${DefaultSandBoxCache}/test.txt"
    let file = FileIo.open(filePath, mode: (OpenMode.CREATE | OpenMode.READ_WRITE))
    FileIo.write(file.fd, "hello world")
    FileIo.fdatasync(file.fd)
    let randomAccessFile = FileIo.createRandomAccessFile(file)
    randomAccessFile.close()
    let responseCallback = ProgressCallback()

    let fileSpec = FileSpec(
        "./test.txt",
        filename: "test.txt",
        mimeType: "application/octet-stream"
    )
    let attachments = ConfigData.FormItems([
        FormItem(
            "taskOnTest",
            FormItemValue.FileItem(fileSpec)
        )
    ])

    let uploadConfig = Config(
        Action.Upload,
        "http://xxx",
        title: "taskOnTest",
        mode: Mode.Foreground,
        description: "Sample code for event listening",
        overwrite: false,
        method: "POST",
        data: attachments,
        saveas: "./",
        network: Network.Cellular,
        metered: false,
        roaming: true,
        retry: true,
        redirect: true,
        index: 0,
        begins: 0,
        ends: -1,
        gauge: false,
        precise: false,
        token: "it is a secret"
    )
    let task = create(UiStageContext, uploadConfig)
    task.on(EventCallbackType.Progress, responseCallback)
    task.start()
}

public class ProgressCallback <: Callback1Argument<Progress> {
    public ProgressCallback() {}

    public open func invoke(err: ?BusinessException, arg: Progress): Unit {
        Hilog.info(0, "CangjieTest", "ProgressCallback Invoke")
    }
}
```
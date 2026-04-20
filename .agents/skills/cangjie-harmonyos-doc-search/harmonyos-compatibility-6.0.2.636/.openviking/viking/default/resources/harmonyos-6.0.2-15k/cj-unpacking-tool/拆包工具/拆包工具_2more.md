# 拆包工具

拆包工具是HarmonyOS提供的一种调测工具，支持通过命令行方式将HAP、HSP、App等文件解压成文件夹，并且提供Java接口对HAP、HSP、App等文件进行解析。

拆包所用的app_unpacking_tool.jar，可以在本地下载的HarmonyOS的SDK库中找到。

> **说明：**
>
> 当前仓颉仅支持开发HAR和HAP包，不支持HSP包，因此本工具中关于HSP包相关的功能，在仓颉程序中不可用。

## 约束与限制

拆包工具需要运行在Java8及其以上环境。
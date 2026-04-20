## 编译态包结构

不同类型的Module编译后会生成对应的HAP、HAR等文件，开发态视图与编译态视图的对照关系如下：

**图2** 开发态与编译态的工程结构视图

![appView](./figures/appView.png)

从开发态到编译态，Module文件变更如下：

- **libs目录**：仓颉源码编译生成.so文件。
- **resources目录**：AppScope目录下的资源文件会合入到Module下面资源目录中，如果两个目录下存在重名文件，编译打包后只会保留AppScope目录下的资源文件。
- **module配置文件**：AppScope目录下的app.json5文件字段会合入到Module下面的module.json5文件之中，编译后生成HAP最终的module.json文件。

> **说明：**
>
> 在编译HAP时，会把它们所依赖的HAR直接编译到HAP中。

## 发布态包结构

每个应用中至少包含一个.hap文件，一个应用中的所有.hap文件合在一起称为**Bundle**，其对应的bundleName是应用的唯一标识（详见[app.json5配置文件](app-configuration-file.md)中的bundleName标签）。

当应用发布上架到应用市场时，需要将Bundle打包为一个.app后缀的文件用于上架，这个.app文件称为**App Pack**（Application Package），与此同时，DevEco Studio工具自动会生成一个**pack.info**文件。**pack.info**文件描述了App Pack中每个HAP的属性，包含APP中的bundleName和versionCode信息、以及Module中的name、type和abilities等信息。

> **说明：**
>
> - App Pack是发布上架到应用市场的基本单元，但是不能在设备上直接安装和运行。
> - 在[应用签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing)、云端分发、端侧安装时，都是以HAP为单位进行签名、分发和安装的。

**图3** 编译发布与上架部署流程图

![hapRelease](./figures/hapRelease.png)
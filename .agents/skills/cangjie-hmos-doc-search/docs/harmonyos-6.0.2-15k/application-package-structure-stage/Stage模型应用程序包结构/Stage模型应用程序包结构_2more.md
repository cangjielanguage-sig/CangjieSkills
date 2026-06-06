# Stage模型应用程序包结构

为了让开发者能对应用程序包在不同阶段的形态有更加清晰的认知，分别对开发态、编译态、发布态的应用程序结构展开介绍。

## 开发态包结构

在DevEco Studio上创建项目工程，并尝试创建多个不同类型的Module。根据实际工程中的目录对照本章节进行学习，可以有助于理解开发态的应用程序结构。

**图1** 项目工程结构示意图（以实际为准）

![project](./figures/cangjieProject.png)

> **说明：**
>
> - AppScope目录由DevEco Studio自动生成，该目录名称更改会导致当前目录下配置文件和资源加载不到，导致编译报错问题，因此该目录名称请勿修改。
> - Module目录名称可以由DevEco Studio自动生成（比如entry、library等），也可以自定义。为了便于说明，下表中统一采用Module_name表示。

工程结构主要包含的文件类型及用途如下：

| 文件类型   | 说明 |
|--------|---------------|
| 配置文件   | 包括应用级配置信息、以及Module级配置信息：<br/> - **AppScope &gt; app.json5**：[app.json5配置文件](app-configuration-file.md)，用于声明应用的全局配置信息，比如应用Bundle名称、应用名称、应用图标、应用版本号等。<br/> - **Module_name &gt; src &gt; main &gt; module.json5**：[module.json5配置文件](module-configuration-file.md)，用于声明Module基本信息、支持的设备类型、所含的组件信息、运行所需申请的权限等。 |
| 仓颉源码文件 | **Module_name &gt; src &gt; main &gt; cangjie**：用于存放Module的仓颉源码文件（.cj文件）。 |
| 资源文件   | 包括应用级资源文件、以及Module级资源文件，支持图形、多媒体、字符串、布局文件等，详见[资源分类与访问](../start/cj-ide-resource-categories-and-access.md)。<br/> - **AppScope &gt; resources** ：用于存放应用需要用到的资源文件。<br/> - **Module_name &gt; src &gt; main &gt; resources** ：用于存放该Module需要用到的资源文件。                                                                      |
| 其他配置文件 | 用于编译构建，包括构建配置文件、编译构建任务脚本、依赖的共享包信息等。<br/> - **build-profile.json5**：工程级<!--add link-->或Module级<!--add link-->的构建配置文件，包括[应用签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing)、产品配置等。 <br/> - **hvigorfile.ts**：工程级或Module级的编译构建任务脚本，开发者可以自定义编译构建工具版本、控制构建行为的配置参数。<br/> - **[oh-package.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-oh-package-json5)**：用于存放依赖库的信息，包括所依赖的三方库和共享包。 |
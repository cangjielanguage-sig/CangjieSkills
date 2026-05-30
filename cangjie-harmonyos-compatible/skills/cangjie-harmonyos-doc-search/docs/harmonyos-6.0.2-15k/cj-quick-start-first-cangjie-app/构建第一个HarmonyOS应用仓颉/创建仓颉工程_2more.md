## 创建仓颉工程

1. 若首次打开**DevEco Studio**，请单击**Create Project**创建工程。如果已经打开了一个工程，请在菜单栏选择**File** > **New** > **Create Project**来创建一个新工程。

2. 选择**Application**应用开发（本文以应用开发为例，仓颉暂不支持元服务开发），选择模板 **[Cangjie] Empty Ability**，单击**Next**进行下一步配置。

   更多模板的使用和说明请见[工程模板介绍](../../../../Cangjie_Deveco_Studio/source_zh_cn/project-manager/cj-project-template-overview.md)。

   ![cangjieTemplate](../../figures/start-cangjieTemplate.png)

3. 进入配置工程界面，可以修改工程名称和存储路径等工程的基本信息，也可以保持默认设置。关于配置工程的基本信息，请参见[创建一个新的工程](../../../../Cangjie_Deveco_Studio/source_zh_cn/project-manager/cj-project-create-new-project.md)。

   ![cangjieConfig](../../figures/start-cangjieConfig.png)

4. 单击 **Finish**，完成工程创建，工具会自动生成基础示例代码和相关资源。

## 仓颉工程目录结构

仓颉工程目录结构如下所示。

```text
Project_name
├── .hvigor
├── .idea
├── AppScope
|    ├── resources
|    └── app.json5
├── entry
│    ├── libs
│    ├── src
│    │    ├── main
│    │    │    ├── cangjie
│    │    │    │    ├── ability_stage.cj
│    │    │    │    ├── index.cj
│    │    │    │    └── main_ability.cj
│    │    │    ├── resources
│    │    │    └── module.json5
│    │    └── ohosTest
│    ├── build-profile.json5
│    ├── cjpm.toml
│    ├── hvigorfile.ts
│    └── oh-package.json5
├── hvigor
│    └── hvigor-config.json5
├── oh_modules
├── build-profile.json5
├── code-linter.json5
├── hvigorfile.ts
├── local.properties
├── oh-package.json5
└── oh-package-lock.json5
```

其中关键文件信息如下：

- **AppScope > app.json5**：应用的全局配置信息。
- **entry**：仓颉工程模块，编译构建生成一个HAP包。
    - **src > main > cangjie**：用于存放仓颉源码。
    - **src > main > resources**：用于存放应用/服务所用到的资源文件，如图形、多媒体、字符串、布局文件等。关于资源文件，请参见[资源分类与访问](../cj-ide-resource-categories-and-access.md)。
    - **src > main > module.json5**：stage 模块配置文件，主要包含 HAP 的配置信息、应用在具体设备上的配置信息以及应用的全局配置信息。
    - **build-profile.json5**：当前的模块信息 、编译信息配置项，包括buildOption、targets配置等。
    - **hvigorfile.ts**：模块级编译构建任务脚本。
    - **cjpm.toml**：仓颉的包管理配置文件。
    - **oh-package.json5**：用来描述包名、版本、入口文件（类型声明文件）和依赖项等信息。
    - **src > ohosTest**：存放仓颉测试源码，用于仓颉Instrument Test。
- **hvigor**：用于存放当前工程使用的 hvigor。
    - **hvigor-config.json5**：指定工程全局使用的 hvigor 以及 hvigor 参数配置。
- **oh_modules**：用于存放三方库依赖信息，包含应用/服务所依赖的第三方库文件。
- **build-profile.json5**：应用级配置信息，包括签名、产品配置等。
- **hvigorfile.ts**：应用级编译构建任务脚本。
- **oh-package.json5**：主要用来描述全局配置，如：依赖覆盖（overrides）、依赖关系重写（overrideDependencyMap）和参数化配置（parameterFile）等。
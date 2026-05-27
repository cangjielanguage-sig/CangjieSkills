## 仓颉与ArkTS混合工程目录结构

仓颉与ArkTS混合工程目录结构如下所示。

```text
Project_name
├── .hvigor
├── .idea
├── AppScope
│    ├── resources
│    └── app.json5
├── entry
│    ├── build
│    ├── har
│    │    └── CJHyAPIRegister-v1.0.1.har
│    ├── libs
│    ├── oh_modules
│    ├── src
│    │    ├── main
│    │    │    ├── cangjie
│    │    │    │    ├── types
│    │    │    │    │    └── libohos_app_cangjie_entry
│    │    │    │    │          ├── Index.d.ts
│    │    │    │    │          └── oh-package.json5
│    │    │    │    └── index.cj
│    │    │    ├── ets
│    │    │    │    ├── entryability
│    │    │    │    ├── entrybackupability
│    │    │    │    └── pages
│    │    │    ├── resources
│    │    │    └── module.json5
│    │    ├── mock
│    │    ├── ohosTest
│    │    └── test
│    ├── build-profile.json5
│    ├── cjpm.toml
│    ├── hvigorfile.ts
│    ├── obfuscation-rules.txt
│    ├── oh-package.json5
│    └── oh-package-lock.json5
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
- **entry**：HarmonyOS工程模块，编译构建生成一个HAP包。
    - **src > har**：用于存放仓颉与ArkTS互操作依赖的HAR模块。
    - **src > main > cangjie**：用于存放仓颉源码。
    - **src > main > cangjie > types**: 仓颉与ArkTS互操作的依赖库。
    - **src > main > ets**：用于存放ArkTS源码。
    - **src > main > ets > entryability**：应用/服务的入口。
    - **src > main > ets > entrybackupability**：应用提供扩展的备份恢复能力。
    - **src > main > ets > pages**：应用/服务包含的页面。
    - **src > main > resources**：用于存放应用/服务所用到的资源文件，如图形、多媒体、字符串、布局文件等。关于资源文件，请参见[资源分类与访问](../cj-ide-resource-categories-and-access.md)。
    - **src > main > module.json5**：模块配置文件。主要包含 HAP 的配置信息、应用/服务在具体设备上的配置信息以及应用/服务的全局配置信息。具体的配置文件说明，请参见[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)。
    - **build-profile.json5**：当前的模块信息 、编译信息配置项，包括buildOption、targets配置等。
    - **cjpm.toml**：仓颉的包管理配置文件，包括编译选项、依赖管理等。
    - **hvigorfile.ts**：模块级编译构建任务脚本。
    - **oh-package.json5**：用来描述包名、版本、入口文件（类型声明文件）和依赖项等信息。
- **hvigor**：用于存放当前工程使用的 hvigor。
    - **hvigor-config.json5**：指定工程全局使用的 hvigor 以及 hvigor 参数配置。
- **oh_modules**：用于存放三方库依赖信息，包含应用/服务所依赖的第三方库文件。
- **build-profile.json5**：应用级配置信息，包括签名、产品配置等。
- **hvigorfile.ts**：应用级编译构建任务脚本。
- **oh-package.json5**：主要用来描述全局配置，如：依赖覆盖（overrides）、依赖关系重写（overrideDependencyMap）和参数化配置（parameterFile）等。
## 在ArkTS模块中增量使用仓颉

> **说明：**
>
> 仓颉模块目前仅支持OpenHarmony的静态库模块，即HAR静态共享包。

仍以上方原始的ArkTS应用工程为例，介绍如何在ArkTS模块中（即**my_module**）使能仓颉开发。

### 右键菜单一键使能仓颉-ArkTS混合模块

1. 按照下图所示，在**Project**窗口，右键单击**my_module**目录，选择 **New -> Cangjie(Interop)**。

![enableCangjie](../../figures/enableCangjie.png)

工程自动同步完成之后，目录结构如下：

```text
├── hvigor
│    ├── hvigor-config.json5
└── my_module
    ├── build
    ├── libs
    ├── oh_modules
    ├── src
    │    ├── main
    │    │    ├── cangjie
    │    │    │    ├── types
    │    │    │    │    └── libohos_app_cangjie_entry
    │    │    │    │          ├── Index.d.ts
    │    │    │    │          └── oh-package.json5
    │    │    │    └── index.cj
    │    │    ├── ets
    │    │    │    └── pages
    │    │    │         └── MyModulePage.ets
    │    │    ├── resources
    │    │    │    └── base
    │    │    │         ├── element
    │    │    │         └── profile
    │    │    │              └── router_map.json
    │    │    └── module.json5
    │    ├── ohosTest
    │    └── test
    ├── build-profile.json5
    ├── consumer-rules.txt
    ├── hvigorfile.ts
    ├── Index.ets
    ├── obfuscation-rules.txt
    ├── oh-package.json5
    └── oh-package-lock.json5
```

可以看出，**my_module** 变成了一个仓颉-ArkTS混合模块。
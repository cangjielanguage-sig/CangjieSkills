## Module类型

Module按照使用场景可以分为两种类型：

- **Ability类型的Module：** 用于实现应用的功能和特性。每一个Ability类型的Module编译后，会生成一个以.hap为后缀的文件，称为HAP（Harmony Ability Package）包。HAP包可以独立安装和运行，是应用安装的基本单位，一个应用可以包含一个或多个HAP包，包含的HAP包分为以下两种类型。
    - entry类型的Module：应用的主模块，包含应用的入口界面、入口图标和主功能特性，编译后生成entry类型的HAP。每一个应用分发到同一类型的设备上的应用程序包，只能包含唯一一个entry类型的HAP，也可以不包含。
    - feature类型的Module：应用的动态特性模块，编译后生成feature类型的HAP。一个应用中可以包含一个或多个feature类型的HAP，也可以不包含。

- **Library类型的Module：** 用于实现代码和资源的共享。同一个Library类型的Module可以被其他的Module多次引用，合理地使用该类型的Module，能够降低开发和维护成本。Library类型的Module分为Static和Shared两种类型，编译后生成共享包。
    - Static Library：静态共享库。编译后生成一个以.har为后缀的文件，即静态共享包HAR（Harmony Archive）。
    - Shared Library：动态共享库。编译后生成一个以.hsp为后缀的文件，即动态共享包HSP（Harmony Shared Package）。

    HAR与HSP两种共享包的主要区别体现在：

    | 共享包类型 | 编译和运行方式  | 发布和引用方式 |
    | --------  | ---- | --- |
    | HAR | HAR中的代码和资源跟随使用方编译，如果有多个使用方，它们的编译产物中会存在多份相同拷贝。<br/>注意：[编译HAR](cj-har-package.md#编译)时，建议开启混淆能力，保护代码资产。 | HAR除了支持应用内引用，还可以独立打包发布到[OHPM中心仓](https://ohpm.openharmony.cn/#/cn/home)或者[OHPM私仓](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo)，供其他应用引用。 |
    | HSP  | HSP中的代码和资源可以独立编译，运行时在一个进程中代码也只会存在一份。 | HSP一般随应用进行打包，当前支持应用内和[集成态HSP](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/quick-start/integrated-hsp.md)。应用内HSP只支持应用内引用，集成态HSP支持发布到OHPM私仓和跨应用引用。<br/>**说明：**<br/> 集成态HSP只是应用内HSP的中间形态，只能参与编译构建过程，无法单独安装。在构建和发布OHPM私仓的过程中，集成态HSP不与特定的应用包名耦合。使用时，工具链支持自动将集成态HSP的包名替换成宿主应用包名，并且会重新签名生成一个新的HSP包，作为宿主应用的安装包，这个新的HSP也属于宿主应用HAP的应用内HSP。|

    **图1** HAR和HSP在APP包中的形态示意图

    ![in-app-har](figures/in-app-hsp-har.png)
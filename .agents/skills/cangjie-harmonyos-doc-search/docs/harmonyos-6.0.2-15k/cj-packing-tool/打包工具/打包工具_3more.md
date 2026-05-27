# 打包工具

打包工具用于在程序编译完成后，对编译出的文件等进行打包，以供安装发布。开发者可以使用DevEco Studio进行打包，也可使用打包工具的JAR包进行打包，JAR包通常存放在SDK路径下的toolchains目录中。

打包工具支持生成：Ability类型的模块包（HAP）、动态共享包（HSP）、应用程序包（App）、快速修复模块包（HQF）、快速修复包（APPQF）。

> **说明：**
>
> 当前仓颉仅支持开发HAR和HAP包，不支持HSP包，因此本工具中关于HSP包相关的功能，在仓颉程序中不可用。

打包指令中的文件来源于[DevEco Studio编译构建产物](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-compile-build)，文件路径查看操作如下。

1. 在DevEco Studio工程根目录下的/hvigor/hvigor-config.json5文件中，修改"logging"下的"level"字段为"debug"。
2. 在DevEco Studio菜单栏，依次选择"构建 -> 清理项目"。
3. 在DevEco Studio菜单栏，依次选择"构建 -> 构建APP(s)"。
4. 在DevEco Studio底部"构建"窗口，搜索"app_packing_tool.jar"，确认打包参数中文件的路径。

## 约束与限制

打包工具需要运行在Java8及其以上环境。

## HAP打包指令

开发者可以使用打包工具的JAR包对模块进行打包，通过传入打包选项、文件路径，生成所需的HAP包。

- Stage模型示例：

    ```bash
    java -jar app_packing_tool.jar --mode hap --json-path <path> [--resources-path <path>] [--ets-path <path>] [--index-path <path>] [--pack-info-path <path>] [--lib-path <path>] --out-path <path> [--force true] [--compress-level 5] [--pkg-context-path <path>] [--hnp-path <path>]
    ```

**表1** HAP打包指令参数说明

| 指令  | 是否必选项 | 选项  | 描述  | 备注  |
| ---- | ---- | --- | ----- | --- |
| --mode | 是  | hap  | 打包类型。  | NA   |
| --json-path | 是  | NA | .json文件路径。Stage模型文件名必须为module.json。 | NA    |
| --profile-path   | 否  | NA | CAPABILITY.profile文件路径。  | NA |
| --maple-so-path  | 否 | NA  | maple so文件输入路径，so文件路径，文件名必须以.so为后缀。如果是多个so需要用“，”分隔。 | NA |
| --maple-so-dir   | 否 | NA  | maple so目录输入路径。 | NA  |
| --dex-path  | 否 | NA  | dex文件路径，文件名必须以.dex为后缀。如果是多个dex需要用“，”分隔。<br/>dex文件路径也可以为目录。 | NA   |
| --lib-path  | 否 | NA | lib库文件路径。| NA   |
| --resources-path | 否  | NA | resources资源包路径。| NA  |
| --index-path  | 否  | NA | .index文件路径，文件名必须为resources.index。| NA |
| --pack-info-path | 否 | NA  | pack.info文件路径，文件名必须为pack.info。| NA |
| --rpcid-path  | 否  | NA | rpcid.sc文件路径，文件名必须为rpcid.sc。 | NA |
| --js-path | 否 | NA | 存放js文件目录路径。| 仅stage模型生效。 |
| --ets-path | 否 | NA  | 存放ets文件目录路径。| 仅stage模型生效。 |
| --out-path  | 是| NA  | 目标文件路径，文件名必须以.hap为后缀。 | NA |
| --force  | 否 | true或者false | 默认值为false。如果为true，表示当目标文件存在时，强制删除。| NA  |
| --an-path | 否  | NA | 存放[an文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-52)的路径。| 仅stage模型生效。 |
| --ap-path | 否| NA | 存放[ap文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-52)的路径。| 仅stage模型生效。 |
| --dir-list | 否 | NA | 可指定目标文件夹列表，将其打入HAP包内。 | NA  |
| --compress-level | 否| number| 压缩等级，默认值1。可选等级1-9。在应用配置compressNativeLibs参数为true的情况下生效，数值越大压缩率越高、压缩速度越慢。 | NA  |
| --pkg-context-path   | 否 | NA  | 可指定语境信息表文件路径，文件名必须为pkgContextInfo.json。 | 仅stage模型生效。|
| --hnp-path | 否 | NA | 指定native软件包文件路径，将native软件包打入HAP包内。 | NA |
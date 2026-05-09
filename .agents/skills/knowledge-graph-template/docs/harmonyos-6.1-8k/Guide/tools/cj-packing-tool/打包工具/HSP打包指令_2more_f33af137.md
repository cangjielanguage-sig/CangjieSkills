## HSP打包指令

HSP包实现了多个HAP对文件的共享，开发者可以使用打包工具的jar包对应用进行打包，通过传入打包选项、文件路径，生成所需的HSP包。

示例：

```bash
java -jar app_packing_tool.jar --mode hsp --json-path <path> [--resources-path <path>] [--ets-path <path>] [--index-path <path>] [--pack-info-path <path>] [--lib-path <path>] --out-path <path> [--force true] [--compress-level 5] [--pkg-context-path <path>]
```

**表2** HSP打包指令参数说明

| 指令   | 是否必选项 | 选项    | 描述   |
| ---- | ------- | ---- | ------ |
| --mode  | 是  | hsp| 打包类型。 |
| --json-path | 是 | NA| .json文件路径，文件名必须为module.json。   |
| --profile-path | 否 | NA  | CAPABILITY.profile文件路径。 |
| --dex-path | 否   | NA | 1. dex文件路径，文件名必须以.dex为后缀。如果是多个dex需要用“，”分隔。<br/>2. dex文件路径也可以为目录。 |
| --lib-path | 否  | NA | lib库文件路径。  |
| --resources-path | 否  | NA  | resources资源包路径。 |
| --index-path     | 否  | NA  | .index文件路径，文件名必须为resources.index。|
| --pack-info-path | 否  | NA | pack.info文件路径，文件名必须为pack.info。 |
| --js-path | 否 | NA| 存放js文件目录路径。|
| --ets-path | 否 | NA  | 存放ets文件目录路径。 |
| --out-path| 是 | NA | 目标文件路径，文件名必须以.hsp为后缀。 |
| --force | 否 | true或者false | 默认值为false。如果为true，表示当目标文件存在时，强制删除。  |
| --compress-level | 否 | number | 压缩等级，默认值1。可选等级1-9。在应用配置compressNativeLibs参数为true的情况下生效，数值越大压缩率越高、压缩速度越慢。 |
| --pkg-context-path | 否 | NA | 可指定语境信息表文件路径，文件名必须为pkgContextInfo.json。 |

## App打包指令

开发者可以使用打包工具的jar包对应用进行打包，通过传入打包选项、文件路径，生成所需的App包。App包用于上架应用市场。

**App打包时HAP合法性校验：** 在对工程内的HAP包打包生成App包时，需要保证被打包的每个HAP在json文件中配置的bundleName、versionCode、minCompatibleVersionCode、debug、minAPIVersion、targetAPIVersion相同，moduleName唯一。HAP模块之间需要保证apiReleaseType相同，HSP模块不校验apiReleaseType。

**打包App时的压缩规则：** 打包App时，对release模式的HAP、HSP包会进行压缩，对debug模式的HAP、HSP包不会压缩。

> **说明：**
>
> 从API version 12开始，App打包不再对versionName校验。

示例：

```bash
java -jar app_packing_tool.jar --mode app [--hap-path <path>] [--hsp-path <path>] --out-path <path> [--signature-path <path>] [--certificate-path <path>] --pack-info-path <path> [--pack-res-path <path>] [--force true] [--encrypt-path <path>]
```

**表3** App打包指令参数说明

| 指令  | 是否必选项 | 选项  | 描述    |
|--------|-------|-------|------|
| --mode  | 是| app  | 多个HAP需满足HAP的合法性校验。                                           |
| --hap-path  | 否   | NA   | HAP包文件路径，文件名必须以.hap为后缀。如果是多个HAP包需要用“，”分隔。<br/>HAP包文件路径也可以是目录。 |
| --hsp-path   | 否| NA  | HSP包文件路径，文件名必须以.hsp为后缀。如果是多个HSP包需要用“，”分隔。<br/>HSP包文件路径也可以是目录。 |
| --pack-info-path | 是  | NA | 文件名必须为pack.info。|
| --out-path  | 是 | NA| 目标文件路径，文件名必须以.app为后缀。 |
| --signature-path | 否 | NA  | 签名路径。  |
| --certificate-path | 否 | NA  | 证书路径。  |
| --pack-res-path    | 否 | NA  | pack.res快照文件路径。 |
| --force   | 否 | true或者false | 默认值为false。如果为true，表示当目标文件存在时，强制删除。 |
| --encrypt-path | 否 | NA  | 文件名必须为encrypt.json 。  |
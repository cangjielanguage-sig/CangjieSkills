## fastApp模式打包指令

开发者可以使用打包工具的jar包对应用进行打包，通过传入打包选项、HAP、HSP包文件目录路径，生成所需的App包。App包用于上架应用市场。

**App打包时HAP合法性校验：** 在对工程内的HAP包打包生成App包时，需要保证被打包的每个HAP在json文件中配置的bundleName、versionCode、minCompatibleVersionCode、debug、minAPIVersion、targetAPIVersion相同，moduleName唯一。HAP模块之间需要保证apiReleaseType相同，HSP模块不校验apiReleaseType。

**打包App时的压缩规则：** 打包App时，对release模式的HAP、HSP包会进行压缩，对debug模式的HAP、HSP包不会压缩。

示例：

```bash
java -jar app_packing_tool.jar --mode fastApp [--hap-path <path>] [--hsp-path <path>] --out-path <path> [--signature-path <path>] [--certificate-path <path>] --pack-info-path <path> [--pack-res-path <path>] [--force true] [--encrypt-path <path>]
```

**表10** 参数含义及规范

| 指令  | 是否必选项 | 选项    | 描述    |
|------|-------|---------|-----|
| --mode     | 是     | fastApp    | 多个HAP需满足HAP的合法性校验。  |
| --hap-path         | 否     | NA         | HAP包文件目录路径，目录内要包含一个完整的HAP包的所有文件。允许传入多个路径，多个路径需要用英文“,”分隔。   |
| --hsp-path     | 否     | NA         | 1. HSP包文件路径，文件名必须以.hsp为后缀。如果是多个HSP包需要用英文“,”分隔。<br/>2. HSP包文件目录路径，目录内要包含一个完整的HSP包的所有文件。允许传入多个路径，多个路径需要用英文“,”分隔。 |
| --pack-info-path   | 是     | NA  | 文件名必须为pack.info。   |
| --out-path  | 是  | NA  | 目标文件路径，文件名必须以.app为后缀。  |
| --signature-path   | 否     | NA    | 签名路径。 |
| --certificate-path | 否     | NA   | 证书路径。  |
| --pack-res-path    | 否     | NA   | pack.res快照文件路径。 |
| --force            | 否     | true或者false | 默认值为false。如果为true，表示当目标文件存在时，强制删除。  |
| --encrypt-path     | 否     | NA   | 文件名必须为encrypt.json。|
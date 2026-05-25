## 多工程打包指令

多工程打包适用于多个团队开发同一个应用，但不方便共享代码的情况。开发者通过传入已经打好的HAP、HSP和App包，将多个包打成一个最终的App包，并上架应用市场。

**多工程打包HAP合法性校验：** 需要保证被打包的每个HAP在json文件中配置的bundleName、versionCode、minCompatibleVersionCode、debug属性相同，minAPIVersion、targetAPIVersion、compileSdkVersion、compileSdkType相同，moduleName唯一，同一设备entry唯一。HAP模块之间需要保证apiReleaseType相同，HSP模块不校验apiReleaseType。

> **说明：**
>
> 从API version 12开始，多工程打包不再对versionName校验。

示例：

```bash
java -jar app_packing_tool.jar --mode multiApp [--hap-list <path>] [--hsp-list <path>] [--app-list <path>] --out-path <option> [--force true] [--encrypt-path <path>]
```

**表4** 多工程打包指令参数说明

| 指令| 是否必选项 | 选项| 描述  |
|---|-------|------|-------|
| --mode     | 是     | multiApp  | 打包类型，在将多个HAP打入同一个App时，需保证每个HAP满足合法性校验规则。                                                            |
| --hap-list | 否     | HAP的路径    | HAP包文件路径，文件名必须以.hap为后缀。如果是多个HAP包需要”，“分隔。<br/>HAP文件路径也可以是目录。                                          |
| --hsp-list | 否     | HSP的路径    | HSP包文件路径，文件名必须以.hsp为后缀。如果是多个HSP包需要”，“分隔。<br/>HSP文件路径也可以是目录。                                          |
| --app-list | 否     | App的路径    | App文件路径，文件名必须以.app为后缀。如果是多个App包需要用”，“分隔。<br/>App文件路径也可以是目录。<br/>--hap-list，--hsp-list，--app-list不可以都不传。 |
| --out-path | 是     | NA | 目标文件路径，文件名必须以.app为后缀。 |
| --force    | 否     | true或者false | 默认值为false。如果为true，表示当目标文件存在时，强制删除。 |
| --encrypt-path | 否     | encrypt.json的路径 | 文件名必须为encrypt.json。 |

## HQF打包指令

HQF包适用于应用存在一些问题，需要紧急修复的场景。开发者可以使用打包工具的jar包对应用进行打包，通过传入打包选项、文件路径，生成所需的HQF包。

示例:

```bash
java -jar app_packing_tool.jar --mode hqf --json-path <path> [--lib-path <path>] [--ets-path <path>] [--resources-path <path>] --out-path <path> [--force true]
```

**表5** HQF打包指令参数说明

| 指令  | 是否必选项 | 选项  | 描述   |
|-------------|-------|-----|-------|
| --mode      | 是     | hqf   | 打包类型。    |
| --json-path | 是 | NA | .json文件路径，文件名必须为patch.json。 |
| --lib-path  | 否     | NA  | lib库文件的路径。   |
| --ets-path  | 否     | NA      | 存放ets文件目录路径。   |
| --resources-path  | 否     | NA | resources资源包路径。   |
| --out-path  | 是     | NA  | 目标文件路径，文件名必须以.hqf为后缀。 |
| --force     | 否     | true或者false | 默认值为false。如果为true，表示当目标文件存在时，强制删除。 |

## APPQF打包指令

APPQF包由一个或多个HQF文件组成。这些HQF包在应用市场会从APPQF包中拆分出来，再被分发到具体的设备上。开发者可以使用打包工具的jar包对应用进行打包，通过传入打包选项、文件路径，生成所需的APPQF包。

示例:

```bash
java -jar app_packing_tool.jar --mode appqf --hqf-list <path> --out-path <path> [--force true]
```

**表6** APPQF打包指令参数说明

| 指令  | 是否必选项 | 选项  | 描述  |
|------------|-------|-----|-----|
| --mode     | 是     | appqf       | 打包类型。 |
| --hqf-list | 是 | NA   | [HQF文件](#hqf打包指令)路径，多个HQF以英文逗号隔开。              |
| --out-path | 是 | NA   | 目标文件路径，文件名必须以.appqf为后缀。 |
| --force    | 否     | true或者false | 默认值为false。如果为true，表示当目标文件存在时，强制删除。 |
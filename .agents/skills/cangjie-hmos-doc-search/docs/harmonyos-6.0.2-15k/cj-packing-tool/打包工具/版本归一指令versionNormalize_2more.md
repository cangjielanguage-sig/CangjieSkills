## 版本归一指令（versionNormalize）

同一个App中，所有HAP、HSP包的versionName和versionCode需要保持一致。当只有一个HAP或HSP需要修改升级时，可以调用此命令，将多个HAP、HSP的版本统一。本命令会修改所传入的HAP、HSP的版本号和版本名称，并在指定目录生成修改后的同名HAP、HSP，以及一个version_record.json文件，用于记录所有HAP、HSP原有的版本号、版本名称。

示例：

```bash
java -jar path\app_packing_tool.jar --mode versionNormalize --input-list 1.hap,2.hsp --version-code 1000001 --version-name 1.0.1 --out-path path\out\
```

**表7** versionNormalize指令参数说明

| 指令   | 是否必选项 | 选项  | 描述   |
|----------------|-------|------------------|-----|
| --mode         | 是     | versionNormalize | 命令类型。   |
| --input-list   | 是     | HAP或HSP的路径       | 1. HAP或HSP包文件路径，文件名必须以.HAP或.HSP为后缀。如果是多个HAP或HSP包需要“,”分隔。<br/>2. 传入目录时，会读取目录下所有的HAP和HSP文件。 |
| --version-code | 是     | 版本号   | 指定的版本号，HAP、HSP的版本号会被修改为该版本。需要为整数，且不小于所有传入的HAP、HSP的版本号。            |
| --version-name | 是  | 版本名称   | 指定的版本名称，HAP、HSP的版本名称会被修改为该版本名称。  |
| --out-path     | 是   | NA    | 目标文件路径，需要为一个目录。   |

## 包名归一指令（packageNormalize）

此命令可以修改传入的HSP的包名和版本号，并在指定目录生成修改后的同名HSP。

示例：

```bash
java -jar path\app_packing_tool.jar --mode packageNormalize --hsp-list path\1.hsp,path\2.hsp --bundle-name com.example.myapplication --version-code 1000001 --out-path path\out\
```

**表8**  参数含义及规范

| 指令 | 是否必选项 | 选项   | 描述  |
|------|-------|------|---|
| --mode | 是     | packageNormalize | 命令类型。 |
| --hsp-list     | 是     | HSP的路径      | 1. HSP包文件路径，文件名必须以.hsp为后缀。如果是多个HSP包需要“,”分隔。<br/>2. HSP包目录。 |
| --bundle-name  | 是 | 包名 | 指定的包名，HSP的包名会被修改为指定的包名。 |
| --version-code | 是     | 版本号  | 指定的版本号，HSP的版本号会被修改为该版本号。需要为整数，且大于0。  |
| --out-path     | 是     | NA | 目标文件路径，需要为一个目录。 |
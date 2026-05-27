## 应用版本声明配置

应用版本声明需要在工程的AppScope目录下的[app.json5配置文件](../cj-start/basic-knowledge/app-configuration-file.md)中配置versionCode标签和versionName标签。versionCode用于标识应用的版本号，该标签值为32位非负整数。此数字仅用于确定某个版本是否比另一个版本更新，数值越大表示版本越高。versionName标签标识版本号的文字描述。

## Module支持的设备类型配置

Module支持的设备类型需要在[module.json5配置文件](../cj-start/basic-knowledge/module-configuration-file.md)中配置[deviceTypes标签](../cj-start/basic-knowledge/module-configuration-file.md#devicetypes标签)，如果deviceTypes标签中添加了某种设备，则表明当前的Module支持在该设备上运行。

## Module权限配置

Module访问系统或其他应用受保护部分所需的权限信息需要在[module.json5配置文件](../cj-start/basic-knowledge/module-configuration-file.md)中配置[requestPermissions标签](../security/AccessToken/cj-declare-permissions.md)。该标签用于声明需要申请权限的名称、申请权限的原因以及权限使用的场景。
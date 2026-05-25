### Distro结构体信息

| 字段                | 类型    | 描述                       | 备注                                                         |
| ------------------- |---------| ------------------------- | ------------------------------------------------------------ |
| moduleName          | String  | 标识当前module的名字。    | 对应Stage模型中module结构体中的moduleName字段。                 |
| moduleType          | String  | 标识当前HAP的类型。       | 对应Stage模型中module结构体中的moduleType字段。                 |
| deliveryWithInstall | boolean | 标识当前HAP是否在用户主动安装的时候安装。true表示安装，false表示不安装。 | 对应Stage模型中module结构体中的deliveryWithInstall字段。         |
| installationFree    | int     | 标识当前HAP是否支持免安装特性。           | 对应Stage模型中module结构体中的installationFree字段，json文件中如果配置了该字段为true，返回1；配置为false，返回0；未配置返回2。 |
| virtualMachine      | String  | 标识当前HAP运行的目标虚拟机类型，供云端分发使用，如应用市场和分发中心。 | 对应Stage模型中module结构体中的virtualMachine字段。 |

### MetaData结构体信息

| 字段           | 类型                 | 描述                             | 备注                      |
| -------------- |----------------------| -------------------------------- | ------------------------- |
| parameters     | List\<MetaDataInfo>  | 标识Metadata的参数信息。           | FA模型特有，stage模型废弃。  |
| results        | List\<MetaDataInfo>  | 标识Metadata的results信息。        | FA模型特有，stage模型废弃。  |
| customizeDatas | List\<CustomizeData> | 标识Metadata的customizeDatas信息。 | NA                         |

### MetaDataInfo结构体信息

| 字段        | 类型   | 描述                              | 备注                      |
| ----------- | ------ | --------------------------------- | ------------------------- |
| name        | String | 标识MetaDataInfo的name信息。        | FA模型特有，stage模型废弃。  |
| description | String | 标识MetaDataInfo的description信息。 | FA模型特有，stage模型废弃。  |
| type        | String | 标识MetaDataInfo的type信息。        | FA模型特有，stage模型废弃。  |

### CustomizeData结构体信息

| 字段  | 类型   | 描述                         | 备注                    |
| ----- | ------ | ---------------------------- | ----------------------- |
| name  | String | 标识CustomizeData的name信息。  | 对应stage模型的metadata。 |
| value | String | 标识CustomizeData的value信息。 | 对应stage模型的metadata。 |
| extra | String | 标识CustomizeData的extra信息。 | 对应stage模型的metadata。 |

### ReqPermission结构体信息

| 字段      | 类型                               | 描述                                                       | 备注 |
| --------- | ---------------------------------- |------------------------------------------------------------| ---- |
| name      | String                             | 标识ReqPermission的名称信息。                                 | NA   |
| reason    | String                             | 当申请的权限为user_grant权限时此字段必填，描述申请权限的原因。 | NA   |
| usedScene | UsedScene结构体（见下述UsedScene） | 描述权限使用的场景和时机。场景类型有：ability、调用时机（when），可配置多个ability。 | NA   |
| reasons   | HashMap\<String, String>           | 当申请的权限为user_grant权限时此字段必填，描述申请权限的原因。 | NA    |

### UsedScene结构体信息

| 字段    | 类型          | 描述                                                         | 备注 |
| ------- | ------------- | ------------------------------------------------------------ | ---- |
| ability | List\<String> | 标识需要使用到该权限的元能力（ability），该标签值为数组形式。   | NA   |
| when    | String        | 标识使用该权限的时机，值为inuse/always，表示为仅允许前台使用和前后台都可使用。 | NA   |

### Shortcut结构体信息

| 字段       | 类型                   | 描述                                                         | 备注 |
| ---------- | ---------------------- | :----------------------------------------------------------- | ---- |
| shortcutId | String                 | 标识ShortCut的Id。                                             | NA   |
| label      | String                 | 标识ShortCut的标签信息。                                       | NA   |
| icon       | String                 | 标识ShortCut的图标信息。                                       | NA   |
| intents    | List\<IntentInfo>      | 标识快捷方式内定义的目标intent信息集合，每个intent可配置两个子标签，targetClass,targetBundle。 | NA   |
| labels     | HashMap\<String, String> | 标识多语言下ShortCut对用户显示的名称。                        | NA   |
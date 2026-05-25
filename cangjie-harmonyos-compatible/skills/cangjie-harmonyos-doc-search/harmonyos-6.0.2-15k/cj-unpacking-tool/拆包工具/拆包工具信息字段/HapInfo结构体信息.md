### HapInfo结构体信息

| 字段                 | 类型                        | 描述                               | 备注       |
| ---------------------|----------------------------|------------------------------------| -----------|
| appModel             | AppModel枚举值              | 标识应用的框架模型。<br/>- FA：FA模型。<br/>- STAGE：Stage模型。 | NA |
| packageStr           | String                      | 标识应用的包信息。     | FA模型特有。             |
| name                 | String                      | 标识当前module的名字。                | NA                 |
| description          | String                      | 标识HAP包的描述信息。                 | FA模型特有。                  |
| supportedModes       | List\<String>               | 标识HAP包的支持的模式。               | NA                           |
| abilities            | List\<AbilityInfo>          | 标识HAP包ability信息。                | NA                             |
| defPermissions       | List\<DefPermission>        | 标识HAP包DefPermission信息。          | NA                             |
| definePermissions    | List\<DefinePermission>     | 标识HAP包DefinePermission信息。       | NA                             |
| defPermissionsGroups | List\<DefPermissionsGroups> | 标识HAP包DefPermissionsGroups 信息。  | NA                             |
| distro               | Distro结构体                 | 标识HAP包的distro信息。               | NA                      |
| reqCapabilities      | List\<String>               | 标识HAP包reqCapabilities信息。        | NA                           |
| deviceType           | List\<String>               | 标识HAP可以运行在哪类设备上。   对应stage模型中的deviceTypes。       | NA |
| metaData             | MetaData结构体（见下述metaData）| 标识HAP的自定义元信息。                | NA           |
| dependencies         | List\<DependencyItem>       | 标识HAP包DependencyItem信息。         | NA                   |
| isJs                 | boolean                     | 标识该应用是否是js应用。true表示是js应用，false表示不是js应用。              | FA模型特有。            |
| reqPermissions       | list\<ReqPermission>        | 标识应用申请的权限的集合。      | 对应stage模型的requestPermissions。 |
| commonEvents         | CommonEvent结构体（见下述CommonEvent）       | 标识静态事件。                         | NA     |
| shortcuts            | list\<Shortcut>                               | 标识应用的shortcuts信息。              | NA                  |
| distroFilter         | DistroFilter结构体                            | 标识应用市场按设备形态分发的信息。     | NA               |
| srcEntrance          | String                                        | 标识应用对应的入口代码路径。           | stage模型新增。          |
| process              | String                                        | 标识HAP的进程名                      | stage模型新增。       |
| mainElement          | String                  | 标识HAP的入口ability名称或者extension名称。 | stage模型新增，FA模型将mainAbility的值赋值给mainElement。 |
| uiSyntax             | String                                        | 定义该JS Component的语法类型。         | stage模型新增。       |
| pages                | List\<String>                                 | 列举JS Component中每个页面信息。       | stage模型新增。       |
| extensionAbilityInfos| List\<ExtensionAbilityInfo>                   | 描述extensionAbility的配置信息。       | stage模型新增。        |
| moduleAtomicService  | ModuleAtomicService结构体（见下述ModuleAtomicService） | 描述HAP的原子化服务信息。          | NA              |
| formInfos            | List\<AbilityFormInfo>                        | 描述卡片的信息。                       | NA              |
| descriptions         | HashMap\<String, String>                      | 标识HAP的说明信息。                    | NA             |
| compressedSize       | long                                          | 标识HAP包压缩后的大小，单位字节。         | NA              |
| originalSize         | long                                          | 标识HAP包的原始大小，单位字节。         | NA             |
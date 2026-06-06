### ExtensionAbilityInfo结构体信息

| 字段            | 类型                     | 描述                                                  | 备注                                |
| --------------- | ------------------------ | ----------------------------------------------------- | ----------------------------------- |
| name            | String                   | 标识当前extensionAbility的逻辑名。                      | stage模型支持。                      |
| srcEntrance     | String                   | 标识extensionAbility所对应的js代码路径。                | stage模型支持。                      |
| icon            | String                   | 标签标识extensionAbility图标。                          | stage模型支持。                      |
| label           | String                   | 标识extensionAbility对用户显示的名称。                  | stage模型支持。                      |
| description     | String                   | 标识extensionAbility的描述。                            | stage模型支持。                      |
| type            | String                   | 标识extensionAbility的类型：form、workScheduler、inputMethod、service、accessibility、dataShare、fileShare、wallpaper、backup。 | stage模型支持，目前仅解析了form、staticSubscriber的信息、其他类型（如：workScheduler、inputMethod、service、accessibility、dataShare、fileShare、wallpaper、backup）暂未解析。        |
| permissions     | List\<String>            | 标识被其它应用的ability调用时需要申请的权限的集合。       | stage模型支持。                      |
| readPermission  | String                   | 标识读取ability的数据所需的权限。                         | stage模型支持。                    |
| writePermission | String                   | 标识向ability写数据所需的权限。                           | stage模型支持。                   |
| visible         | boolean                  | 标识extensionAbility是否可以被其它应用调用。              | stage模型支持。                   |
| skills          | List\<SkillInfo>         | 标识extensionAbility能够接收的意图的特征集。              | stage模型支持。                    |
| metadataInfos   | List\<ModuleMetadataInfo>| 标识extensionAbility能够接收的元数据信息。                | stage模型支持。                    |
| metadata        | MetaData结构体           | 标识extensionAbility的元信息。                            | 将metadata中的信息赋值到CustomizeData中。 |
| uri             | String                   | 标识extensionAbility提供的数据uri。                       | stage模型支持。                           |
| descriptions    | HashMap\<String, String> | 标识多语言下extensionAbility的描述。                      | NA                              |
| labels          | HashMap\<String, String> | 标识多语言下extensionAbility对用户显示的名称。            | NA                             |

### SkillInfo结构体信息

| 字段     | 类型                | 描述                   | 备注 |
| -------- | ------------------- |----------------------| ---- |
| actions  | List\<String>       | 标识能够接收的意图的action值的集合。 | NA   |
| entities | List\<String>       | 标识能够接收的意图的元能力的类别集合。   | NA   |
| domainVerify | boolean       | ability是否支持域校验。true表示支持，false表示不支持。   | NA   |

### UriInfo结构体信息

| 字段          | 类型   | 描述                     | 备注 |
| ------------- | ------ |------------------------| ---- |
| schema        | String | 标识ModuleUriInfo的范式信息。   | NA   |
| host          | String | 标识ModuleUriInfo的宿主信息。   | NA   |
| port          | String | 标识ModuleUriInfo的端口信息。   | NA   |
| pathStartWith | String | 标识ModuleUriInfo的路径前缀。   | NA   |
| pathRegex     | String | 标识ModuleUriInfo的路径正则信息。 | NA   |
| path          | String | 标识ModuleUriInfo的路径信息。   | NA   |
| type          | String | 标识ModuleUriInfo的种类。     | NA   |
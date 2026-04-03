### AbilityInfo结构体信息

| 字段              | 类型                       | 描述                         | 备注                        |
|-------------------|---------------------------| ---------------------------- | -------------------------- |
| name              | String                    | 标识当前ability的逻辑名。        | NA                              |
| description       | String                    | 标识ability的描述。             | NA                              |
| descriptionRes    | String                    | 标识ability资源的描述。            | NA                              |
| icon              | String                    | 标识ability图标。            | NA                              |
| iconPath          | String                    | 标识ability图标路径。      | NA                              |
| label             | String                    | 标识ability对用户显示的名称。       | NA                              |
| labelRes          | String                    | 标识ability对用户显示的名称资源。      | NA                    |
| type              | String                    | 标识ability类型。      | Stage模型下该值直接赋予page类型。 |
| formsEnabled      | boolean                   | 标识ability卡片是否使能。true表示使能，false表示不使能。      | NA                              |
| formInfo          | FormInfo结构体             | 描述卡片的信息。       | NA                              |
| uri               | String                    | 标识ability的uri信息。      | FA模型支持。                      |
| launchType        | String                    | 标识ability中的launcherType信息。         | NA                      |
| orientation       | String                    | 标识ability中的orientation信息。      | NA                              |
| visible           | boolean                   | 标识ability中的visible信息。true表示可见，false表示不可见。      | NA                              |
| grantPermission   | boolean                   | 标识ability中的grantPermission信息。   | NA                              |
| readPermission    | String                    | 标识ability中的readPermission信息。  | NA                              |
| writePermission   | String                    | 标识ability中的writePermission信息。    | NA                              |
| uriPermissionMode | String                    | 标识ability中的uriPermissionMode信息。   | NA                              |
| uriPermissionPath | String                    | 标识ability中的uriPermissionPath信息。 | NA                              |
| directLaunch      | boolean                   | 标识ability中的directLaunch信息。   | NA                              |
| mission           | String                    | 标识ability中的mission信息。    | NA                              |
| targetAbility     | String                    | 标识ability中的targetAbility信息。   | NA                              |
| multiUserShared   | boolean                   | 标识ability中的multiUserShared信息。true表示支持多用户状态进行共享，false表示不支持多用户状态进行共享。   | NA                              |
| supportPipMode    | boolean                   | 标识ability中的supportPipMode信息。true表示支持用户进入PIP模式，false表示不支持用户进入PIP模式。  | NA                              |
| srcLanguage       | String                    | 标识ability中的srcLanguage信息。     | NA                              |
| srcPath           | String                    | 标识ability中的srcPath信息。  | NA                              |
| srcEntrance       | String                    | 标识ability中的srcEntrance信息。      | NA                              |
| continuable       | boolean                   | 标识ability中的continuable信息。true表示ability可迁移，false表示不可迁移。 | NA                              |
| metaData          | MetaData结构体（见下述MetaData） | 标识ability的自定义元信息。     | NA                             |
| configChanges     | List\<String>             | 标识ability中的configChanges信息。    | NA                              |
| formInfos         | List\<AbilityFormInfo>    | 标识ability中的forms信息。              | NA                              |
| permissions       | List\<String>             | 标识ability中的permissions信息。           | NA                              |
| skills            | List\<SkillInfo>          | 标识ability中的skills信息。               | NA                              |
| backgroundModes   | List\<String>             | 标识ability中的backgroundModes信息。       | NA                              |
| labels            | HashMap\<String, String>  | 标识多语言下ability对用户显示的名称。     | NA                             |
| descriptions      | HashMap\<String, String>  | 标识多语言下ability的描述。              | NA                              |
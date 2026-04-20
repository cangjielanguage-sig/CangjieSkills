### AbilityFormInfo结构体信息

| 字段                | 类型                     | 描述                                                         | 备注        |
| ------------------- | -------------------------| ------------------------------------------------------------ |-----------|
| name                | String                   | 标识forms的名称。                                              | NA        |
| type                | String                   | 标签标识卡片的类型。                                           | NA        |
| updateEnabled       | boolean                  | 标识该卡片是否支持定时刷新。true表示支持，false表示不支持。                                   | NA        |
| scheduledUpdateTime | String                   | 标签标识卡片顶点刷新的时间，采用24小时计数，精确到分钟。       | NA        |
| updateDuration      | int                      | 标识卡片定时刷新的更新频率，单位为30分钟，取值为30的倍数值。   | NA        |
| supportDimensions   | List\<String>            | 标识卡片外观规格，取值为”1 * 2“，”2 * 2“，”2 * 4“，”4 * 4“。   | NA        |
| defaultDimension    | String                   | 标识卡片默认外观规格，取值必须在supportDimensions配置的列表中。 | NA        |
| MetaData            | MetaData                 | 标识卡片的自定义信息。                                         | NA        |
| description         | String                   | 标识forms的描述。                                              | stage模型新增。 |
| src                 | String                   | 标签JS卡片对应的UI代码。                                       | NA        |
| windowInfo          | ModuleWindowInfo结构体   | 标签能力窗体的窗口。                                       | NA        |
| isDefault           | boolean                  | 标识该卡片是否为默认卡片，每个HAP有且只能有一个默认卡片。true表示默认卡片，false表示非默认卡片。      | NA        |
| colorMode           | String                   | 标识卡片的色调，取值为auto、dark、light其中之一。              | NA        |
| formConfigAbility   | String                   | 标识卡片调整的Ability名称。                                    | NA        |
| formVisibleNotify   | String                   | 标识卡片是否被允许使用卡片可见性通知。                         | NA        |
| providerAbility     | String                   | 卡片的提供方所在的Ability或者extension名称。<br/>1. FA模型：如果卡片配置在service类型的ability中，providerAbility配置为mainAbility。<br/>2. FA模型：如果卡片配置在Page类型的Ability中，providerAbility配置为当前Ability。<br/>3. FA模型：如果没有配置mainAbility，providerAbility配置为当前HAP包中的优先使用system.home，否则第一个page的Ability。<br/>4. stage模型中（follow上述规则），providerAbility配置为mainElement。 | NA |
| descriptions        | HashMap\<String, String> | 标识多语言下ability的描述。      | NA     |
## 隐式Want匹配原理

隐式[Want](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-want)匹配原理如下表所示。

| 名称        | 类型                           | 匹配项 | 必选 | 规则                                                         |
| ----------- | ------------------------------ | ------ | ---- | ------------------------------------------------------------ |
| deviceId    | String                         | 是     | 否   | 跨设备目前不支持隐式调用。                                   |
| abilityName | String                         | 否     | 否   | 该字段必须留空表示隐式匹配。                                 |
| bundleName  | String                         | 是     | 否   | 匹配对应应用包内的目标应用组件。                              |
| moduleName  | String                         | 是     | 否   | 匹配对应Module内的目标应用组件。                              |
| uri         | String                         | 是     | 否   | 参见[want参数的uri和type匹配规则](#want参数的uri和type匹配规则)。                                                             |
| type        | String                         | 是     | 否   | 参见[want参数的uri和type匹配规则](#want参数的uri和type匹配规则)。                                                             |
| action      | String                         | 是     | 否   | 参见[want参数的action匹配规则](#want参数的action匹配规则)。                                                             |
| entities    | Array&lt;String&gt;            | 是     | 否   | 参见[want参数的entities匹配规则](#want参数的entities匹配规则)。                                                             |
| flags       | UInt32                         | 否     | 否   | 不参与匹配，直接传递给系统处理，一般用来设置运行态信息，例如URI数据授权等。 |
| parameters  | String | 是     | 否   | 应用自定义数据将直接传递给目标应用组件。当前支持使用key为linkFeature的参数进行匹配，当linkFeature字段取值不为空时，优先进行linkFeature匹配。|

从隐式Want的定义，可得知：

- 调用方传入的want参数，表明调用方需要执行的操作，并提供相关数据以及其他应用类型限制。
- 待匹配应用组件的skills配置，声明其具备的能力（[module.json5配置文件](../cj-start/basic-knowledge/module-configuration-file.md)中的[skills标签](../cj-start/basic-knowledge/module-configuration-file.md#skills标签)参数）。

系统将调用方传入的want参数（包含action、entities、uri、type和parameters属性）与已安装待匹配应用组件的skills配置（包含actions、entities、uris和type属性）进行匹配。当want参数五个属性匹配均未配置，隐式匹配失败。

- 当parameters中的linkFeature字段取值不为空时，系统将优先进行linkFeature匹配。
    - 如果linkFeature匹配成功，并且want中配置了uri或type，则继续匹配uri和type属性，均匹配成功则隐式匹配成功；否则，匹配失败。如果want中未配置uri和type, 则隐式匹配成功。
    - 如果linkFeature匹配失败，则不进行后续属性匹配，匹配失败。
- 当parameters中的linkFeature未配置或取值为空时，只有当action、entities、uri和type四个属性均匹配通过时，此应用才会被应用选择器展示给用户进行选择。
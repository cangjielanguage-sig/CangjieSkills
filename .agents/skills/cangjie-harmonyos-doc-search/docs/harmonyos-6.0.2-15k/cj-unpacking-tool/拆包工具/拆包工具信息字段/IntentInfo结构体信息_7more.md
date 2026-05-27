### IntentInfo结构体信息

| 字段         | 类型   | 描述             | 备注 |
| ------------ | ------ | ---------------- | ---- |
| targetClass  | String | 快捷方式目标类型。 | NA   |
| targetBundle | String | 快捷方式目标包名。 | NA   |

### DistroFilter结构体信息

| 字段          | 类型                | 描述                                  | 备注 |
| ------------- | ------------------- | ------------------------------------- | ---- |
| apiVersion    | ApiVersion结构体    | 标识DistroFilter中的apiVersion信息。    | NA   |
| screenShape   | ScreenShape结构体   | 标识DistroFilter中的screenShape信息。   | NA   |
| screenDensity | ScreenDensity结构体 | 标识DistroFilter中的screenDensity信息。 | NA   |
| screenWindow  | ScreenWindow结构体  | 标识DistroFilter中的screenWindow信息。  | NA   |
| countryCode   | CountryCode结构体   | 标识DistroFilter中的countryCode信息。   | NA   |

### ApiVersion结构体信息

| 字段   | 类型          | 描述                     | 备注 |
| ------ | ------------- | ------------------------ | ---- |
| policy | String        | 标识结构体中的policy信息。 | NA   |
| value  | List\<String> | 标识结构体中的value信息。  | NA   |

### ScreenShape结构体信息

| 字段   | 类型          | 描述                     | 备注 |
| ------ | ------------- | ------------------------ | ---- |
| policy | String        | 标识结构体中的policy信息。 | NA   |
| value  | List\<String> | 标识结构体中的value信息。  | NA   |

### ScreenDensity结构体信息

| 字段   | 类型          | 描述                     | 备注 |
| ------ | ------------- | ------------------------ | ---- |
| policy | String        | 标识结构体中的policy信息。 | NA   |
| value  | List\<String> | 标识结构体中的value信息。  | NA   |

### ScreenWindow结构体信息

| 字段   | 类型          | 描述                     | 备注 |
| ------ | ------------- | ------------------------ | ---- |
| policy | String        | 标识结构体中的policy信息。 | NA   |
| value  | List\<String> | 标识结构体中的value信息。  | NA   |

### CountryCode结构体信息

| 字段   | 类型          | 描述                     | 备注 |
| ------ | ------------- | ------------------------ | ---- |
| policy | String        | 标识结构体中的policy信息。 | NA   |
| value  | List\<String> | 标识结构体中的value信息。  | NA   |
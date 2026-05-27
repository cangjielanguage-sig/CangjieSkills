### UncompressResult（Bundle信息）结构体信息

| 字段            | 类型               | 描述                                     | 备注 |
| ----------------| ------------------ |----------------------------------------| ---- |
| result          | boolean            | 标识此次解析是否成功。true表示解析成功，false表示解析失败。                             | NA   |
| message         | String             | 解析失败时返回失败原因。                            | NA   |
| packInfos       | List\<PackInfo>    | bundle中pack.info文件的packages信息。          | NA   |
| profileInfos    | List\<profileInfo> | 应用的配置信息。                                | NA   |
| profileInfosStr | List\<String>      | 应用的配置信息。 | NA   |
| icon            | String             | 返回入口组件的icon路径，如果没有入口组件，则返回第一个组件的icon信息。 | NA   |
| label           | String             | 返回入口组件的label，如果没有入口组件，则返回第一个组件的label信息。 | NA   |
| packageSize     | long               | 表示App包的大小，单位字节。 | NA   |

### PackInfo结构体信息

| 字段                | 类型          | 描述                                    | 备注 |
| ------------------- | ------------- | --------------------------------------- | ---- |
| name                | String        | 包名。                                    | NA   |
| moduleName          | String        | HAP名称。                                 | NA   |
| moduleType          | String        | module的类型。                            | NA   |
| deviceType          | List\<String> | 表示当前HAP包所支持的设备类型。           | NA   |
| deliveryWithInstall | boolean       | 标识当前HAP是否在用户主动安装的时候安装。true表示安装，false表示不安装。 | NA   |

### ProfileInfo结构体信息

| 字段         | 类型                           | 描述                                       | 备注                                                         |
| ------------ | ------------------------------ | ------------------------------------------ | ------------------------------------------------------------ |
| hapName      | String                         | 标识当前解析的HAP包名称。                    | NA                                                           |
| appInfo      | AppInfo结构体（见下述AppInfo） | 标识App信息的结构体（见下述AppInfo信息）。   | NA                                                           |
| deviceConfig | Map\<String,DeviceConfig>      | 标识设备信息。                               | 存储类型为Map\<String,String>，存储设备类型名称及对应设备类型的信息，在stage模型中，这个字段存储在app结构体中。 |
| hapInfo      | HapInfo结构体（见下述HapInfo）。 | 标识HAP包中module信息（见下述HapInfo信息）。 | NA                                                           |
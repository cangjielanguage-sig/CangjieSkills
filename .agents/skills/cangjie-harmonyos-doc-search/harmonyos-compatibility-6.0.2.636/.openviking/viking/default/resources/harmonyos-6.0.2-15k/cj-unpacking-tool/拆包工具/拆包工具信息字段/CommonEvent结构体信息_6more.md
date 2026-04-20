### CommonEvent结构体信息

| 字段   | 类型   | 描述    | 备注  |
| ------ | ------- | ---------- | -------- |
| name   | String        | 当前静态公共事件对应的类名。    | Stage模型从staticSubscriber类型的Extension中获取。 |
| permission | String        | 标识实现该静态公共事件需要申请的权限。   | Stage模型从staticSubscriber类型的Extension中获取。 |
| data       | List\<String> | 当前静态公共时间需要携带的额外数据数组。 | Stage模型从staticSubscriber类型的Extension中获取。 |
| type       | List\<String> | 配置当前静态公共时间的类别数组。         | Stage模型从staticSubscriber类型的Extension中获取。 |
| events     | List\<String> | 标识能够接收的意图的event值的集合。      | Stage模型从staticSubscriber类型的Extension中获取。 |

### DependencyItem结构体信息

| 字段           | 类型   | 描述           | 备注 |
|--------------| ------ |--------------| ---- |
| bundleName   | String | 共享包的bundleName。 | NA   |
| moduleName   | String | 共享包的moduleName。 | NA   |
| versionCode  | String | 共享包的版本号。      | NA   |

### ModuleAtomicService结构体信息

| 字段         | 类型                   | 描述           | 备注 |
|--------------|------------------------|----------------| ---- |
| preloadItems | list\<PreloadItem>     | 预加载对象。     | NA   |

### PreloadItem结构体信息

| 字段         | 类型   | 描述           | 备注 |
|--------------|--------|----------------| ---- |
| moduleName   | String | 预加载的模块名。 | NA   |

### DeviceConfig结构体信息

| 字段                           | 类型    | 描述                                     | 备注 |
|--------------------------------|-------- |------------------------------------------| ---- |
| targetReqSdk                   | String  | 标识应用程序DeviceConfig的目标请求Sdk版本。  | NA   |
| compatibleReqSdk               | String  | 标识应用程序DeviceConfig的兼容请求Sdk版本。  | NA   |
| jointUserid                    | String  | 标识应用程序DeviceConfig的jointUserid。      | NA   |
| process                        | String  | 标识应用程序DeviceConfig的进程。             | NA   |
| arkFlag                        | String  | 标识应用程序DeviceConfig的arkFlag。          | NA   |
| targetArkVersion               | String  | 标识应用程序DeviceConfig的targetArkVersion。 | NA   |
| compatibleArkVersion           | String  | 标识应用程序DeviceConfig的兼容ArkVersion。   | NA   |
| directLaunch                   | boolean | 标识应用程序DeviceConfig的直接启动。         | NA   |
| distributedNotificationEnabled | boolean | 标识应用程序AppJson的distributedNotificationEnabled。true表示开启分布式通知，false表示不开启分布式通知。 | NA   |

### DefPermission结构体信息

| 字段           | 类型                     | 描述                                      | 备注 |
|----------------|--------------------------|-------------------------------------------| ---- |
| name           | String                   | 标识指示DefPermission的名称。               | NA   |
| grantMode      | String                   | 标识DefPermission的grantMode。              | NA   |
| group          | String                   | 标识DefPermission的组。                     | NA   |
| label          | String                   | 标识DefPermission的标签。                   | NA   |
| description    | String                   | 标识DefPermission的描述。                   | NA   |
| availableScope | List\<String>            | 标识DefPermission的可用范围。               | NA   |
| labels         | HashMap\<String, String> | 标识多语言应用程序DefPermission的标签。     | NA   |
| descriptions   | HashMap\<String, String> | 标识多语言应用程序DefPermission的说明。     | NA   |
### AppInfo结构体信息

| 字段                           | 类型     | 描述                      | 备注         |
|--------------------------------|---------|---------------------------|-------------|
| bundleName                     | String  | 标识App的包名称。          | NA          |
| vendor                         | String  | 标识App的供应商信息。       | NA          |
| relatedBundleName              | String  | 标识App相关bundle的包名。   | NA          |
| versionName                    | String  | 标识App中的versionName信息。       | NA          |
| versionCode                    | String  | 标识App中的versionCode信息。  | NA          |
| targetApiVersion               | int     | 标识应用运行需要的API目标版本。    | NA          |
| compatibleApiVersion           | int     | 标识应用兼容的API版本。    | NA          |
| appName                        | String  | 标识显示在桌面上的ability的label。      | NA          |
| appNameEN                      | String  | 标识显示在桌面上的ability的label。    | NA          |
| releaseType                    | String  | 标识应用运行需要的API目标版本的类型。 | NA          |
| shellVersionCode               | String  | 标识应用的API版本号。 | NA          |
| shellVersionName               | String  | 标识应用的API版本名称。  | NA          |
| multiFrameworkBundle           | boolean | 标识应用框架。true表示混合打包，false表示非混合打包。   | NA          |
| debug                          | boolean | 标识应用是否可调试。true表示可调试，false表示不可调试。     | NA          |
| icon                           | String  | 标识应用的图标路径。 | NA          |
| label                          | String  | 标识应用的label。  | NA          |
| description                    | String  | 标识应用的描述信息。    | stage模型新增。   |
| minCompatibleVersionCode       | int     | 标识应用能够兼容的最低版本号。  | NA          |
| distributedNotificationEnabled | boolean | 标记该应用是否开启分布式通知。true表示开启，false表示不开启。   | stage模型新增。   |
| bundleType                     | String  | 标识bundle的类型，取值：<br/>- app：应用。<br/>- atomicService：原子化服务。 <br/>- shared：应用间共享库。 | NA   |
| compileSdkVersion              | String  | 标识编译该应用时使用的sdk版本。                                                              | 仅限API10及以后的应用。   |
| compileSdkType                 | String  | 标识编译该应用时使用的sdk类别。                                                              | 仅限API10及以后的应用。   |
| labels                         | HashMap\<String, String> | 标识多语言应用程序AppJson的标签。 | NA          |
| descriptions                   | HashMap\<String, String> | 标识多语言应用程序AppJson的说明。 | NA          |
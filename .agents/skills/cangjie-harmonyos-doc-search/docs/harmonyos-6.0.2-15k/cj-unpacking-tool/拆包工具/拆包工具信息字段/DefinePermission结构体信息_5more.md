### DefinePermission结构体信息

| 字段      | 类型  | 描述   | 备注 |
|------------------------|--------------------------|----------------------------------------------------| ---- |
| name                   | String                   | 标识DefinePermission的名称。                         | NA   |
| grantMode              | String                   | 标识DefinePermission的grantMode。                        | NA   |
| availableLevel         | String                   | 标识DefinePermission的组。                               | NA   |
| provisionEnable        | boolean                  | 标识模块定义权限的提供启用。true表示支持证书方式申请权限，false不支持证书方式申请权限。                           | NA   |
| distributedSceneEnable | boolean                  | 标识ModuleDefinePermissions的distributedSceneEnable。true表示支持分布式场景下使用该权限，false表示不支持分布式场景下使用该权限。 | NA   |
| label                  | String                   | 标识DefinePermission的标签。                              | NA   |
| description            | String                   | 标识DefinePermission的描述。                              | NA   |
| descriptions           | HashMap\<String, String> | 标识多语言应用程序DefinePermission的说明。                | NA   |
| labels                 | HashMap\<String, String> | 标识多语言应用程序DefinePermission的标签。                | NA   |

### DefPermissionsGroups结构体信息

| 字段        | 类型    | 描述                         | 备注 |
|-------------|---------|------------------------------| ---- |
| name        | String  | 标识DefPermissionGroup的名称。 | NA   |
| order       | String  | 标识DefPermissionGrou的顺序。  | NA   |
| icon        | String  | 标识DefPermissionGroup的图标。 | NA   |
| label       | String  | 标识DefPermissionGroup的标签。 | NA   |
| description | String  | 标识DefPermissionGroup的描述。 | NA   |
| request     | boolean | 标识DefPermissionGroup的请求。 | NA   |

### FormInfo结构体信息

| 字段          | 类型          | 描述                     | 备注 |
|---------------|---------------|--------------------------| ---- |
| formEntity    | List\<String> | 标识formInfo的formEntity。 | NA   |
| minHeight     | String        | 标识formInfo的最小高度。   | NA   |
| defaultHeight | String        | 标识formInfo的默认高度。   | NA   |
| minWidth      | String        | 标识formInfo的最小宽度。   | NA   |
| defaultWidth  | String        | 标识formInfo的默认宽度。   | NA   |

### ModuleMetadataInfo结构体信息

| 字段     | 类型    | 描述                         | 备注 |
|----------|---------|------------------------------| ---- |
| name     | String  | 标识ModuleMetadataInfo的名称。 | NA   |
| value    | String  | 标识ModuleMetadataInfo的值。   | NA   |
| resource | String  | 标识ModuleMetadataInfo的资源。 | NA   |

### ModuleWindowInfo结构体信息

| 字段            | 类型    | 描述                                | 备注 |
|-----------------|---------|-------------------------------------| ---- |
| designWidth     | int     | 标识模块已用场景的设计宽度。           | NA   |
| autoDesignWidth | boolean | 标识ModuleUsedScene的autoDesignWidth。 | NA   |
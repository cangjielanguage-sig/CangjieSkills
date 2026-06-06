## definePermissions标签

该标签仅支持系统资源hap定义权限，不支持应用自定义权限。权限定义方式参见[系统资源权限定义](https://gitee.com/openharmony/utils_system_resources/blob/master/systemres/main/config.json)。

**表26** definePermissions标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| -------- | -------- | -------- | -------- |
| name | 标识权限的名称，该标签最大长度为255字节。 | 字符串 | 不可缺省。 |
| grantMode | 标识权限的授予方式，支持如下两种授予模式如下：<br/>-&nbsp;system_grant：安装后系统自动授予该权限。<br/>-&nbsp;user_grant：使用时动态申请，用户授权后才可使用。 | 字符串 | 可缺省，缺省值为system_grant。 |
| availableLevel | 标识权限限制类别，可选值如下：<br/>-&nbsp;system_core：系统核心权限。<br/>-&nbsp;system_basic：系统基础权限。<br/>-&nbsp;normal：普通权限。所有应用允许申请的权限。 | 字符串 | 可缺省，缺省值为normal。 |
| provisionEnable | 标识权限是否支持证书方式申请权限，包括高级别的权限。配置为true表示开发者可以通过证书方式申请权限。配置为false表示开发者不可以通过证书方式申请权限。 | 布尔值 | 可缺省，缺省值为true。 |
| distributedSceneEnabled | 标识权限是否支持分布式场景下使用该权限。配置为true表示开发者可以在分布式场景下使用该权限。配置为false表示开发者不可以在分布式场景下使用该权限。 | 布尔值 | 可缺省，缺省值为false。 |
| label | 标识权限的简短描述，配置为对描述内容的资源索引。 | 字符串 | 可缺省，缺省值为空。 |
| description | 标识权限的详细描述，可以是字符串，或者是对描述内容的资源索引。 | 字符串 | 可缺省，缺省值为空。 |

definePermissions标签示例：

```json
{
  "module" : {
    "definePermissions": [
      {
        "name": "ohos.abilitydemo.permission.PROVIDER",
        "grantMode": "system_grant",
        "availableLevel": "system_core",
        "provisionEnable": true,
        "distributedSceneEnable": false,
        "label": "$string:EntryAbility_label"
      }
    ]
  }
}
```

<!--DelEnd-->
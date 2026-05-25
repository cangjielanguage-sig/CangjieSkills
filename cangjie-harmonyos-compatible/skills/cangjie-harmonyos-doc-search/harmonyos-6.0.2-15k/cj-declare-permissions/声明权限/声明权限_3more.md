# 声明权限

应用在申请权限时，需要在项目的配置文件中，逐个声明需要的权限，否则应用将无法获取授权。

## 在配置文件中声明权限

应用需要在module.json5配置文件的requestPermissions标签中声明权限。

| 属性 | 含义 | 数据类型 | 取值范围 |
| :-------- | :-------- | :-------- | :-------- |
| name | 需要使用的权限名称。 | 字符串 | **必填**，需为系统已定义的权限，取值范围请参见[应用权限列表](./cj-permissions-for-all.md)|
| reason | 申请权限的原因。 | 字符串 | **可选填写**，该字段用于应用上架校验，当申请的权限为user_grant权限时必填，并且需要进行多语种适配。<br>使用string类资源引用。格式为$string: \*\*\*。<br/>请参见[权限使用理由的文案内容规范](#权限使用理由的文案内容规范)。 |
| usedScene | 权限使用的场景，该字段用于应用上架校验。包括abilities和when两个子项。<br/>- abilities：使用权限的UIAbility或者ExtensionAbility组件的名称。<br/>- when：调用时机。 | 对象 | usedScene**必填**。<br/>- abilities：**可选填写**，可以配置为多个UIAbility或者ExtensionAbility名称的字符串数组。<br/>- when：**可选填写**，但如果配置此字段，只能填入固定值inuse（使用时）、always（始终），不能为空。<br/>当申请的权限为user_grant权限时建议填写。 |

> **说明：**
>
> 已在子模块中申请的权限，无需在主项目重复添加，权限将在整个应用生效。

## 声明样例

> **说明：**
>
> 以下"ohos.permission.PERMISSION1"、"ohos.permission.PERMISSION2"仅为样例示意，不存在该权限。请开发者根据实际需要，参照上表要求填写对应属性。

```json
// src/main/resources/base/element/string.json
{
  "string": [
    // ...
    {
      "name": "reason",
      "value": "reason_for_permission"
    }
  ]
}
```

```json
// src/main/module.json5
{
  "module" : {
    // ...
    "requestPermissions":[
      {
        "name" : "ohos.permission.PERMISSION1",
        "reason": "$string:reason",
        "usedScene": {
          "abilities": [
            "EntryAbility"
          ],
          "when":"inuse"
        }
      },
      {
        "name" : "ohos.permission.PERMISSION2",
        "reason": "$string:reason",
        "usedScene": {
          "abilities": [
            "EntryAbility"
          ],
          "when":"always"
        }
      }
    ]
  }
}
```
## shortcuts标签

shortcuts标识应用的快捷方式信息。标签值为数组，包含四个子标签shortcutId、label、icon、wants。

metadata中指定shortcut信息，其中：

- name：指定shortcuts的名称，使用ohos.ability.shortcuts作为shortcuts信息的标识。

- resource：指定shortcuts信息的资源位置。

**表10** shortcuts标签说明

| 属性名称 | 含义 | 类型  | 是否可缺省 |
| -------- | -------- | -------- | -------- |
| shortcutId | 标识快捷方式的ID，取值为长度不超过63字节的字符串。**不支持通过资源索引的方式（$string）配置该字段。** | 字符串 | 该标签不可缺省。 |
| label | 标识快捷方式的标签信息，即快捷方式对外显示的文字描述信息。取值为长度不超过255字节的字符串，可以是描述性内容，也可以是标识label的资源索引。 | 字符串 | 该标签可缺省，缺省值为空。 |
| icon | 标识快捷方式的图标，取值为资源文件的索引。 | 字符串 | 该标签可缺省，缺省值为空。 |
| [wants](#wants标签) | 标识快捷方式内定义的目标wants信息集合，在调用launcherBundleManager的startShortcut接口时，会拉起wants标签里的第一个目标组件，推荐只配置一个wants元素。 | 对象 | 该标签可缺省，缺省为空。 |

1. 在/resources/base/profile/目录下配置shortcuts_config.json配置文件。

   ```json
   {
     "shortcuts": [
       {
         "shortcutId": "id_test1",
         "label": "$string:shortcut",
         "icon": "$media:aa_icon",
         "wants": [
           {
             "bundleName": "com.ohos.hello",
             "moduleName": "entry",
             "abilityName": "EntryAbility",
             "parameters": {
               "testKey": "testValue"
             }
           }
         ]
       }
     ]
   }
   ```

2. 在module.json5配置文件的abilities标签中，针对需要添加快捷方式的UIAbility进行配置metadata标签，使shortcut配置文件对该UIAbility生效。

   ```json
   {
     "module": {
       // ...
       "abilities": [
         {
           "name": "EntryAbility",
           "srcEntry": "ohos_app_cangjie_entry.MainAbility",
           // ...
           "skills": [
             {
               "entities": [
                 "entity.system.home"
               ],
               "actions": [
                 "ohos.want.action.home"
               ]
             }
           ],
           "metadata": [
             {
               "name": "ohos.ability.shortcuts",
               "resource": "$profile:shortcuts_config"
             }
           ]
         }
       ]
     }
   }
   ```

### wants标签

此标签用于标识快捷方式内定义的目标wants信息集合。

**表11** wants标签说明

| 属性名称 | 含义 | 类型  | 是否可缺省 |
| -------- | -------- | -------- | -------- |
| bundleName | 表示快捷方式的目标包名。 | 字符串 | 该标签不可缺省。 |
| moduleName | 表示快捷方式的目标模块名。 | 字符串 | 该标签可缺省。 |
| abilityName| 表示快捷方式的目标组件名。 | 字符串 | 该标签不可缺省。 |
| parameters | 表示拉起快捷方式时的自定义数据，仅支持配置字符串类型的数据。其中键值均最大支持1024长度的字符串。 | 对象 | 该标签可缺省。 |

data标签示例：

```json
{
  "wants": [
    {
      "bundleName": "com.ohos.hello",
      "moduleName": "entry",
      "abilityName": "EntryAbility",
      "parameters": {
        "testKey": "testValue"
      }
    }
  ]
}
```
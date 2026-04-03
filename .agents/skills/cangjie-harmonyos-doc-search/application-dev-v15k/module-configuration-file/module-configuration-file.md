# module.json5配置文件

## metadata标签

该标签标识HAP的自定义元信息，标签值为数组类型，包含name、value、resource三个子标签。

**表1** metadata标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| :-------- | :-------- | :-------- | :-------- |
| name | 标识数据项的名称，取值为长度不超过255字节的字符串。 | 字符串 | 该标签可缺省，缺省值为空。 |
| value | 标识数据项的值，取值为长度不超过255字节的字符串。 | 字符串 | 该标签可缺省，缺省值为空。 |
| resource | 标识定义用户自定义数据格式，取值为长度不超过255字节的字符串，内容为标识该数据的资源索引。| 字符串 | 该标签可缺省，缺省值为空。 |

resource属性值使用“$profile:文件名”的方式指定文件所在位置，$profile表示资源的路径为工程中的/resources/base/profile目录下。例如$profile:shortcuts_config指定了/resources/base/profile/shortcuts_config.json文件。

```json
{
  "module": {
    "metadata": [{
      "name": "module_metadata",
      "value": "a test demo for module metadata",
      "resource": "$profile:shortcuts_config"
    }],

    "abilities": [{
      "metadata": [{
        "name": "ability_metadata",
        "value": "a test demo for ability",
        "resource": "$profile:config_file"
      },
      {
        "name": "ability_metadata_2",
        "value": "a string test",
        "resource": "$profile:config_file"
      }],
    }],

    "extensionAbilities": [{
      "metadata": [{
        "name": "extensionAbility_metadata",
        "value": "a test for extensionAbility",
        "resource": "$profile:config_file"
      },
      {
        "name": "extensionAbility_metadata_2",
        "value": "a string test",
        "resource": "$profile:config_file"
      }],
    }]
  }
}
```

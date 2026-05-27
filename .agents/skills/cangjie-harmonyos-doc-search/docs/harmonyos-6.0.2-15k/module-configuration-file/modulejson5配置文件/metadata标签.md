## metadata标签

该标签标识HAP的自定义元信息，标签值为数组类型，包含name、value、resource三个子标签。

**表5** metadata标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| -------- | -------- | -------- | -------- |
| name | 标识数据项的名称，取值为长度不超过255字节的字符串。 | 字符串 | 该标签可缺省，缺省值为空。 |
| value | 标识数据项的值，取值为长度不超过255字节的字符串。 | 字符串 | 该标签可缺省，缺省值为空。 |
| resource | 标识了用户自定义数据，取值为长度不超过255字节的字符串，内容为该数据的资源索引，例如配置成$profile:shortcuts_config，表示指向了/resources/base/profile/shortcuts_config.json配置文件。| 字符串 | 该标签可缺省，缺省值为空。 |

下面给出两种metadata标签的使用场景及示例，开发者也可以根据实际需求自定义设置。

1. 使用metadata标签配置主窗口的默认大小和位置（单位为vp）。其中name取值及对应含义如下：

    - name取值为ohos.ability.window.height表示主窗口的默认高度，value表示高度大小。
    - name取值为ohos.ability.window.width表示主窗口的默认宽度，value表示宽度大小。
    - name取值为ohos.ability.window.left表示主窗口默认左边的位置。value表示配置格式，取值：对齐方式 +/- 偏移量。对齐方式包括center、left和right，默认值为left；当偏移量为0时可以省略。
    - name取值为ohos.ability.window.top表示主窗口顶部的位置。value表示配置格式，取值：对齐方式 +/- 偏移量。对齐方式包括center、top和bottom，默认值为top。如果对齐方式和偏移量同时省略，则按照系统默认的层叠规格处理。

2. 使用metadata标签配置是否移除启动页。配置项为：name取值为enable.remove.starting.window，value取值为true或false，取值为true表示移除启动页、取值为false表示不移除启动页，未配置时默认为false。

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
      },
      {
        "name": "ohos.ability.window.height",
        "value": "987"
      },
      {
        "name": "ohos.ability.window.width",
        "value": "1300"
      },
      {
        "name": "ohos.ability.window.left",
        "value": "right-50"
      },
      {
        "name": "ohos.ability.window.top",
        "value": "center+50"
      },
      {
        "name": "enable.remove.starting.window",
        "value": "true"
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
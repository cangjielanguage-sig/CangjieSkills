## appEnvironments标签

此标签标识应用配置的环境变量。应用运行时有时会依赖一些三方库，这些三方库会使用到一些自定义的环境变量，为了不修改三方库的实现逻辑，可以在工程的配置文件中设置自定义的环境变量，以供运行时使用。

**表2** appEnvironments标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| -------- | -------- | -------- | -------- |
| name | 标识环境变量的变量名称。取值为长度不超过4096字节的字符串。 | 字符串  | 该标签可缺省，缺省值为空。 |
| value         | 标识环境变量的值。取值为长度不超过4096字节的字符串。       | 字符串  | 该标签可缺省，缺省值为空。 |

appEnvironments标签示例：

```json
{
  "app": {
    "appEnvironments": [
      {
        "name":"name1",
        "value": "value1"
      }
    ]
  }
}
```

## multiAppMode标签

应用多开模式。

**表3** multiAppMode标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| -------- | -------- | -------- | -------- |
| multiAppModeType | 标识应用多开模式类型，支持的取值如下：<br/>-&nbsp;multiInstance：多实例模式。该字段仅支持2in1设备，常驻进程不支持该字段。<br/>-&nbsp;appClone：应用分身模式。 | 字符串  | 该标签不可缺省。 |
| maxCount | 标识最大允许的应用多开个数，支持的取值如下：<br/>-&nbsp;multiInstance模式：取值范围1\~10。<br/>-&nbsp;appClone模式：取值范围1\~5。      | 数值  | 该标签不可缺省。 |

multiAppMode标签示例：

```json
{
  "app": {
    "multiAppMode": {
      "multiAppModeType": "appClone",
      "maxCount": 5
    }
  }
}
```

## configuration标签

该标签是一个profile文件资源，用于指定描述应用字体大小跟随系统变更的配置文件。

configuration标签示例：

```json
{
  "app": {
    "configuration": "$profile:configuration"  
  }
}
```

在开发视图的AppScope/resources/base/profile下面定义配置文件configuration.json，其中文件名"configuration"可自定义，需要和configuration标签指定的信息对应。配置文件中列举了当前应用字体大小跟随系统变化的属性。

**表4** configuration标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| -------- | -------- | -------- | -------- |
| fontSizeScale | 应用字体大小是否跟随系统，支持的取值如下：<br/>-&nbsp;followSystem：跟随系统。<br/>-&nbsp;nonFollowSystem：不跟随系统。| 字符串 | 该标签可缺省，缺省值为nonFollowSystem。 |
| fontSizeMaxScale | 应用字体大小选择跟随系统后，相比系统字体的最大比例，支持的取值为：1、1.15、1.3、1.45、1.75、2、3.2。  <br/> 例如配置最大比例为1.75，系统字体默认大小为10fp。<br/>（1）如果设置中调整系统大小为1.5倍，此时系统的实际字体大小为15fp，应用会跟随系统字体一起调整为15fp。<br/>（2）如果设置中调整系统大小为2倍，此时系统的字体大小为20fp，但由于应用配置的跟随系统的最大比例为1.75，所以此时应用的字体大小为17.5fp。 <br/> **说明**<br/> fontSizeScale为nonFollowSystem时，该项不生效。 | 字符串 | 该标签可缺省，缺省值为3.2。 |

configuration标签示例：

```json
{
  "configuration": {
    "fontSizeScale": "followSystem",
    "fontSizeMaxScale": "3.2"
  }
}
```
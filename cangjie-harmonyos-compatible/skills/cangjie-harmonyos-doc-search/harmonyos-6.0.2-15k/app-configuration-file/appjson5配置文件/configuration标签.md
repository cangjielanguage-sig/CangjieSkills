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
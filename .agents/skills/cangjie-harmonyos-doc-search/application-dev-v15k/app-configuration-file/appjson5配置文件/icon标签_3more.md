## icon标签

此标签标识[应用的图标](../../application-models/cj-application-component-configuration-stage.md)和对分层图标配置文件的索引。

分层图标的配置方式如下：

1. 将图标的前景资源和背景资源放在AppScope/resources/base/media目录下，或使用目录下默认存放的前景资源和背景资源。

2. 上述media目录下存在一个分层图标配置文件（layered_image.json），在文件中引用前景资源和背景资源，详见[图标资源规范](https://developer.huawei.com/consumer/cn/doc/design-guides/application-icon-0000001953444009#section634668113212)。

分层图标配置文件示例：

```json
{
  "layered-image"：
    {
      "background":"$media:background", //背景资源
      "foreground":"$media:foreground" //前景资源
    }
}
```

icon标签示例：

```json
{
  "app":{
    "icon":"$media:layered_image"
  }
}
```

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
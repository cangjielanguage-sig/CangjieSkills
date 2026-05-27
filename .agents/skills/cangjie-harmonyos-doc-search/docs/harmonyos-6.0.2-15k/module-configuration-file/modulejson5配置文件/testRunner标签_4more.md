## testRunner标签

此标签用于支持对测试框架的配置。

**表17** testRunner标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| -------- | -------- | -------- | -------- |
| name | 标识测试框架对象名称，取值为长度不超过255字节的字符串。 | 字符串 | 不可缺省。 |
| srcPath | 标识测试框架代码路径，取值为长度不超过255字节的字符串。 | 字符串 | 不可缺省。 |

testRunner标签示例：

```json
{
  "module": {
    // ...
    "testRunner": {
      "name": "myTestRunnerName",
      "srcPath": "etc/test/TestRunner.ts"
    }
  }
}
```

## dependencies标签

此标签标识模块运行时依赖的共享库列表。

**表18** dependencies标签说明

| 属性名称    | 含义  | 数据类型 | 是否可缺省 |
| ----------- | ------------------------------ | -------- | ---------- |
| bundleName  | 标识当前模块依赖的共享包包名。取值为长度7~128字节的字符串。 | 字符串   | 该标签可缺省，缺省值为空。 |
| moduleName  | 标识当前模块依赖的共享包模块名。取值为长度不超过31字节的字符串。 | 字符串   | 该标签不可缺省。 |
| versionCode | 标识当前模块依赖的共享包的版本号。取值范围为0~2147483647。 | 数值 | 该标签可缺省，缺省值为空。 |

dependencies标签示例：

```json
{
  "module": {
    "dependencies": [
      {
        "bundleName":"com.share.library",
        "moduleName": "library",
        "versionCode": 10001
      }
    ]
  }
}
```

## proxyData标签

此标签标识模块提供的数据代理列表，仅限entry和feature配置。

**表19** proxyData标签说明

| 属性名称    | 含义  | 数据类型 | 是否可缺省 |
| ----------- | ------------------------------ | -------- | ---------- |
| uri | 标识用于访问该数据代理的URI，不同的数据代理配置的URI不可重复，且需要满足`datashareproxy://当前应用包名/xxx`的格式。取值为长度不超过255字节的字符串。 | 字符串   | 该标签不可缺省。 |
| requiredReadPermission  | 标识从该数据代理中读取数据所需要的权限。若不配置，则其他应用无法使用该代理。非系统应用配置的权限的等级需为system_basic或system_core，系统应用配置的权限的等级没有限制。权限等级可以参考[权限列表](../../security/AccessToken/cj-app-permissions.md)。取值为长度不超过255字节的字符串。 | 字符串   | 该标签可缺省，缺省值为空。 |
| requiredWritePermission | 标识向该数据代理中写入数据所需要的权限。若不配置，则其他应用无法使用该代理。非系统应用配置的权限的等级需为system_basic或system_core，系统应用配置的权限的等级没有限制。权限等级可以参考[权限列表](../../security/AccessToken/cj-app-permissions.md)。取值为长度不超过255字节的字符串。 | 字符串   | 该标签可缺省，缺省值为空。 |
| [metadata](#metadata标签) | 标识该数据代理的元信息，只支持配置name和resource字段。 | 对象 | 该标签可缺省，缺省值为空。 |

proxyData标签示例：

```json
{
  "module": {
    "proxyData": [
      {
        "uri":"datashareproxy://com.ohos.datashare/event/Meeting",
        "requiredReadPermission": "ohos.permission.GET_BUNDLE_INFO",
        "requiredWritePermission": "ohos.permission.GET_BUNDLE_INFO",
        "metadata": {
          "name": "datashare_metadata",
          "resource": "$profile:datashare"
        }
      }
    ]
  }
}
```

## appEnvironments标签

此标签标识模块配置的应用环境变量。

**表20** appEnvironments标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| -------- | -------- | -------- | -------- |
| name | 标识环境变量的变量名称。取值为长度不超过4096字节的字符串。 | 字符串  | 该标签可缺省，缺省值为空。 |
| value  | 标识环境变量的值。取值为长度不超过4096字节的字符串。   | 字符串  | 该标签可缺省，缺省值为空。 |

appEnvironments标签示例：

```json
{
  "module": {
    "appEnvironments": [
      {
        "name":"name1",
        "value": "value1"
      }
    ]
  }
}
```
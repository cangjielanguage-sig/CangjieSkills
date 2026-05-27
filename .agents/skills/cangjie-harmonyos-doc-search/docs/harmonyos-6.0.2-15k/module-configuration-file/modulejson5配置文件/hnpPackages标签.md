## hnpPackages标签

该标签标识应用包含的Native软件包信息。

**表21** hnpPackages标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| -------- | -------- | -------- | -------- |
| package | 标识Native软件包名称。 | 字符串 | 该标签不可缺省。 |
| type | 标识Native软件包类型。支持的取值如下：<br/>-&nbsp;public：公有类型。<br/>-&nbsp;private：私有类型。  | 字符串 | 该标签不可缺省。 |

hnpPackages示例：

```json
{
  "module" : {
    "hnpPackages": [
      {
        "package": "hnpsample.hnp",
        "type": "public"
      }
    ]
  }
}
```
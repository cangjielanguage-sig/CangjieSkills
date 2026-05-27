## skills标签

该标签标识UIAbility组件或者ExtensionAbility组件能够接收的[Want](../../application-models/cj-want-overview.md)的特征。

**表7** skills标签说明

| 属性名称 | 含义 | 数据类型 | 是否可缺省 |
| -------- | -------- | -------- | -------- |
| actions | 标识能够接收的Action值集合，取值通常为系统预定义的action值，也允许自定义。<br>一个skill中不建议配置多个action，否则可能导致无法匹配预期场景。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| entities | 标识能够接收的Entity值的集合。<br>一个skill中不建议配置多个entity，否则可能导致无法匹配预期场景。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| uris | 标识与Want中URI（Uniform&nbsp;Resource&nbsp;Identifier）相匹配的集合。数组允许的最大数量为512。 | 对象数组 | 该标签可缺省，缺省值为空。 |
| permissions | 标识当前UIAbility组件自定义的权限信息。其他应用访问该UIAbility时，需要申请相应的权限信息。<br/>一个数组元素为一个权限名称，权限名称采用反向域名格式（不超过255字节），取值为系统预定义的权限。 | 字符串数组 | 该标签可缺省，缺省值为空。 |
| domainVerify | 标识是否开启域名校验。<br/>-&nbsp;true：表示开启域名校验。<br/>-&nbsp;false：表示不开启域名校验。 | 布尔值 | 该标签可缺省，缺省值为false。 |

**表8** uris标签说明

> **说明：**
>
> 以下字符串类型的字段不支持使用资源索引的方式（$string）配置。

| 属性名称 | 含义  | 数据类型 | 是否可缺省 |
| -------- |-----------------| -------- | -------- |
| scheme | 标识URI的协议名部分，常见的有http、https、file、ftp等。<br/>**说明：**<br/>从API 18开始，该字段在参与隐式Want匹配时不区分大小写。   | 字符串 | uris中仅配置type时可以缺省，缺省值为空，否则不可缺省。 |
| host | 标识URI的主机地址部分，该字段只有当scheme配置时才生效。常见的方式：<br/>-&nbsp;域名方式，如example.com。<br/>-&nbsp;IP地址方式，如10.10.10.1。<br/>**说明：**<br/>从API 18开始，该字段在参与隐式Want匹配时不区分大小写。   | 字符串 | 该标签可缺省，缺省值为空。 |
| port | 标识URI的端口部分。如http默认端口为80，https默认端口是443，ftp默认端口是21。该字段只有当scheme和host都配置时才生效。  | 字符串 | 该标签可缺省，缺省值为空。 |
| path&nbsp;\| &nbsp;pathStartWith&nbsp;\|&nbsp;pathRegex | 标识URI的路径部分，path、pathStartWith和pathRegex配置时三选一。path标识URI与want中的路径部分全匹配，pathStartWith标识URI与want中的路径部分允许前缀匹配，pathRegex标识URI与want中的路径部分允许正则匹配。该字段只有当scheme和host都配置时才生效。 | 字符串 | 该标签可缺省，缺省值为空。 |
| type | 标识与Want相匹配的数据类型，使用MIME（Multipurpose&nbsp;Internet&nbsp;Mail&nbsp;Extensions）类型规范和[UniformDataType](../../../API_Reference/source_zh_cn/apis/ArkData/cj-apis-uniformTypeDescriptor.md)类型规范。可以与scheme同时配置，也可以单独配置。 | 字符串 | 该标签可缺省，缺省值为空。 |
| utd | 标识与Want相匹配的[标准化数据类型](../../database/cj-uniform-data-type-descriptors.md)，适用于分享等场景。   | 字符串 | 该标签可缺省，缺省值为空。 |
| maxFileSupported | 对于指定类型的文件，标识一次能接收或打开的最大数量，适用于分享等场景，需要与utd配合使用。    | 整数 | 该标签可缺省，缺省值为0。|
| linkFeature | 标识URI提供的功能类型（如文件打开、分享、导航等），用于实现应用间跳转。取值为长度不超过127字节的字符串，不支持中文。同一Bundle中声明的linkFeature数量不能超过150个。详情见[linkFeature标签说明](../../application-models/cj-app-uri-config.md#linkfeature标签说明)。 | 字符串 | 该标签可缺省，缺省值为空。|

skills示例：
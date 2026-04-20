### static func removeAdsBlockAllowedList(Array\<String>)

```cangjie
public static func removeAdsBlockAllowedList(domainSuffixes: Array<String>): Unit
```

**功能：** 从AdsBlockManager的AllowedList中删除一组域名。

> **说明：**
>
> - AdsBlockManager的AllowedList不会持久化，应用重启需要重新设置。
> - 删除不存在的条目不会触发异常。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|domainSuffixes|Array\<String>|是|-|一组域名列表，例如['example.com', 'abcd.efg.com']。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|

### static func removeAdsBlockDisallowedList(Array\<String>)

```cangjie
public static func removeAdsBlockDisallowedList(domainSuffixes: Array<String>): Unit
```

**功能：** 从AdsBlockManager的DisallowedList中删除一组域名。

> **说明：**
>
> - AdsBlockManager的DisallowedList不会持久化，应用重启需要重新设置。
> - 删除不存在的条目不会触发异常。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|domainSuffixes|Array\<String>|是|-|一组域名列表，例如['example.com', 'abcd.efg.com']。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|

### static func setAdsBlockRules(String, Bool)

```cangjie
public static func setAdsBlockRules(rulesFile: String, replace: Bool): Unit
```

**功能：** 向Web组件中设置自定义的符合通用EasyList语法规则的广告过滤配置文件。

> **说明：**
>
> 此接口设置的广告过滤规则，内部解析成功后会持久化存储，应用重启后不需要重复设置。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rulesFile|String|是|-|指定了符合EasyList通用语法的规则文件路径，应用需要有此文件的读权限。|
|replace|Bool|是|-|true表示强制替换掉内置的默认规则，false表示设置的自定义规则将与内置规则共同工作。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|
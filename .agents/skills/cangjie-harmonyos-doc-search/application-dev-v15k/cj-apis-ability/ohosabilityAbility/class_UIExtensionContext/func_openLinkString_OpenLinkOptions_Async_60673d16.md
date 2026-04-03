### func openLink(String, ?OpenLinkOptions, ?AsyncCallback\<AbilityResult>)

```cangjie
public func openLink(link: String, options!: ?OpenLinkOptions = None,
    callback!: ?AsyncCallback<AbilityResult> = None): Unit
```

**功能：** 通过AppLinking启动Ability，通过异步回调返回结果。仅支持在主线程调用。通过在link字段中传入标准格式的URL，基于隐式want匹配规则拉起目标Ability。目标方必须具备以下过滤器特征，才能处理AppLinking链接：

- "actions"列表中包含"ohos.want.action.viewData"。
- "entities"列表中包含"entity.system.browsable"。
- "uris"列表中包含"scheme"为"https"且"domainVerify"为true的元素。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|link|String|是|-|指示要打开的标准格式URL。|
|options|?[OpenLinkOptions](#class-openlinkoptions)|否|None| **命名参数。** 打开URL的选项参数。|
|callback|?[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<[AbilityResult](#struct-abilityresult)>|否|None| **命名参数。** 执行结果回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  | 201 | The application does not have permission to call the interface. |
  | 401 | Parameter error.  |
  | 16000001 | The specified ability does not exist. |
  | 16000002 | Incorrect ability type. |
  | 16000004 | Failed to start the invisible ability. |
  | 16000005 | The specified process does not have the permission. |
  | 16000006 | Cross-user operations are not allowed. |
  | 16000008 | The crowdtesting application expires. |
  | 16000009 | An ability cannot be started or stopped in Wukong mode. |
  | 16000010 | The call with the continuation flag is forbidden.        |
  | 16000011 | The context does not exist.        |
  | 16000012 | The application is controlled.        |
  | 16000013 | The application is controlled by EDM.       |
  | 16000019 | No matching ability is found. |
  | 16000069 | The extension cannot start the third party application. |
  | 16200001 | The caller has been released. |
  | 16000053 | The ability is not on the top of the UI. |
  | 16000082 | The UIAbility is being started. |
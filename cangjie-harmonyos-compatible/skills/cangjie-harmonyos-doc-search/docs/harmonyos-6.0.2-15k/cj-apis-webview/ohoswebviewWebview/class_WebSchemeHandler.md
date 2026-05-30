## class WebSchemeHandler

```cangjie
public class WebSchemeHandler {
    public init()
}
```

**功能：** 用于拦截指定scheme请求的拦截器。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### init()

```cangjie
public init()
```

**功能：** 构造一个WebSchemeHandler对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### func onRequestStart((WebSchemeHandlerRequest, WebResourceHandler) -> Bool)

```cangjie
public func onRequestStart(callback: (WebSchemeHandlerRequest, WebResourceHandler) -> Bool): Unit
```

**功能：** 当请求开始时的回调，在该回调函数中可以决定是否拦截该请求。

当回调返回false是表示不拦截此请求，此时handler失效；当回调返回true，表示拦截此请求。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([WebSchemeHandlerRequest](#class-webschemehandlerrequest),[WebResourceHandler](#class-webresourcehandler))->Bool|是|-|拦截对应scheme请求开始时触发的回调。request为请求，handler用于提供自定义的返回头以及返回体给Web组件，返回值表示该请求是否拦截。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|

### func onRequestStop((WebSchemeHandlerRequest) -> Unit)

```cangjie
public func onRequestStop(callback: (WebSchemeHandlerRequest) -> Unit): Unit
```

**功能：** 当请求完成时的回调。仅当[onRequestStart](#func-onrequeststartwebschemehandlerrequest-webresourcehandler---bool)中回调决定拦截此请求时触发。触发的时机有以下两种情况：

- WebResourceHandler调用didFail或者didFinish。

- 此请求因为其他原因中断。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([WebSchemeHandlerRequest](#class-webschemehandlerrequest))->Unit|是|-|对应请求结束的回调函数。|
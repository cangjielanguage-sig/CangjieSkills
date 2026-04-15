### class OnPermissionRequestEvent

```cangjie
public class OnPermissionRequestEvent {
    public var request: PermissionRequest
    public init(request: PermissionRequest)
}
```

**功能：** 描述通知收到获取权限请求的参数结构。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

#### var request

```cangjie
public var request: PermissionRequest
```

**功能：** Web组件返回授权或拒绝权限功能的对象。示例代码参考[onPermissionRequest](#class-onpermissionrequestevent)事件。

**类型：** [PermissionRequest](#class-permissionrequest)

**读写能力：** 可读写

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

#### init(PermissionRequest)

```cangjie

public init(request: PermissionRequest)
```

**功能：** 构造一个OnPermissionRequestEvent类型的对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|request|[PermissionRequest](#class-permissionrequest)|是|-|Web组件返回授权或拒绝权限功能的对象。|
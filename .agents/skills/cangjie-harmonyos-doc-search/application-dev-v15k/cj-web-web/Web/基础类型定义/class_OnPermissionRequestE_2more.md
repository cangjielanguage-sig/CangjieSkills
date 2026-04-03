### class OnPermissionRequestEvent

```cangjie
public class OnPermissionRequestEvent {
    public OnPermissionRequestEvent(
        public let request: PermissionRequest
    )
}
```

**功能：** 描述通知收到获取权限请求的参数结构。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### let request

```cangjie
public let request: PermissionRequest
```

**功能：** 通知Web组件用户操作行为。

**类型：** [PermissionRequest](#class-permissionrequest)

**读写能力：** 只读

**起始版本：** 19

#### OnPermissionRequestEvent(PermissionRequest)

```cangjie
public OnPermissionRequestEvent(
    public let request: PermissionRequest
)
```

**功能：** 定义通知收到获取权限请求。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|request|[PermissionRequest](#class-permissionrequest)|是|-|通知Web组件用户操作行为。|

### class OnPromptEvent

```cangjie
public class OnPromptEvent {
    public OnPromptEvent(
        public let url: String,
        public let message: String,
        public let value: String,
        public let result: WebResult
    )
}
```

**功能：** 描述网页调用prompt()告警时触发此回调参数结构。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### let message

```cangjie
public let message: String
```

**功能：** 弹窗中显示的信息。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

#### let result

```cangjie
public let result: WebResult
```

**功能：** 通知Web组件用户操作行为。

**类型：** [WebResult](#class-webresult)

**读写能力：** 只读

**起始版本：** 19

#### let url

```cangjie
public let url: String
```

**功能：** 当前显示弹窗所在网页的URL。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

#### let value

```cangjie
public let value: String
```

**功能：** 提示对话框的信息。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

#### OnPromptEvent(String, String, String, WebResult)

```cangjie
public OnPromptEvent(
    public let url: String,
    public let message: String,
    public let value: String,
    public let result: WebResult
)
```

**功能：** 定义网页调用prompt()告警时触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|当前显示弹窗所在网页的URL。|
|message|String|是|-|弹窗中显示的信息。|
|value|String|是|-|提示对话框的信息。|
|result|[WebResult](#class-webresult)|是|-|通知Web组件用户操作行为。|
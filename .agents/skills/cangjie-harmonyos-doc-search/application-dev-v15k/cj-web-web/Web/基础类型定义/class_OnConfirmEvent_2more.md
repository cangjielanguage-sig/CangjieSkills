### class OnConfirmEvent

```cangjie
public class OnConfirmEvent {
    public OnConfirmEvent(
        public let url: String,
        public let message: String,
        public let result: WebResult
    )
}
```

**功能：** 描述定义网页调用confirm()告警的参数结构。

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

#### OnConfirmEvent(String, String, WebResult)

```cangjie
public OnConfirmEvent(
    public let url: String,
    public let message: String,
    public let result: WebResult
)
```

**功能：** 定义网页调用confirm()告警时触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|当前显示弹窗所在网页的URL。|
|message|String|是|-|弹窗中显示的信息。|
|result|[WebResult](#class-webresult)|是|-|通知Web组件用户操作行为。|

### class OnConsoleEvent

```cangjie
public class OnConsoleEvent {
    public OnConsoleEvent(
        public let message: ConsoleMessage
    )
}
```

**功能：** 描述通知宿主应用JavaScript console消息参数结构。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### let message

```cangjie
public let message: ConsoleMessage
```

**功能：** 触发的控制台信息。

**类型：** [ConsoleMessage](#class-consolemessage)

**读写能力：** 只读

**起始版本：** 19

#### OnConsoleEvent(ConsoleMessage)

```cangjie
public OnConsoleEvent(
    public let message: ConsoleMessage
)
```

**功能：** 定义通知宿主应用JavaScript console消息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|[ConsoleMessage](#class-consolemessage)|是|-|触发的控制台信息。|
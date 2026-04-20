### class ScriptItem

```cangjie
public class ScriptItem {
    public ScriptItem(
        public var script: String,
        public var scriptRules: Array<String>
    )
}
```

**功能：** 描述通过[javaScriptOnDocumentStart](#func-javascriptondocumentstartarrayscriptitem)属性注入到Web组件的ScriptItem对象的参数结构。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### var script

```cangjie
public var script: String
```

**功能：** 需要注入、执行的JavaScript脚本。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

#### var scriptRules

```cangjie
public var scriptRules: Array<String>
```

**功能：** 一组允许来源的匹配规则。

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 19

#### ScriptItem(String, Array\<String>)

```cangjie
public ScriptItem(
    public var script: String,
    public var scriptRules: Array<String>
)
```

**功能：** 通过[javaScriptOnDocumentStart](#func-javascriptondocumentstartarrayscriptitem)属性注入到Web组件的ScriptItem对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|script|String|是|-|需要注入、执行的JavaScript脚本。|
|scriptRules|Array\<String>|是|-|一组允许来源的匹配规则。<br>1.如果需要允许所有来源的网址，使用通配符“ * ”。<br>2.如果需要精确匹配，则描述网站地址，如"https://www.example.com"。<br>3.如果模糊匹配网址，可以使用“ * ”通配符替代，如"https://*.example.com"。不允许使用"x. * .y.com"、" * foobar.com"等。<br>4.如果来源是ip地址，则使用规则2。<br>5.对于http/https以外的协议(自定义协议)，不支持使用精确匹配和模糊匹配，且必须以"://"结尾，例如"resource://"。<br>6.一组scriptRule中，如果其中一条不满足以上规则，则整组scriptRule都不生效。|

### class WebEvent

```cangjie
public class WebEvent {
    public WebEvent(
        public var url: String,
        public var message: String,
        public var value: String,
        public var result: WebResult
    )
}
```

**功能：** 描述Web组件弹窗时的回调信息的参数结构。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var message

```cangjie
public var message: String
```

**功能：** 弹窗中显示的信息。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

#### var result

```cangjie
public var result: WebResult
```

**功能：** 页面返回的信息。

**类型：** [WebResult](#class-webresult)

**读写能力：** 可读写

**起始版本：** 12

#### var url

```cangjie
public var url: String
```

**功能：** 当前弹窗所在页面的URL。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

#### var value

```cangjie
public var value: String
```

**功能：** 提示对话框的信息。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

#### WebEvent(String, String, String, WebResult)

```cangjie
public WebEvent(
    public var url: String,
    public var message: String,
    public var value: String,
    public var result: WebResult
)
```

**功能：** Web组件弹窗时的回调信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|当前弹窗所在页面的URL。|
|message|String|是|-|弹窗中显示的信息。|
|value|String|是|-|提示对话框的信息。|
|result|[WebResult](#class-webresult)|是|-|通知Web组件用户操作行为。|
### func javaScriptOnDocumentStart(Array\<ScriptItem>)

```cangjie
public func javaScriptOnDocumentStart(scripts: Array<ScriptItem>): This
```

**功能：** 注入JavaScript对象到window对象中，并在window对象中调用该对象的方法。

> **说明：**
>
> - 该脚本将在页面的任何JavaScript代码之前运行，并且DOM树此时可能尚未加载、渲染完毕。
> - 该脚本按照字典序执行，非数组本身顺序，若需数组本身顺序，建议使用runJavaScriptOnDocumentStart接口。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scripts|Array\<[ScriptItem](#class-scriptitem)>|是|-|需要注入的ScriptItem数组。|

### func javaScriptProxy(Array\<(String) -> String>, String, Array\<String>, WebviewController)

```cangjie
public func javaScriptProxy(funcList!: Array<(String)->String>, name!: String, methodList!: Array<String>, controller!: WebviewController): This
```

**功能：** 注入JavaScript对象到window对象中，并在window对象中调用该对象的方法。

> **说明：**
>
> - javaScriptProxy接口需要和deleteJavaScriptRegister接口配合使用，防止内存泄漏。
> - javaScriptProxy对象的所有参数不支持更新。
> - 注册对象时，同步与异步方法列表请至少选择一项不为空，可同时注册两类方法。
> - 此接口只支持注册一个对象，若需要注册多个对象请使用[registerJavaScriptProxy](../apis/ArkWeb/cj-apis-webview.md)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|funcList|Array\<(String)->String>|是|-| **命名参数。** 参与注册的应用侧JavaScript对象的同步方法。|
|name|String|是|-| **命名参数。** 注册对象的名称，与window中调用的对象名一致。|
|methodList|Array\<String>|是|-| **命名参数。** 参与注册的应用侧JavaScript对象的异步方法。|
|controller|[WebviewController](../apis/ArkWeb/cj-apis-webview.md)|是|-| **命名参数。** 设置Web控制器|

### func keyboardAvoidMode(WebKeyboardAvoidMode)

```cangjie
public func keyboardAvoidMode(mode: WebKeyboardAvoidMode): This
```

**功能：** Web组件自定义软件键盘避让模式。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[WebKeyboardAvoidMode](#enum-webkeyboardavoidmode)|是|-|Web软键盘避让模式。默认是WebKeyboardAvoidMode.RESIZE_CONTENT避让行为。嵌套滚动场景下不推荐使用web软键盘避让，包括RESIZE_VISUAL与RESIZE_CONTENT。|
### func onPrompt((OnPromptEvent) -> Bool)

```cangjie
public func onPrompt(callback: (OnPromptEvent) -> Bool): This
```

**功能：** 网页调用prompt()告警时触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([OnPromptEvent](#class-onpromptevent))->Bool|是|-|回调函数，网页调用prompt()告警时触发。返回值bool。当回调返回true时，应用可以调用自定义弹窗能力（包括确认和取消），并且需要根据用户的确认或取消操作调用WebResult通知Web组件最终是否离开当前页面。当回调返回false时，函数中绘制的自定义弹窗无效。|

### func onlineImageAccess(Bool)

```cangjie
public func onlineImageAccess(onlineImageAccess: Bool): This
```

**功能：** 设置是否允许从网络加载图片资源（通过HTTP和HTTPS访问的资源），默认允许访问。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onlineImageAccess|Bool|是|-|是否允许从网络加载图片资源。true表示设置允许从网络加载图片资源，false表示设置不允许从网络加载图片资源。<br> 初始值：true。|
### func onAdsBlocked((AdsBlockedDetails) -> Unit)

```cangjie
public func onAdsBlocked(callback: (AdsBlockedDetails) -> Unit): This
```

**功能：** 一个页面发生广告过滤后，通过此回调接口通知过滤的详细信息。由于页面可能随时发生变化并不断产生网络请求，为了减少通知频次、降低对页面加载过程的影响，仅在页面加载完成时进行首次通知，此后发生的过滤将间隔1秒钟上报，无广告过滤则无通知。

**需要权限：**  SystemCapability.Web.Webview.Core

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([AdsBlockedDetails](#class-adsblockeddetails))->Unit|是|-|回调函数，onAdsBlocked的回调。|

### func onAlert((OnAlertEvent) -> Bool)

```cangjie
public func onAlert(callback: (OnAlertEvent) -> Bool): This
```

**功能：** 网页触发alert()告警弹窗时触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([OnAlertEvent](#class-onalertevent))->Bool|是|-|网页触发alert()告警弹窗时触发返回值boolean。当回调返回true时，应用可以调用自定义弹窗能力（包括确认和取消），并且需要根据用户的确认或取消操作调用WebResult通知Web组件最终是否离开当前页面。当回调返回false时，函数中绘制的自定义弹窗无效。|

### func onBeforeUnload((OnBeforeUnloadEvent) -> Bool)

```cangjie
public func onBeforeUnload(callback: (OnBeforeUnloadEvent) -> Bool): This
```

**功能：** 刷新或关闭场景下，在即将离开当前页面时触发此回调。刷新或关闭当前页面应先通过点击等方式获取焦点，才会触发此回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([OnBeforeUnloadEvent](#class-onbeforeunloadevent))->Bool|是|-|刷新或关闭场景下，在即将离开当前页面时触发。返回值boolean。当回调返回true时，应用可以调用自定义弹窗能力（包括确认和取消），并且需要根据用户的确认或取消操作调用WebResult通知Web组件最终是否离开当前页面。当回调返回false时，函数中绘制的自定义弹窗无效。|

### func onConfirm((OnConfirmEvent) -> Bool)

```cangjie
public func onConfirm(callback: (OnConfirmEvent) -> Bool): This
```

**功能：** 网页调用confirm()告警时触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([OnConfirmEvent](#class-onconfirmevent))->Bool|是|-|网页调用confirm()告警时触发<br>返回值boolean。当回调返回true时，应用可以调用自定义弹窗能力（包括确认和取消），并且需要根据用户的确认或取消操作调用WebResult通知Web组件最终是否离开当前页面。当回调返回false时，函数中绘制的自定义弹窗无效。|

### func onConsole((OnConsoleEvent) -> Bool)

```cangjie
public func onConsole(callback: (OnConsoleEvent) -> Bool): This
```

**功能：** 通知宿主应用JavaScript console消息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([OnConsoleEvent](#class-onconsoleevent))->Bool|是|-|网页收到JavaScript控制台消息时触发。返回值boolean。当返回true时，该条消息将不会再打印至控制台，反之仍会打印至控制台。|
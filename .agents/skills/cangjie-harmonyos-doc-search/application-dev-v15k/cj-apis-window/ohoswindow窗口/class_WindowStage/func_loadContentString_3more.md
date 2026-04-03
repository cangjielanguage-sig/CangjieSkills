### func loadContent(String)

```cangjie
public func loadContent(path: String): Unit
```

**功能：** 为当前WindowStage的主窗口加载具体页面内容。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|要加载到窗口中的页面内容的路径，该路径需添加到工程的main_pages.json文件中。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] findWindow: This window state is abnormal.|

### func off(WindowCallbackType, ?Callback1Argument\<WindowStageEventType>)

```cangjie
public func off(callbackType: WindowCallbackType,callback!: ?Callback1Argument<WindowStageEventType> = None): Unit
```

**功能：** 关闭WindowStage生命周期变化的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callbackType|[WindowCallbackType](#enum-windowcallbacktype)|是|-|监听事件类型，WindowCallbackType.WindowStageEvent才生效，即WindowStage生命周期变化事件。|
|callback|?[Callback1Argument](../apis/BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[WindowStageEventType](#enum-windowstageeventtype)>|否|None|回调函数实例对象。返回当前的WindowStage生命周期状态。若传入参数，则关闭该监听。若未传入参数，则关闭所有WindowStage生命周期变化的监听。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible cause: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types.|
  |1300002|This window state is abnormal.|
  |1300005|This window state is abnormal.|

### func on(WindowCallbackType, Callback1Argument\<WindowStageEventType>)

```cangjie
public func on(callbackType: WindowCallbackType, callback: Callback1Argument<WindowStageEventType>): Unit
```

**功能：** 开启WindowStage生命周期变化的监听。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callbackType|[WindowCallbackType](#enum-windowcallbacktype)|是|-|监听事件类型，WindowCallbackType.WindowStageEvent才生效，即WindowStage生命周期变化事件。|
|callback|[Callback1Argument](../apis/BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[WindowStageEventType](#enum-windowstageeventtype)>|是|-|回调函数实例对象。返回当前的WindowStage生命周期状态。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible cause: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types.|
  |1300002|This window state is abnormal.|
  |1300005|This window state is abnormal.|
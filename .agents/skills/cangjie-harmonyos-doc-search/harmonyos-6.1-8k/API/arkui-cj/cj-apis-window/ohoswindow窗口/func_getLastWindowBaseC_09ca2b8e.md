## func getLastWindow(BaseContext)

```cangjie
public func getLastWindow(ctx: BaseContext): Window
```

**功能：** 获取当前应用程序的顶层窗口。如果没有子窗口，则返回应用程序的主窗口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|ctx|[BaseContext](../AbilityKit/cj-apis-app-ability.md#class-basecontext)|是|-|当前应用程序上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[Window](#class-window)|返回获取的顶层窗口。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1300002|This window state is abnormal.|
  |1300006|This window context is abnormal.|
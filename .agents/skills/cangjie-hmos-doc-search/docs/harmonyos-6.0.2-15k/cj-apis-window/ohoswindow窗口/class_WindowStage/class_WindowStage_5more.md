## class WindowStage

```cangjie
public class WindowStage {}
```

**功能：** 窗口管理器。管理各个基本窗口单元，即Window实例。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### func createSubWindow(String)

```cangjie
public func createSubWindow(name: String): Window
```

**功能：** 创建该WindowStage实例下的子窗口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|子窗口的名字。|

**返回值：**

|类型|说明|
|:----|:----|
|[Window](#class-window)|返回当前WindowStage下的子窗口对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[WindowStage] create subwindow: This window state is abnormal.|

### func createSubWindowWithOptions(String, SubWindowOptions)

```cangjie
public func createSubWindowWithOptions(name: String, option: SubWindowOptions): Window
```

**功能：** 创建该WindowStage实例下的子窗口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|子窗口的名字。|
|option|[SubWindowOptions](#class-subwindowoptions)|是|-|子窗口参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[Window](#class-window)|返回当前WindowStage下创建的子窗口对象|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |202|[WindowStage] create subwindow: Permission verification failed, application which is not a system application uses system API.|
  |801|[WindowStage] create subwindow: Capability not supported.|
  |1300002|[WindowStage] create subwindow: This window state is abnormal.|

### func getMainWindow()

```cangjie
public func getMainWindow(): Window
```

**功能：** 获取该WindowStage实例下的主窗口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[Window](#class-window)|返回当前WindowStage下的主窗口对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[WindowStage] get mainwindow:This window state is abnormal.|

### func getSubWindow()

```cangjie
public func getSubWindow(): Array<Window>
```

**功能：** 获取该WindowStage实例下的所有子窗口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[Window](#class-window)>|返回当前WindowStage下的所有子窗口对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[WindowStage] get subWindow: This window state is abnormal.|
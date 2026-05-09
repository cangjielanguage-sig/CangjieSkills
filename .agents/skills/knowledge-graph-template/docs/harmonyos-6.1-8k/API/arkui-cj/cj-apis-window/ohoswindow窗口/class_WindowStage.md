## class WindowStage

```cangjie
public class WindowStage {}
```

**功能：** 窗口管理器。管理各个基本窗口单元，即[Window](#class-window)实例。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### func createSubWindow(String)

```cangjie
public func createSubWindow(name: String): Window
```

**功能：** 创建该WindowStage实例下的子窗口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|子窗口名称。|

**返回值：**

|类型|说明|
|:----|:----|
|[Window](#class-window)|返回子窗口。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1300002|This window state is abnormal.|

### func getMainWindow()

```cangjie
public func getMainWindow(): Window
```

**功能：** 获取此窗口阶段的主窗口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[Window](#class-window)|返回主窗口。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1300002|This window state is abnormal.|

### func getSubWindow()

```cangjie
public func getSubWindow(): Array<Window>
```

**功能：** 获取此窗口阶段的所有子窗口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[Window](#class-window)>|返回所有子窗口。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)和[窗口错误码](./cj-errorcode-window.md)。

  |错误码|说明|
  |:----|:----|
  |1300002|This window state is abnormal.|

### func loadContent(String)

```cangjie
public func loadContent(path: String): Unit
```

**功能：** 将页面内容加载到此窗口。建议在UIAbility启动期间调用此API。
如果多次调用，此API将在加载新内容之前销毁现有页面内容(UIContent)。使用时请谨慎。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|将加载内容的页面路径。|
### func setSpecificSystemBarEnabled(SpecificSystemBar, Bool, Bool)

```cangjie
public func setSpecificSystemBarEnabled(name: SpecificSystemBar, enable: Bool, enableAnimation: Bool): Unit
```

**功能：** 设置主窗口三键导航栏、状态栏、底部导航条的显示和隐藏。

> **说明：**
>
> - 该接口在2in1设备上调用不生效。
> - 其他设备在分屏模式（即窗口模式为[WindowStatusType.SPLIT_SCREEN](#enum-windowstatustype)）、自由悬浮窗口模式（即窗口模式为[WindowStatusType.FLOATING](#enum-windowstatustype)）、自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下调用不会立刻生效，只有进入全屏主窗口才会生效。
> - 调用生效后返回并不表示三键导航栏、状态栏和底部导航条的显示或隐藏已完成。子窗口调用后不生效。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|[SpecificSystemBar](#enum-specificsystembar)|是|-|设置窗口全屏模式时，显示或隐藏的系统栏类型。|
|enable|Bool|是|-|设置窗口全屏模式时状态栏、三键导航栏或底部导航条是否显示，true表示显示， false表示隐藏。|
|enableAnimation|Bool|是|-|设置状态栏、三键导航栏或底部导航条显示状态变化时是否使用动画，true表示使用， false表示不使用。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|[Window] setSpecificSystemBarEnabled: Parameter error. |
  |1300002|[Window] setSpecificSystemBarEnabled: This window state is abnormal.|

### func setSubWindowModal(Bool)

```cangjie
public func setSubWindowModal(isModal: Bool): Unit
```

**功能：** 设置子窗的模态属性是否启用。

> **说明：**
>
> - 子窗口调用该接口时，设置子窗口模态属性是否启用。启用子窗口模态属性后，其父级窗口不能响应用户操作，直到子窗口关闭或者子窗口的模态属性被禁用。
>
> - 子窗口之外的窗口调用该接口时，会报错。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isModal|Bool|是|-|设置子窗口模态属性是否启用，true为启用，false为不启用|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|[Window] setSubWindowModal: Capability not supported.|
  |1300002|[Window] setSubWindowModal: This window state is abnormal.|
  |1300004|[Window] setSubWindowModal: Unauthorized operation.|

### func setWindowBackgroundColor(String)

```cangjie
public func setWindowBackgroundColor(color: String): Unit
```

**功能：** 设置窗口的背景色。

> **说明：**
>
> 该接口需要在[loadContent()](#func-loadcontentstring)调用生效后使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|String|是|-|需要设置的背景色，为十六进制RGB或ARGB颜色，不区分大小写。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible cause: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed.|
  |1300002|[Window] setWindowBackgroundColor: This window state is abnormal.|
### func setWindowLayoutFullScreen(Bool)

```cangjie
public func setWindowLayoutFullScreen(isLayoutFullScreen: Bool): Unit
```

**功能：** 设置主窗口或子窗口的布局是否为沉浸式布局。

> **说明：**
>
> - 沉浸式布局生效时，布局不避让状态栏与导航栏，组件可能产生与其重叠的情况。
> - 非沉浸式布局生效时，布局避让状态栏与导航栏，组件不会与其重叠。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isLayoutFullScreen|Bool|是|-|窗口的布局是否为沉浸式布局（该沉浸式布局状态栏、导航栏仍然显示）。true表示沉浸式布局；false表示非沉浸式布局。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] setWindowLayoutFullScreen: This window state is abnormal.|

### func setWindowLimits(WindowLimits)

```cangjie
public func setWindowLimits(windowLimits: WindowLimits): WindowLimits
```

**功能：** 设置当前应用窗口的尺寸限制。

> **说明：**
>
> 默认存在一个系统尺寸限制，系统尺寸限制由产品配置决定，不可修改。未调用[setWindowLimits](#func-setwindowlimitswindowlimits)配置过[WindowLimits](#class-windowlimits)时，使用[getWindowLimits](#func-getwindowlimits)可获取系统限制。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|windowLimits|[WindowLimits](#class-windowlimits)|是|-|目标窗口的尺寸限制，单位为px。|

**返回值：**

|类型|说明|
|:----|:----|
|[WindowLimits](#class-windowlimits)|返回设置后的尺寸限制|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|[Window] setWindowLimits: Parameter error. |
  |1300002|[Window] setWindowLimits: This window state is abnormal.|

### func setWindowPrivacyMode(Bool)

```cangjie
public func setWindowPrivacyMode(isPrivacyMode: Bool): Unit
```

**功能：** 设置窗口是否为隐私模式。设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。此接口可用于禁止截屏/录屏的场景。

**需要权限：** ohos.permission.PRIVACY_WINDOW

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isPrivacyMode|Bool|是|-|窗口是否为隐私模式。true表示模式开启；false表示模式关闭。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] setWindowPrivacyMode: This window state is abnormal.|
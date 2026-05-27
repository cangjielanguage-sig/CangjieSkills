### func resize(UInt32, UInt32)

```cangjie
public func resize(width: UInt32, height: UInt32): Unit
```

**功能：** 改变当前窗口大小。

> **说明：**
>
> - 应用主窗口与子窗口存在大小限制，默认宽度范围：[320, 1920]，默认高度范围：[240, 1920]，单位为vp。
>
> - 应用主窗口与子窗口的最小宽度与最小高度可由产品端进行配置，配置后的最小宽度与最小高度以产品段配置值为准，具体尺寸限制范围可以通过[getWindowLimits](#func-getwindowlimits)接口进行查询。
>
> - 系统窗口存在大小限制，宽度范围：(0, 1920]，高度范围：(0, 1920]，单位为vp。设置的宽度与高度受到此约束限制，规则：<br>若所设置的窗口宽/高尺寸小于窗口最小宽/高限值，则窗口最小宽/高限值生效；<br>若所设置的窗口宽/高尺寸大于窗口最大宽/高限值，则窗口最大宽/高限值生效。<br>全屏模式窗口不支持该操作。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|UInt32|是|-|目标窗口的宽度，单位为px。|
|height|UInt32|是|-|目标窗口的高度，单位为px。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible cause: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed.|
  |1300002|This window state is abnormal.|
  |1300003|This window manager service works abnormally.|

### func setAspectRatio(Float64)

```cangjie
public func setAspectRatio(ratio: Float64): Unit
```

**功能：** 设置窗口内容布局的比例。

> **说明：**
>
> - 通过其他接口如resize、resizeAsync设置窗口大小时，不受ratio约束。
> - 仅主窗可设置，且仅在自由悬浮窗口模式（即窗口模式为[WindowStatusType.FLOATING](#enum-windowstatustype)）下生效，比例参数将持久化保存，关闭应用或重启设备设置的比例仍然生效。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|ratio|Float64|是|-|除边框装饰之外的窗口内容布局的宽高比。<br>**说明：**<br>该参数受窗口最大最小尺寸限制，比例值下限为最小宽度/最大高度，上限为最大宽度/最小高度。窗口最大最小尺寸由[WindowLimits](#class-windowlimits)和系统限制的交集决定，系统限制优先级高于[WindowLimits](#class-windowlimits)。ratio的有效范围会随[WindowLimits](#class-windowlimits)变化而变化。如果先设置了[WindowLimits](#class-windowlimits)，后设置的ratio与其冲突，会返回错误码；如果先设置了ratio，后设置的[WindowLimits](#class-windowlimits)与其冲突，窗口的宽高比可能会不跟随设置的宽高比（ratio）。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|[Window] setAspectRatio: Parameter error.|
  |1300002|[Window] setAspectRatio: This window state is abnormal.|
  |1300004|[Window] setAspectRatio: Unauthorized operation.|
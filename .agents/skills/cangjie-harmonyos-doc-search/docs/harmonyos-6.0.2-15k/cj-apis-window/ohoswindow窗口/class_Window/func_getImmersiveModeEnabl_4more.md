### func getImmersiveModeEnabledState()

```cangjie
public func getImmersiveModeEnabledState(): Bool
```

**功能：** 查询当前窗口是否已经开启沉浸式布局。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|是否已经开启沉浸式布局。<br>true表示开启，false表示关闭。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1300002|[Window] setImmersiveModeEnabledState: This window state is abnormal.|

### func getPreferredOrientation()

```cangjie
public func getPreferredOrientation(): Orientation
```

**功能：** 主窗口调用，获取窗口的显示方向属性。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[Orientation](#enum-orientation)|窗口显示方向的属性。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|[Window] getPreferredOrientation: Parameter error.|
  |1300002|[Window] getPreferredOrientation: This window state is abnormal.|

### func getTitleButtonRect()

```cangjie
public func getTitleButtonRect(): TitleButtonRect
```

**功能：** 获取主窗口或启用装饰的子窗口的标题栏上的最小化、最大化、关闭按钮矩形区域。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[TitleButtonRect](#class-titlebuttonrect)|标题栏上的最小化、最大化、关闭按钮矩形区域，该区域位置坐标相对窗口右上角。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|[Window] getWindowDecorHeight: Capability not supported. |
  |1300002|[Window] getWindowDecorHeight: This window state is abnormal.|

### func getWindowAvoidArea(AvoidAreaType)

```cangjie
public func getWindowAvoidArea(areaType: AvoidAreaType): AvoidArea
```

**功能：** 获取当前应用窗口内容规避的区域。如系统栏区域、刘海屏区域、手势区域、软键盘区域等与窗口内容重叠时，需要窗口内容避让的区域。

> **说明：**
>
> 该接口一般适用于两种场景：
> 1、在onWindowStageCreate方法中，获取应用启动时的初始布局避让区域时可调用该接口；
> 2、当应用内子窗需要临时显示，对显示内容做布局避让时可调用该接口。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|areaType|[AvoidAreaType](#enum-avoidareatype)|是|-|表示规避区类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[AvoidArea](#class-avoidarea)|窗口内容规避区域。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)和[窗口错误码](../errorcodes/cj-errorcode-window.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|[Window] getWindowAvoidArea: Parameter error.|
  |1300002|[Window] getWindowAvoidArea: This window state is abnormal.|
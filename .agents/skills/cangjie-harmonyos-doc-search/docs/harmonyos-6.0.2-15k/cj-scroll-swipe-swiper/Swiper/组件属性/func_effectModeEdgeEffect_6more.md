### func effectMode(EdgeEffect)

```cangjie
public func effectMode(value: EdgeEffect): This
```

**功能：** 设置边缘滑动效果，[loop](#func-loopbool) = false时生效。调用SwiperController.changeIndex()、SwiperController.showNext()和SwiperController.showPrevious()接口跳转至首尾页时不生效回弹。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[EdgeEffect](./cj-common-types.md#enum-edgeeffect)|是|-|边缘滑动效果。<br>初始值：EdgeEffect.Spring。|

### func index(UInt32)

```cangjie
public func index(value: UInt32): This
```

**功能：** 设置当前在容器中显示的子组件的索引值。设置大于等于子组件数量时，按照初始值0处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|UInt32|是|-|当前在容器中显示的子组件的索引值。<br> **说明：**<br>设置的值小于0或大于最大页面索引时，取0。<br>初始值：0。|

### func indicator(Bool)

```cangjie
public func indicator(value: Bool): This
```

**功能：** 设置可选导航点指示器样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|可选导航点指示器样式。<br>- boolean：是否启用导航点指示器。设置为true启用，false不启用。<br>初始值：true。|

### func indicator(DotIndicator)

```cangjie
public func indicator(value: DotIndicator): This
```

**功能：** 设置外部绑定的导航点组件控制器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[DotIndicator](#class-dotindicator)|是|-|可选导航点指示器样式。<br>- DotIndicator：圆点指示器样式。|

### func indicator(DigitIndicator)

```cangjie
public func indicator(value: DigitIndicator): This
```

**功能：** 设置外部绑定的导航点组件控制器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[DigitIndicator](#class-digitindicator)|是|-|可选导航点指示器样式。<br>- DigitIndicator：数字指示器样式。|

### func indicatorInteractive(Bool)

```cangjie
public func indicatorInteractive(value: Bool): This
```

**功能：** 设置禁用组件导航点交互功能。设置为true时表示导航点可交互。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|导航点是否可交互。true为导航点可交互，false为导航点不可交互。<br>初始值：true。|
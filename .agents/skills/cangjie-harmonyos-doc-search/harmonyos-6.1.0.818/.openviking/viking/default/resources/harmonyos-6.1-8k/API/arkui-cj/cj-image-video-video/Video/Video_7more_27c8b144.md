# Video

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

用于播放视频文件并控制其播放状态的组件。

> **说明：**
>
> Video组件只提供简单的视频播放功能，无法支撑复杂的视频播控场景。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 权限列表

使用网络视频时，需要申请权限ohos.permission.INTERNET。

## 子组件

不支持子组件。

## 创建组件

### init(?ResourceStr, ?PlaybackSpeed, ?ResourceStr, ?VideoController)

```cangjie
public init(
    src!: ?ResourceStr = None,
    currentProgressRate!: ?PlaybackSpeed = Option.None,
    previewUri!: ?ResourceStr = None,
    controller!: ?VideoController = None
)
```

**功能：** 根据视频的数据源，播放倍速，预览图片和视频控制器创建一个 video 组件。

**需要权限：** 使用网络视频时，需要申请权限ohos.permission.INTERNET。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None| **命名参数。** 视频的数据源，支持本地视频和网络视频。|
|currentProgressRate|?[PlaybackSpeed](./cj-common-types.md#enum-playbackspeed)|否|Option.None| **命名参数。** 视频播放倍速。<br>初始值：SpeedForward100X。|
|previewUri|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None| **命名参数。** 视频未播放时的预览图片路径。|
|controller|?[VideoController](#class-videocontroller)|否|None| **命名参数。** 设置视频控制器，可以控制视频的播放状态。<br>初始值：VideoController()|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。

## 组件属性

### func autoPlay(?Bool)

```cangjie
public func autoPlay(value: ?Bool): This
```

**功能：** 设置视频是否自动播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|视频是否自动播放。<br>初始值：false。|

### func controls(?Bool)

```cangjie
public func controls(value: ?Bool): This
```

**功能：** 设置控制视频播放的控制栏是否显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|是否显示控制栏。<br>初始值：true。|

### func loop(?Bool)

```cangjie
public func loop(value: ?Bool): This
```

**功能：** 设置是否单个视频循环播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|视频是否循环播放。<br>初始值：false。|

### func muted(?Bool)

```cangjie
public func muted(value: ?Bool): This
```

**功能：** 设置视频是否静音。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|视频是否静音。<br>初始值：false。|

### func objectFit(?ImageFit)

```cangjie
public func objectFit(value: ?ImageFit): This
```

**功能：** 设置视频填充模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ImageFit](./cj-common-types.md#enum-imagefit)|是|-|视频填充模式。<br>初始值：ImageFit.Cover。|
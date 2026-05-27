### init(AppResource, Float64, AppResource, VideoController)

```cangjie
public init(
    src!: AppResource,
    currentProgressRate!: Float64 = 1.0,
    previewUri!: AppResource,
    controller!: VideoController = VideoController()
)
```

**功能：** 根据视频的数据源，播放倍速，预览图片和视频控制器创建一个 video 组件。

**需要权限：** 使用网络视频时，需要申请权限ohos.permission.INTERNET。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 视频的数据源，支持本地视频和网络视频。<br>Resource格式可以跨包/跨模块访问资源文件，常用于访问本地视频。<br>- 支持rawfile文件下的资源，即通过@rawfile引用视频文件。<br>视频支持的格式是：mp4、mkv、TS。|
|currentProgressRate|Float64|否|1.0| **命名参数。** 视频播放倍速。<br>取值仅支持：0.75，1.0，1.25，1.75，2.0。|
|previewUri|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 视频未播放时的预览图片路径。|
|controller|[VideoController](#class-videocontroller)|否|VideoController()| **命名参数。** 设置视频控制器，可以控制视频的播放状态。|

### init(AppResource, PlaybackSpeed, AppResource, VideoController)

```cangjie
public init(
    src!: AppResource,
    currentProgressRate!: PlaybackSpeed,
    previewUri!: AppResource,
    controller!: VideoController = VideoController()
)
```

**功能：** 根据视频的数据源，播放倍速，预览图片和视频控制器创建一个 video 组件。

**需要权限：** 使用网络视频时，需要申请权限ohos.permission.INTERNET。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 视频的数据源，支持本地视频和网络视频。<br>Resource格式可以跨包/跨模块访问资源文件，常用于访问本地视频。<br>- 支持rawfile文件下的资源，即通过@rawfile引用视频文件。<br>视频支持的格式是：mp4、mkv、TS。|
|currentProgressRate|[PlaybackSpeed](#enum-playbackspeed)|是|-| **命名参数。** 视频播放倍速。<br>取值仅支持：Speed_Forward_0_75_X，Speed_Forward_1_00_X，Speed_Forward_1_25_X，Speed_Forward_1_75_X，Speed_Forward_2_00_X。|
|previewUri|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 视频未播放时的预览图片路径。|
|controller|[VideoController](#class-videocontroller)|否|VideoController()| **命名参数。** 设置视频控制器，可以控制视频的播放状态。|
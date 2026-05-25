# ohos.multimedia.camera_picker（相机选择器）

本模块提供相机拍照与录制的能力。应用可以自行选择媒体类型实现拍照和录制的功能。该模块接口，需要应用在界面UIAbility中调用，否则无法拉起cameraPicker应用。

## 导入模块

```cangjie
import kit.CameraKit.*
```

## func pick(UIAbilityContext, Array\<PickerMediaType>, PickerProfile, Callback1Argument\<PickerResult>)

```cangjie
public func pick(context: UIAbilityContext, mediaTypes: Array<PickerMediaType>, pickerProfile: PickerProfile,
    callback: Callback1Argument<PickerResult>): Unit
```

**功能：** 拉起相机选择器，根据媒体类型进入相应的模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](../AbilityKit/cj-apis-ability.md#class-uiabilitycontext)|是|-|应用上下文。|
|mediaTypes|Array\<[PickerMediaType](#enum-pickermediatype)>|是|-|媒体类型。|
|pickerProfile|[PickerProfile](#struct-pickerprofile)|是|-|pickerProfile对象。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[PickerResult](#struct-pickerresult)>|是|-|使用回调的方式获取相机选择器的处理结果。|

## struct PickerProfile

```cangjie
public struct PickerProfile {
    public var cameraPosition: CameraPosition
    public var saveUri: String
    public var videoDuration: Int32
    public init(cameraPosition: CameraPosition, saveUri!: String = "", videoDuration!: Int32 = 0)
}
```

**功能：** 相机选择器的配置信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### var cameraPosition

```cangjie
public var cameraPosition: CameraPosition
```

**功能：** 相机的位置。

**类型：** [CameraPosition](../CameraKit/cj-apis-multimedia-camera.md#enum-cameraposition)

**读写能力：** 可读写

**起始版本：** 19

### var saveUri

```cangjie
public var saveUri: String
```

**功能：** 保存配置信息的uri。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var videoDuration

```cangjie
public var videoDuration: Int32
```

**功能：** 录制的最大时长。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### init(CameraPosition, String, Int32)

```cangjie
public init(cameraPosition: CameraPosition, saveUri!: String = "", videoDuration!: Int32 = 0)
```

**功能：** 创建PickerProfile。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cameraPosition|[CameraPosition](../CameraKit/cj-apis-multimedia-camera.md#enum-cameraposition)|是|-|相机的位置。|
|saveUri|String|否|""| **命名参数。** 保存配置信息的uri。|
|videoDuration|Int32|否|0| **命名参数。** 录制的最大时长。|
### class XComponentController

```cangjie
public open class XComponentController {
    public init()
}
```

**功能：** XComponent组件的控制器，可以将此对象绑定至XComponent组件，然后通过控制器来调用组件方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init()

```cangjie
public init()
```

**功能：** 构造一个XComponentController类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### func getXComponentSurfaceId()

```cangjie
public func getXComponentSurfaceId(): String
```

**功能：** 获取XComponent对应Surface的ID，供ohos接口使用，使用方式可参考[相机管理](../apis/CameraKit/cj-apis-multimedia-camera.md)，仅XComponent类型为SURFACE或TEXTURE时有效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|XComponent持有Surface的ID。|

#### func getXComponentSurfaceRect()

```cangjie
public func getXComponentSurfaceRect(): SurfaceRect
```

**功能：** 获取XComponent持有Surface的显示区域，仅XComponent类型为SURFACE或TEXTURE时有效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[SurfaceRect](#class-surfacerect)|获取XComponent持有Surface的显示区域。|

#### func getXComponentSurfaceRotation()

```cangjie
public func getXComponentSurfaceRotation(): SurfaceRotationOptions
```

**功能：** 获取XComponent持有Surface在屏幕旋转时是否锁定方向的设置，仅XComponent类型为SURFACE时有效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[SurfaceRotationOptions](#class-surfacerotationoptions)|获取XComponent持有Surface在屏幕旋转时是否锁定方向的设置。|

#### func setXComponentSurfaceRect(SurfaceRect)

```cangjie
public func setXComponentSurfaceRect(rect: SurfaceRect): Unit
```

**功能：** 设置XComponent持有Surface的显示区域，仅XComponent类型为SURFACE或TEXTURE时有效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rect|[SurfaceRect](#class-surfacerect)|是|-|XComponent持有Surface的显示区域。|

#### func setXComponentSurfaceRotation(SurfaceRotationOptions)

```cangjie
public func setXComponentSurfaceRotation(rotationOptions: SurfaceRotationOptions): Unit
```

**功能：** 设置XComponent持有Surface在屏幕旋转时是否锁定方向，仅XComponent类型为SURFACE时有效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rotationOptions|[SurfaceRotationOptions](#class-surfacerotationoptions)|是|-|设置XComponent持有Surface在屏幕旋转时是否锁定方向。|

> **说明：**
>
> - rotationOptions未配置时，默认XComponent持有Surface在屏幕旋转时不锁定方向，跟随屏幕进行旋转。
> - 仅在屏幕旋转过程中生效，旋转完成后不再锁定Surface。
> - 仅在屏幕旋转90°，即发生横竖屏切换时生效。
> - 锁定旋转后的Buffer宽高需要保持不变，否则会有拉伸问题。
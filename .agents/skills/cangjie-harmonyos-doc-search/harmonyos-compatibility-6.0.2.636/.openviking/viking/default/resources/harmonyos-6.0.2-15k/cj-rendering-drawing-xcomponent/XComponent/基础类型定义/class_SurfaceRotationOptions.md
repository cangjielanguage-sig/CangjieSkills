### class SurfaceRotationOptions

```cangjie
public class SurfaceRotationOptions {
    public var lock: Bool
    public init(lock: Bool)
}
```

**功能：** 用于描述XComponent持有Surface在屏幕旋转时是否锁定方向的设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var lock

```cangjie
public var lock: Bool
```

**功能：** Surface在屏幕旋转时是否锁定方向。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Bool)

```cangjie
public init(lock: Bool)
```

**功能：** 创建SurfaceRotationOptions。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|lock|Bool|是|-|Surface在屏幕旋转时是否锁定方向。<br> 初始值：false，即不锁定方向。|
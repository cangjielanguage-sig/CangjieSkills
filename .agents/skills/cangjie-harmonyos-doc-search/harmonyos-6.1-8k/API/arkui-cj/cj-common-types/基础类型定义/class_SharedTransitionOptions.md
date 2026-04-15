## class SharedTransitionOptions

```cangjie
public class SharedTransitionOptions {
    public var duration: ?Int32
    public var curve: ?Curve
    public var delay: ?Int32
    public var motionPath: ?MotionPathOptions
    public var zIndex: ?Int32
    public var effectType: ?SharedTransitionEffectType
    public init(duration!: ?Int32 = None, curve!: ?Curve = None, delay!: ?Int32 = None, motionPath!: ?MotionPathOptions = None, zIndex!: ?Int32 = None, effectType!: ?SharedTransitionEffectType = None)
}
```

**功能：** 共享转场选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var duration

```cangjie
public var duration: ?Int32
```

**功能：** 描述共享元素转场动效播放时长。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var curve

```cangjie
public var curve: ?Curve
```

**功能：** 动画曲线。

**类型：** ?[Curve](#enum-curve)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var delay

```cangjie
public var delay: ?Int32
```

**功能：** 延迟播放时间。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var motionPath

```cangjie
public var motionPath: ?MotionPathOptions
```

**功能：** 设置共享转场的运动路径。

**类型：** ?[MotionPathOptions](#class-motionpathoptions)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var zIndex

```cangjie
public var zIndex: ?Int32
```

**功能：** 设置Z轴。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var effectType

```cangjie
public var effectType: ?SharedTransitionEffectType
```

**功能：** 动画类型。

**类型：** ?[SharedTransitionEffectType](#enum-sharedtransitioneffecttype)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?Int32, ?Curve, ?Int32, ?MotionPathOptions, ?Int32, ?SharedTransitionEffectType)

```cangjie
public init(duration!: ?Int32 = None, curve!: ?Curve = None, delay!: ?Int32 = None, motionPath!: ?MotionPathOptions = None, zIndex!: ?Int32 = None, effectType!: ?SharedTransitionEffectType = None)
```

**功能：** 构造一个SharedTransitionOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|duration|?Int32|否|None|**命名参数。** 描述共享元素转场动效播放时长。<br>初始值：1000。<br>单位：毫秒。<br>取值范围：[0, +∞)。|
|curve|?[Curve](./cj-common-types.md#enum-curve)|否|None|**命名参数。** 动画曲线。<br>初始值：Curve.Linear。|
|delay|?Int32|否|None|**命名参数。** 延迟播放时间。<br>初始值：0。<br>单位：毫秒。|
|motionPath|?[MotionPathOptions](#class-motionpathoptions)|否|None|**命名参数。** 设置共享转场的运动路径。<br>初始值：MotionPathOptions(path: "")。|
|zIndex|?Int32|否|None|**命名参数。** 设置Z轴。<br>取值范围：(-∞, +∞)。<br>初始值：0。|
|effectType|?[SharedTransitionEffectType](./cj-common-types.md#enum-sharedtransitioneffecttype)|否|None|**命名参数。** 动画类型。<br>初始值为SharedTransitionEffectType.Exchange。|
#### init(Float64, Float64, Float64, Float64, Int32)

```cangjie
public init(
    width: Float64,
    height: Float64,
    componentWidth: Float64,
    componentHeight: Float64,
    loadingStatus: Int32
)
```

**功能：** 构造一个 CJImageComplete 实例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|Float64|是|-|图片的宽度。<br>单位：px。|
|height|Float64|是|-|图片的高度。<br>单位：px。|
|componentWidth|Float64|是|-|组件的宽度。<br>单位：px。|
|componentHeight|Float64|是|-|组件的高度。<br>单位：px。|
|loadingStatus|Int32|是|-|图片加载成功的状态。|

#### init(Float64, Float64, Float64, Float64, Int32, Float64, Float64, Float64, Float64)

```cangjie
public init(
    width: Float64,
    height: Float64,
    componentWidth: Float64,
    componentHeight: Float64,
    loadingStatus: Int32,
    contentWidth: Float64,
    contentHeight: Float64,
    contentOffsetX: Float64,
    contentOffsetY: Float64
)
```

**功能：** 构造一个 CJImageComplete 实例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|Float64|是|-|图片的宽度。<br>单位：px。|
|height|Float64|是|-|图片的高度。<br>单位：px。|
|componentWidth|Float64|是|-|组件的宽度。<br>单位：px。|
|componentHeight|Float64|是|-|组件的高度。<br>单位：px。|
|loadingStatus|Int32|是|-|图片加载成功的状态。|
|contentWidth|Float64|是|-|图片实际绘制的宽度。<br>单位：px。<br>仅在loadingStatus返回1时有效。|
|contentHeight|Float64|是|-|图片实际绘制的高度。<br>单位：px。<br>仅在loadingStatus返回1时有效。|
|contentOffsetX|Float64|是|-|实际绘制内容相对于组件自身的x轴偏移。<br>单位：px。<br>仅在loadingStatus返回1时有效。|
|contentOffsetY|Float64|是|-|实际绘制内容相对于组件自身的y轴偏移。<br>单位：px。<br>仅在loadingStatus返回1时有效。|

#### init()

```cangjie
public init()
```

**功能：** 构造一个 CJImageComplete 实例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19
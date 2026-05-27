## class NativeMediaPlayerSurfaceInfo

```cangjie
public class NativeMediaPlayerSurfaceInfo {
    public NativeMediaPlayerSurfaceInfo(
        let id: String,
        let rect: RectEvent
    )
}
```

**功能：** [应用接管网页媒体播放功能](../../arkui-cj/cj-web-web.md#func-enablenativemediaplayerbool-bool)中用于同层渲染的 surface 信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### NativeMediaPlayerSurfaceInfo(String, RectEvent)

```cangjie
public NativeMediaPlayerSurfaceInfo(
    let id: String,
    let rect: RectEvent
)
```

**功能：** 构造NativeMediaPlayerSurfaceInfo对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|String|是|-|surface的id，用于同层渲染的NativeImage的psurfaceid。|
|rect|[RectEvent](#class-rectevent)|是|-|surface的位置信息。|

## class ScrollOffset

```cangjie
public class ScrollOffset {
    public var x: Float32
    public var y: Float32
    public init(x: Float32, y: Float32)
}
```

**功能：** 提供网页当前的滚动偏移量。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 20

**示例：**

```cangjie
let scrollOffset: ScrollOffset = ScrollOffset(0.0, 0.0)
```

### var x

```cangjie
public var x: Float32,
```

**功能：** 网页在水平方向的滚动偏移量。取值为网页左边界x坐标与Web组件左边界x坐标的差值。当网页向右过滚动时，取值范围为负值。当网页没有过滚动或者网页向左过滚动时，取值为0或正值。单位：vp。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 20

### var y

```cangjie
public var y: Float32
```

**功能：** 网页在垂直方向的滚动偏移量。取值为网页上边界y坐标与Web组件上边界y坐标的差值。当网页向下过滚动时，取值范围为负值。当网页没有过滚动或者网页向上过滚动时，取值为0或正值。单位：vp。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 20

### init(Float32, Float32)

```cangjie
public init(x: Float32, y: Float32)
```

**功能：** ScrollOffset对象的构造方法

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|是|-|网页在水平方向的滚动偏移量。|
|y|Float32|是|-|网页在垂直方向的滚动偏移量。|
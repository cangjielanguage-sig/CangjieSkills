## class CJSnapshotOptions

```cangjie
public class CJSnapshotOptions {
    public CJSnapshotOptions(
        public let scale: Float32,
        public let waitUntilRenderFinished: Bool
    )
}
```

**功能：** 截图相关的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let scale

```cangjie
public let scale: Float32
```

**功能：** 指定截图时图形侧绘制pixelmap的缩放比例。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 19

### let waitUntilRenderFinished

```cangjie
public let waitUntilRenderFinished: Bool
```

**功能：** 设置是否强制系统在截图前等待所有绘制指令执行完毕。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### CJSnapshotOptions(Float32, Bool)

```cangjie
public CJSnapshotOptions(
    public let scale: Float32,
    public let waitUntilRenderFinished: Bool
)
```

**功能：** 创建截图选项对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scale|Float32|是|-|指定截图时图形侧绘制pixelmap的缩放比例，比例过大时截图时间会变长，或者截图可能会失败。<br>取值范围：[0, +∞)，当小于等于0时按默认情况处理。<br>**说明：**<br>请不要截取过大尺寸的图片，截图不建议超过屏幕尺寸的大小。当要截取的图片目标长宽超过底层限制时，截图会返回失败，不同设备的底层限制不同。|
|waitUntilRenderFinished|Bool|是|-|设置是否强制系统在截图前等待所有绘制指令执行完毕。true表示强制系统在截图前等待所有绘制指令执行完毕，false表示不强制系统在截图前等待所有绘制指令执行完毕。该选项可尽可能确保截图内容是最新的状态，应尽量开启。需要注意的是，开启后接口可能需要更长的时间返回，具体的时间依赖页面当时时刻需要重绘区域的大小。|

## type SnapshotRetCallBack

```cangjie
public type SnapshotRetCallBack = AsyncCallback<PixelMap>
```

**功能：** SnapshotRetCallBack是[AsyncCallback](../apis/BasicServicesKit/cj-apis-base.md#type-asynccallback)\<[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)>类型的别名。
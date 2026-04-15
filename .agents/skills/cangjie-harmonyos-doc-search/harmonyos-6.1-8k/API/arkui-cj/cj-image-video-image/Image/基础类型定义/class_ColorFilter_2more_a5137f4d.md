### class ColorFilter

```cangjie
public class ColorFilter {
    public init(value: ?Array<Float32>)
}
```

**功能：** 颜色滤镜矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Array\<Float32>)

```cangjie
public init(value: ?Array<Float32>)
```

**功能：** 构建一个颜色滤镜矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Array\<Float32>|是|-|4x5的滤镜矩阵。<br>初始值：[]|

### class ImageError

```cangjie
public class ImageError {
    public var componentWidth: Float64
    public var componentHeight: Float64
    public var message: String
}
```

**功能：** 图片加载异常时触发回调的返回对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var componentHeight

```cangjie
public var componentHeight: Float64
```

**功能：** 组件的高度，单位为px。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var componentWidth

```cangjie
public var componentWidth: Float64
```

**功能：** 组件的宽度，单位为px。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var message

```cangjie
public var message: String
```

**功能：** 错误信息。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22
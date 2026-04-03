## class Component

```cangjie
public class Component {
    public let componentType: ComponentType
    public let rowStride: Int32
    public let pixelStride: Int32
    public let byteBuffer: Array<UInt8>
}
```

**功能：** 描述图像颜色分量。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### let byteBuffer

```cangjie
public let byteBuffer: Array<UInt8>
```

**功能：** 组件缓冲区。

**类型：** Array\<UInt8>

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### let componentType

```cangjie
public let componentType: ComponentType
```

**功能：** 组件类型。

**类型：** [ComponentType](#enum-componenttype)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### let pixelStride

```cangjie
public let pixelStride: Int32
```

**功能：** 像素间距。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### let rowStride

```cangjie
public let rowStride: Int32
```

**功能：** 行距。读取相机预览流数据时，需要按stride进行读取，使用详情请参考[相机预览花屏解决方案](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-deal-stride-solution)。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22
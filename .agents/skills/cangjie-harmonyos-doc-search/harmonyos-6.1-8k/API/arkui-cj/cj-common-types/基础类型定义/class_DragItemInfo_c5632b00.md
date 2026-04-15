## class DragItemInfo

```cangjie
public class DragItemInfo {
    public var pixelMap: ?PixelMap
    public var builder: ?CustomBuilder
    public var extraInfo: ?String
    public init(pixelMap: ?PixelMap, builder: ?CustomBuilder, extraInfo: ?String)
}
```

**功能：** 拖拽过程中显示的组件信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var builder

```cangjie
public var builder: ?CustomBuilder
```

**功能：** 使用自定义的生成器进行绘图，如果设置了pixelMap，则该值无效。

**类型：** ?[CustomBuilder](./cj-common-types.md#type-custombuilder)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var extraInfo

```cangjie
public var extraInfo: ?String
```

**功能：** 配置拖拽项的描述。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var pixelMap

```cangjie
public var pixelMap: ?PixelMap
```

**功能：** 设置拖拽过程中显示的图片。

**类型：** ?[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?PixelMap, ?CustomBuilder, ?String)

```cangjie
public init(pixelMap: ?PixelMap, builder: ?CustomBuilder, extraInfo: ?String)
```

**功能：** 创建一个DragItemInfo类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pixelMap|?[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|是|-|设置拖拽过程中显示的图片。|
|builder|?[CustomBuilder](./cj-common-types.md#type-custombuilder)|是|-|使用自定义生成器进行绘图，如果设置了pixelMap，则忽略此值。|
|extraInfo|?String|是|-|拖拽项的描述。|
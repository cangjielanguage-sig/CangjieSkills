### class DragInfo

```cangjie
public class DragInfo {
    public DragInfo(
        public var extraParams: String,
        public var dragEvent: Position
    )
}
```

**功能：** 拖拽动作参数配置类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var dragEvent

```cangjie
public var dragEvent: Position
```

**功能：** 存储拖拽点坐标信息。

**类型：** [Position](./cj-common-types.md#class-position)

**读写能力：** 可读写

**起始版本：** 12

#### var extraParams

```cangjie
public var extraParams: String
```

**功能：** 存储拖拽事件额外信息。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

#### DragInfo(String, Position)

```cangjie
public DragInfo(
    public var extraParams: String,
    public var dragEvent: Position
)
```

**功能：** 创建一个DragInfo类型的对象。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|extraParams|String|是|-|拖拽事件额外信息。|
|dragEvent|[Position](./cj-common-types.md#class-position)|是|-| 拖拽事件信息，包括拖拽点坐标。|

> **说明：**
>
> - extraParams为拖拽事件额外信息，由拖拽组件设置。
> - extraParams的内容是Json转换的String字符串。
> - 当拖拽事件设在父容器的子元素时，selectedIndex表示当前被拖拽子元素是父容器第selectedIndex个子元素，selectedIndex从0开始。
> - 当前拖拽元素在List组件中放下时，insertIndex表示被拖拽元素插入该组件的第insertIndex个位置，insertIndex从0开始。

### struct DragItemInfo

```cangjie
public struct DragItemInfo {
    public DragItemInfo(
        public var pixelMap!: Option<PixelMap> = Option.None ,
        public var builder!: Option<() -> Unit> = Option.None,
        public var extraInfo!: String = ""
    )
}
```

**功能：** 拖拽过程中显示的组件信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var builder

```cangjie
public var builder: Option<() -> Unit> = Option.None
```

**功能：** 使用自定义的生成器进行绘图，如果设置了pixelMap，则该值无效。

**类型：** Option\<()->Unit>

**读写能力：** 可读写

**起始版本：** 12

#### var extraInfo

```cangjie
public var extraInfo: String = ""
```

**功能：** 配置拖拽项的描述。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

#### var pixelMap

```cangjie
public var pixelMap: Option<PixelMap> = Option.None
```

**功能：** 设置拖拽过程中显示的图片。

**类型：** Option\<[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)>

**读写能力：** 可读写

**起始版本：** 12

#### DragItemInfo(Option\<PixelMap>, Option\<() -> Unit>, String)

```cangjie
public DragItemInfo(
    public var pixelMap!: Option<PixelMap> = Option.None ,
    public var builder!: Option<() -> Unit> = Option.None,
    public var extraInfo!: String = ""
)
```

**功能：** 创建一个DragItemInfo类型的对象。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pixelMap|Option\<[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)>|否|Option.None| **命名参数。** 设置拖拽过程中显示的图片。|
|builder|Option\<()->Unit>|否|Option.None| **命名参数。** 使用自定义生成器进行绘图，如果设置了pixelMap，则忽略此值。|
|extraInfo|String|否|""| **命名参数。** 拖拽项的描述。|
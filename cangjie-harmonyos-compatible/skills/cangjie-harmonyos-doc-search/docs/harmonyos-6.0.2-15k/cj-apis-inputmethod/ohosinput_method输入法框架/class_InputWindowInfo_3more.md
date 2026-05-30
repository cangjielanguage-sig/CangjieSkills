## class InputWindowInfo

```cangjie
public class InputWindowInfo {
    public InputWindowInfo(
        public let name: String,
        public let left: Int32,
        public let top: Int32,
        public let width: Int32,
        public let height: Int32
    )
}
```

**功能：** 输入法软键盘的窗口信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### let height

```cangjie
public let height: Int32
```

**功能：** 输入法窗口的高度，单位为px。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let left

```cangjie
public let left: Int32
```

**功能：** 输入法窗口左上顶点的横坐标，单位为px。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let name

```cangjie
public let name: String
```

**功能：** 输入法窗口的名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let top

```cangjie
public let top: Int32
```

**功能：** 输入法窗口左上顶点的纵坐标，单位为px。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let width

```cangjie
public let width: Int32
```

**功能：** 输入法窗口的宽度，单位为px。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### InputWindowInfo(String, Int32, Int32, Int32, Int32)

```cangjie
public InputWindowInfo(
    public let name: String,
    public let left: Int32,
    public let top: Int32,
    public let width: Int32,
    public let height: Int32
)
```

**功能：** 构建输入法软键盘的窗口信息的对象。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|输入法窗口的名称。|
|left|Int32|是|-|输入法窗口左上顶点的横坐标，单位为px。|
|top|Int32|是|-|输入法窗口左上顶点的纵坐标，单位为px。|
|width|Int32|是|-|输入法窗口的宽度，单位为px。|
|height|Int32|是|-|输入法窗口的高度，单位为px。|

## class Movement

```cangjie
public class Movement {
    public Movement(
        public let direction: Direction
    )
}
```

**功能：** 选中文本时，光标移动的方向。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### let direction

```cangjie
public let direction: Direction
```

**功能：** 选中文本时，光标的移动方向。

**类型：** [Direction](../LocalizationKit/cj-apis-resource_manager.md#enum-direction)

**读写能力：** 只读

**起始版本：** 19

### Movement(Direction)

```cangjie
public Movement(
    public let direction: Direction
)
```

**功能：** 构建选中文本时光标移动的方向的对象。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|direction|[Direction](../LocalizationKit/cj-apis-resource_manager.md#enum-direction)|是|-|选中文本时，光标的移动方向。|

## class Range

```cangjie
public class Range {
    public Range(
        public let start: Int32,
        public let end: Int32
    )
}
```

**功能：** 文本的选中范围。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

### let end

```cangjie
public let end: Int32
```

**功能：** 选中文本的末字符在编辑框的索引值。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let start

```cangjie
public let start: Int32
```

**功能：** 选中文本的首字符在编辑框的索引值。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### Range(Int32, Int32)

```cangjie
public Range(
    public let start: Int32,
    public let end: Int32
)
```

**功能：** 构建文本的选中范围的对象。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|Int32|是|-|选中文本的首字符在编辑框的索引值。|
|end|Int32|是|-|选中文本的末字符在编辑框的索引值。|
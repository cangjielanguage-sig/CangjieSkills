## class CastDisplayInfo

```cangjie
public class CastDisplayInfo {
    public CastDisplayInfo(
        public var id: UInt64,
        public var name: String,
        public var state: CastDisplayState,
        public var width: Int32,
        public var height: Int32
    )
}
```

**功能：** 扩展屏投播显示设备相关属性。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**起始版本：** 19

### var height

```cangjie
public var height: Int32
```

**功能：** 投播显示设备的屏幕高度，单位为px。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var id

```cangjie
public var id: UInt64
```

**功能：** 投播显示设备的ID。

**类型：** UInt64

**读写能力：** 可读写

**起始版本：** 19

### var name

```cangjie
public var name: String
```

**功能：** 投播显示设备的名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var state

```cangjie
public var state: CastDisplayState
```

**功能：** 投播显示设备状态。

**类型：** [CastDisplayState](#enum-castdisplaystate)

**读写能力：** 可读写

**起始版本：** 19

### var width

```cangjie
public var width: Int32
```

**功能：** 投播显示设备的屏幕宽度，单位为px。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### CastDisplayInfo(UInt64, String, CastDisplayState, Int32, Int32)

```cangjie
public CastDisplayInfo(
    public var id: UInt64,
    public var name: String,
    public var state: CastDisplayState,
    public var width: Int32,
    public var height: Int32
)
```

**功能：** [CastDisplayInfo](#class-castdisplayinfo)构造函数。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|UInt64|是|-|投播显示设备的ID。|
|name|String|是|-|投播显示设备的名称。|
|state|[CastDisplayState](#enum-castdisplaystate)|是|-|投播显示设备状态。|
|width|Int32|是|-|投播显示设备的屏幕宽度，单位为px。|
|height|Int32|是|-|投播显示设备的屏幕高度，单位为px。|
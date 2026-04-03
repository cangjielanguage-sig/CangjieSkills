## class CallMetadata

```cangjie
public class CallMetadata {
    public CallMetadata (
        public var name: ?String,
        public var phoneNumber: ?String,
        public var avatar: ?PixelMap
    )
    public init()
}
```

**功能：** 通话会话元数据相关属性。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

### var avatar

```cangjie
public var avatar: ?PixelMap
```

**功能：** 来电人头像。

**类型：** ?[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)

**读写能力：** 可读写

**起始版本：** 19

### var name

```cangjie
public var name: ?String
```

**功能：** 来电人姓名（别名）。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var phoneNumber

```cangjie
public var phoneNumber: ?String
```

**功能：** 来电电话号码。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### CallMetadata(?String, ?String, ?PixelMap)

```cangjie
public CallMetadata (
    public var name: ?String,
    public var phoneNumber: ?String,
    public var avatar: ?PixelMap
)
```

**功能：** [CallMetadata](#class-callmetadata)构造函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|?String|是|-|来电人姓名（别名）。|
|phoneNumber|?String|是|-|来电电话号码。|
|avatar|?[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|是|-|来电人头像。|

### init()

```cangjie
public init()
```

**功能：** [CallMetadata](#class-callmetadata)构造函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19
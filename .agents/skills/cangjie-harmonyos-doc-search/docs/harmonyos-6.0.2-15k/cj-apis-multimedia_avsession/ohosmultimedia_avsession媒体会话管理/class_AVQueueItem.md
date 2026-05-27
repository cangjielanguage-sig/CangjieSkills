## class AVQueueItem

```cangjie
public class AVQueueItem {
    public AVQueueItem(
        public var itemId: Int32,
        public var description: ?AVMediaDescription
    )
    public init(itemId: Int32)
}
```

**功能：** 播放列表中单项的相关属性。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

### var description

```cangjie
public var description: ?AVMediaDescription
```

**功能：** 播放列表中单项的媒体元数据。

**类型：** ?[AVMediaDescription](#class-avmediadescription)

**读写能力：** 可读写

**起始版本：** 19

### var itemId

```cangjie
public var itemId: Int32
```

**功能：** 播放列表中单项的ID。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### AVQueueItem(Int32, ?AVMediaDescription)

```cangjie
public AVQueueItem(
    public var itemId: Int32,
    public var description: ?AVMediaDescription
)
```

**功能：** [AVQueueItem](#class-avqueueitem)构造函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|itemId|Int32|是|-|播放列表中单项的ID。|
|description|?[AVMediaDescription](#class-avmediadescription)|是|-|播放列表中单项的媒体元数据。|

### init(Int32)

```cangjie
public init(itemId: Int32)
```

**功能：** [AVQueueItem](#class-avqueueitem)构造函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|itemId|Int32|是|-|播放列表中单项的媒体元数据。|
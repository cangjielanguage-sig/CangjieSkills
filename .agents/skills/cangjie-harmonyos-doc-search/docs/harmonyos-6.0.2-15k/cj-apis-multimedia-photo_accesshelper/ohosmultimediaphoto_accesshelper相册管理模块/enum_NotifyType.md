## enum NotifyType

```cangjie
public enum NotifyType <: Equatable<NotifyType> & ToString {
    | NOTIFY_ADD
    | NOTIFY_UPDATE
    | NOTIFY_REMOVE
    | NOTIFY_ALBUM_ADD_ASSET
    | NOTIFY_ALBUM_REMOVE_ASSET
    | ...
}
```

**功能：** 通知事件的类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**父类型：**

- Equatable\<NotifyType>
- ToString

### NOTIFY_ADD

```cangjie
NOTIFY_ADD
```

**功能：** 添加文件集或相册通知的类型。

**起始版本：** 19

### NOTIFY_ALBUM_ADD_ASSET

```cangjie
NOTIFY_ALBUM_ADD_ASSET
```

**功能：** 在相册中添加的文件集的通知类型。

**起始版本：** 19

### NOTIFY_ALBUM_REMOVE_ASSET

```cangjie
NOTIFY_ALBUM_REMOVE_ASSET
```

**功能：** 在相册中删除的文件集的通知类型。

**起始版本：** 19

### NOTIFY_REMOVE

```cangjie
NOTIFY_REMOVE
```

**功能：** 删除文件集或相册的通知类型。

**起始版本：** 19

### NOTIFY_UPDATE

```cangjie
NOTIFY_UPDATE
```

**功能：** 文件集或相册的更新通知类型。

**起始版本：** 19

### func !=(NotifyType)

```cangjie
public operator func !=(other: NotifyType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[NotifyType](#enum-notifytype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(NotifyType)

```cangjie
public operator func ==(other: NotifyType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[NotifyType](#enum-notifytype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|
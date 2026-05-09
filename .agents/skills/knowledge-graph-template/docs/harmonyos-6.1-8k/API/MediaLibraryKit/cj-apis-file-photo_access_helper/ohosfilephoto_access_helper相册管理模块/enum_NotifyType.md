## enum NotifyType

```cangjie
public enum NotifyType <: Equatable<NotifyType> & ToString {
    | NotifyAdd
    | NotifyUpdate
    | NotifyRemove
    | NotifyAlbumAddAsset
    | NotifyAlbumRemoveAsset
    | ...
}
```

**功能：** 枚举，通知事件的类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**父类型：**

- Equatable\<NotifyType>
- ToString

### NotifyAdd

```cangjie
NotifyAdd
```

**功能：** 添加文件集或相册通知的类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### NotifyAlbumAddAsset

```cangjie
NotifyAlbumAddAsset
```

**功能：** 在相册中添加的文件集的通知类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### NotifyAlbumRemoveAsset

```cangjie
NotifyAlbumRemoveAsset
```

**功能：** 在相册中删除的文件集的通知类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### NotifyRemove

```cangjie
NotifyRemove
```

**功能：** 删除文件集或相册的通知类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### NotifyUpdate

```cangjie
NotifyUpdate
```

**功能：** 文件集或相册的更新通知类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### func !=(NotifyType)

```cangjie
public operator func !=(other: NotifyType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

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

**起始版本：** 22

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

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|
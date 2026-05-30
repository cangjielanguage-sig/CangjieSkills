## enum ResourceType

```cangjie
public enum ResourceType <: Equatable<ResourceType> & ToString {
    | IMAGE_RESOURCE
    | VIDEO_RESOURCE
    | ...
}
```

**功能：** 表示图片资源。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**父类型：**

- Equatable\<ResourceType>
- ToString

### IMAGE_RESOURCE

```cangjie
IMAGE_RESOURCE
```

**功能：** 表示图片资源。

**起始版本：** 19

### VIDEO_RESOURCE

```cangjie
VIDEO_RESOURCE
```

**功能：** 表示视频资源。

**起始版本：** 19

### func !=(ResourceType)

```cangjie
public operator func !=(other: ResourceType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ResourceType](#enum-resourcetype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(ResourceType)

```cangjie
public operator func ==(other: ResourceType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ResourceType](#enum-resourcetype)|是|-|另一个枚举值。|

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
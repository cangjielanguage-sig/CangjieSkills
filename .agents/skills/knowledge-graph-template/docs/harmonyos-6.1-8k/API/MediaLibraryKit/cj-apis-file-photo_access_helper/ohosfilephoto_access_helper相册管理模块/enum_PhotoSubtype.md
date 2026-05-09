## enum PhotoSubtype

```cangjie
public enum PhotoSubtype <: Equatable<PhotoSubtype> & ToString {
    | Default
    | MovingPhoto
    | Burst
    | ...
}
```

**功能：** PhotoSubtype是不同[PhotoAsset](#class-photoasset)类型的枚举。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**父类型：**

- Equatable\<PhotoSubtype>
- ToString

### Burst

```cangjie
Burst
```

**功能：** 连拍照片文件类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### Default

```cangjie
Default
```

**功能：** 默认照片类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### MovingPhoto

```cangjie
MovingPhoto
```

**功能：** 动态照片文件类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### func !=(PhotoSubtype)

```cangjie
public operator func !=(other: PhotoSubtype): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PhotoSubtype](#enum-photosubtype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(PhotoSubtype)

```cangjie
public operator func ==(other: PhotoSubtype): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PhotoSubtype](#enum-photosubtype)|是|-|另一个枚举值。|

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
## struct PickerResult

```cangjie
public struct PickerResult {
    public let resultCode: Int32
    public let resultUri: String
    public let mediaType: PickerMediaType
}
```

**功能：** 相机选择器的处理结果。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### let mediaType

```cangjie
public let mediaType: PickerMediaType
```

**功能：** 返回的媒体类型。

**类型：** [PickerMediaType](#enum-pickermediatype)

**读写能力：** 只读

**起始版本：** 19

### let resultCode

```cangjie
public let resultCode: Int32
```

**功能：** 处理的结果，成功返回0，失败返回-1。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let resultUri

```cangjie
public let resultUri: String
```

**功能：** 返回的uri地址。若saveUri为空，resultUri为公共媒体路径。若saveUri不为空且具备写权限，resultUri与saveUri相同。若saveUri不为空且不具备写权限，则无法获取到resultUri。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

## enum PickerMediaType

```cangjie
public enum PickerMediaType <: ToString & Equatable<PickerMediaType> {
    | PHOTO
    | VIDEO
    | ...
}
```

**功能：** 相机选择器的媒体类型。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<PickerMediaType>

### PHOTO

```cangjie
PHOTO
```

**功能：** 拍照模式。

**起始版本：** 19

### VIDEO

```cangjie
VIDEO
```

**功能：** 录制模式。

**起始版本：** 19

### func !=(PickerMediaType)

```cangjie
public operator func !=(other: PickerMediaType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PickerMediaType](#enum-pickermediatype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(PickerMediaType)

```cangjie
public operator func ==(other: PickerMediaType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PickerMediaType](#enum-pickermediatype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString()
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

| 类型                  | 说明                     |
| :--------------------- | :------------------------ |
| String | 枚举的说明。 |
## enum KeyOfCallMetadata

```cangjie
public enum KeyOfCallMetadata <: Equatable<KeyOfCallMetadata> {
    | KEY_OF_CALLMETADATA_NAME
    | KEY_OF_CALLMETADATA_PHONENUMBER
    | KEY_OF_CALLMETADATA_AVATAR
    | ...
}
```

**功能：** 通话会话元数据相关属性。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**父类型：**

- Equatable\<[KeyOfCallMetadata](#enum-keyofcallmetadata)>

### KEY_OF_CALLMETADATA_AVATAR

```cangjie
KEY_OF_CALLMETADATA_AVATAR
```

**功能：** 来电人头像。

**起始版本：** 19

### KEY_OF_CALLMETADATA_NAME

```cangjie
KEY_OF_CALLMETADATA_NAME
```

**功能：** 来电人姓名（别名）。

**起始版本：** 19

### KEY_OF_CALLMETADATA_PHONENUMBER

```cangjie
KEY_OF_CALLMETADATA_PHONENUMBER
```

**功能：** 来电电话号码。

**起始版本：** 19

### func !=(KeyOfCallMetadata)

```cangjie
public operator func !=(other: KeyOfCallMetadata): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[KeyOfCallMetadata](#enum-keyofcallmetadata)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(KeyOfCallMetadata)

```cangjie
public operator func ==(other: KeyOfCallMetadata): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[KeyOfCallMetadata](#enum-keyofcallmetadata)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表示。|
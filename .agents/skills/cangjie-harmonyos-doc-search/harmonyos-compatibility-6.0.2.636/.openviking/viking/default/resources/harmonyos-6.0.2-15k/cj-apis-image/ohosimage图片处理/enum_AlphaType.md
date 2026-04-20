## enum AlphaType

```cangjie
public enum AlphaType <: Equatable<AlphaType> & ToString {
    | UNKNOWN
    | OPAQUE
    | PREMUL
    | UNPREMUL
    | ...
}
```

**功能：** 图像的透明度类型。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**父类型：**

- Equatable\<AlphaType>
- ToString

### OPAQUE

```cangjie
OPAQUE
```

**功能：** 没有alpha或图片不透明。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### PREMUL

```cangjie
PREMUL
```

**功能：** RGB前乘alpha。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** 未知透明度。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### UNPREMUL

```cangjie
UNPREMUL
```

**功能：** RGB不前乘alpha。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### func !=(AlphaType)

```cangjie
public operator func !=(other: AlphaType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AlphaType](#enum-alphatype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(AlphaType)

```cangjie
public operator func ==(other: AlphaType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AlphaType](#enum-alphatype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|
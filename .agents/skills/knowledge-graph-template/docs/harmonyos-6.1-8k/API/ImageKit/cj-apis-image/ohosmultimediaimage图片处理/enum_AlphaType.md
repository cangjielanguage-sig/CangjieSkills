## enum AlphaType

```cangjie
public enum AlphaType <: Equatable<AlphaType> & ToString {
    | Unknown
    | Opaque
    | Premul
    | UnPremul
    | ...
}
```

**功能：** 枚举，图像的透明度类型。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**父类型：**

- Equatable\<AlphaType>
- ToString

### Opaque

```cangjie
Opaque
```

**功能：** 没有alpha或图片不透明。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### Premul

```cangjie
Premul
```

**功能：** RGB预乘alpha。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### UnPremul

```cangjie
UnPremul
```

**功能：** RGB非预乘alpha。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### Unknown

```cangjie
Unknown
```

**功能：** 未知透明度。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### func !=(AlphaType)

```cangjie
public operator func !=(other: AlphaType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

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

**起始版本：** 22

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

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|
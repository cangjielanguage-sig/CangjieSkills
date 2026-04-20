## enum AntiAliasingLevel

```cangjie
public enum AntiAliasingLevel <: Equatable<AntiAliasingLevel> & ToString {
    | NONE
    | LOW
    | MEDIUM
    | HIGH
    | ...
}
```

**功能：** 缩放时的缩放算法。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**父类型：**

- Equatable\<AntiAliasingLevel>
- ToString

### HIGH

```cangjie
HIGH
```

**功能：** cubic缩放算法。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### LOW

```cangjie
LOW
```

**功能：** 双线性缩放算法。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### MEDIUM

```cangjie
MEDIUM
```

**功能：** 双线性缩放算法，同步开启mipmap。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### NONE

```cangjie
NONE
```

**功能：** 默认为最近邻缩放算法。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### func !=(AntiAliasingLevel)

```cangjie
public operator func !=(other: AntiAliasingLevel): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AntiAliasingLevel](#enum-antialiasinglevel)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(AntiAliasingLevel)

```cangjie
public operator func ==(other: AntiAliasingLevel): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AntiAliasingLevel](#enum-antialiasinglevel)|是|-|另一个枚举值。|

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

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|
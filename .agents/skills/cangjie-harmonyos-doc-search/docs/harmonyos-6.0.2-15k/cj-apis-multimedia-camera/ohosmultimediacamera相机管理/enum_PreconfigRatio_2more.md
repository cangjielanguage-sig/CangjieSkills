## enum PreconfigRatio

```cangjie
public enum PreconfigRatio <: Equatable<PreconfigRatio> & ToString {
    | PRECONFIG_RATIO_1_1
    | PRECONFIG_RATIO_4_3
    | PRECONFIG_RATIO_16_9
    | ...
}
```

**功能：** 提供预配置的分辨率比例。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- Equatable\<PreconfigRatio>
- ToString

### PRECONFIG_RATIO_16_9

```cangjie
PRECONFIG_RATIO_16_9
```

**功能：** 16:9画幅。

**起始版本：** 19

### PRECONFIG_RATIO_1_1

```cangjie
PRECONFIG_RATIO_1_1
```

**功能：** 1:1画幅。

**起始版本：** 19

### PRECONFIG_RATIO_4_3

```cangjie
PRECONFIG_RATIO_4_3
```

**功能：** 4:3画幅。

**起始版本：** 19

### func !=(PreconfigRatio)

```cangjie
public operator func !=(other: PreconfigRatio): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PreconfigRatio](#enum-preconfigratio)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(PreconfigRatio)

```cangjie
public operator func ==(other: PreconfigRatio): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PreconfigRatio](#enum-preconfigratio)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|

## enum PreconfigType

```cangjie
public enum PreconfigType <: Equatable<PreconfigType> & ToString {
    | PRECONFIG_720P
    | PRECONFIG_1080P
    | PRECONFIG_4K
    | PRECONFIG_HIGH_QUALITY
    | ...
}
```

**功能：** 提供预配置的类型。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- Equatable\<PreconfigType>
- ToString

### PRECONFIG_1080P

```cangjie
PRECONFIG_1080P
```

**功能：** 1080P预配置。

**起始版本：** 19

### PRECONFIG_4K

```cangjie
PRECONFIG_4K
```

**功能：** 4K预配置。

**起始版本：** 19

### PRECONFIG_720P

```cangjie
PRECONFIG_720P
```

**功能：** 720P预配置。

**起始版本：** 19

### PRECONFIG_HIGH_QUALITY

```cangjie
PRECONFIG_HIGH_QUALITY
```

**功能：** 高质量预配置。

**起始版本：** 19

### func !=(PreconfigType)

```cangjie
public operator func !=(other: PreconfigType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PreconfigType](#enum-preconfigtype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(PreconfigType)

```cangjie
public operator func ==(other: PreconfigType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[PreconfigType](#enum-preconfigtype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|
## enum RecommendationType

```cangjie
public enum RecommendationType <: Equatable<RecommendationType> & ToString {
    | QR_OR_BAR_CODE
    | QR_CODE
    | BAR_CODE
    | ID_CARD
    | PROFILE_PICTURE
    | PASSPORT
    | BANK_CARD
    | DRIVER_LICENSE
    | DRIVING_LICENSE
    | FEATURED_SINGLE_PORTRAIT
    | ...
}
```

**功能：** 推荐的图片类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**父类型：**

- Equatable\<RecommendationType>
- ToString

### BANK_CARD

```cangjie
BANK_CARD
```

**功能：** 银行卡。

**起始版本：** 19

### BAR_CODE

```cangjie
BAR_CODE
```

**功能：** 条码。

**起始版本：** 19

### DRIVER_LICENSE

```cangjie
DRIVER_LICENSE
```

**功能：** 驾驶证。

**起始版本：** 19

### DRIVING_LICENSE

```cangjie
DRIVING_LICENSE
```

**功能：** 行驶证。

**起始版本：** 19

### FEATURED_SINGLE_PORTRAIT

```cangjie
FEATURED_SINGLE_PORTRAIT
```

**功能：** 推荐人像。

**起始版本：** 19

### ID_CARD

```cangjie
ID_CARD
```

**功能：** 身份证。

**起始版本：** 19

### PASSPORT

```cangjie
PASSPORT
```

**功能：** 护照。

**起始版本：** 19

### PROFILE_PICTURE

```cangjie
PROFILE_PICTURE
```

**功能：** 头像。

**起始版本：** 19

### QR_CODE

```cangjie
QR_CODE
```

**功能：** 二维码。

**起始版本：** 19

### QR_OR_BAR_CODE

```cangjie
QR_OR_BAR_CODE
```

**功能：** 二维码或条码。

**起始版本：** 19

### func !=(RecommendationType)

```cangjie
public operator func !=(other: RecommendationType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[RecommendationType](#enum-recommendationtype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(RecommendationType)

```cangjie
public operator func ==(other: RecommendationType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[RecommendationType](#enum-recommendationtype)|是|-|另一个枚举值。|

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
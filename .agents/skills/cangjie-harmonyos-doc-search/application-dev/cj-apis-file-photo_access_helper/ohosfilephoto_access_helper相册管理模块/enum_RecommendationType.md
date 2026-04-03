## enum RecommendationType

```cangjie
public enum RecommendationType <: Equatable<RecommendationType> & ToString {
    | QrOrBarCode
    | QrCode
    | BarCode
    | IdCard
    | ProfilePicture
    | Passport
    | BankCard
    | DriverLicense
    | DrivingLicense
    | FeaturedSinglePortrait
    | ...
}
```

**功能：** 枚举，推荐的图片类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

**父类型：**

- Equatable\<RecommendationType>
- ToString

### BankCard

```cangjie
BankCard
```

**功能：** 银行卡。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### BarCode

```cangjie
BarCode
```

**功能：** 条码。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### DriverLicense

```cangjie
DriverLicense
```

**功能：** 驾驶证。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### DrivingLicense

```cangjie
DrivingLicense
```

**功能：** 行驶证。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### FeaturedSinglePortrait

```cangjie
FeaturedSinglePortrait
```

**功能：** 推荐人像。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### IdCard

```cangjie
IdCard
```

**功能：** 身份证。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### Passport

```cangjie
Passport
```

**功能：** 护照。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### ProfilePicture

```cangjie
ProfilePicture
```

**功能：** 头像。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### QrCode

```cangjie
QrCode
```

**功能：** 二维码。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### QrOrBarCode

```cangjie
QrOrBarCode
```

**功能：** 二维码或条码。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

### func !=(RecommendationType)

```cangjie
public operator func !=(other: RecommendationType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 22

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

**起始版本：** 22

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

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|
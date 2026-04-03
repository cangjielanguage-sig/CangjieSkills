# Rating

一个提供在给定范围内选择评分的组件。

## 子组件

无

## 创建组件

### init(Float64, Bool)

```cangjie
public init(rating!: Float64, indicator!: Bool = false)
```

**功能：** 构造一个在给定范围内选择评分的组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rating|Float64|是|-| **命名参数。** 设置并接收评分值。<br>初始值：0。<br>取值范围： [0, stars] ，小于0取0，大于stars取最大值stars。|
|indicator|Bool|否|false| **命名参数。** 设置评分组件作为指示器使用，不可改变评分。<br>初始值：false，可进行评分。<br>**说明：**<br>indicator=true时，默认组件高度height=12.0.vp，组件width=height * stars。indicator=false时，默认组件高度height=28.0.vp，组件width=height * stars。|

### init(Int64, Bool)

```cangjie
public init(rating!: Int64, indicator!: Bool = false)
```

**功能：** 构造一个在给定范围内选择评分的组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rating|Int64|是|-| **命名参数。** 设置并接收评分值。<br>初始值：0。<br>取值范围： [0, stars] ，小于0取0，大于stars取最大值stars。|
|indicator|Bool|否|false| **命名参数。** 设置评分组件作为指示器使用，不可改变评分。<br>初始值：false，可进行评分。<br>**说明：**<br>indicator=true时，默认组件高度height=12.0.vp，组件width=height * stars。indicator=false时，默认组件高度height=28.0.vp，组件width=height * stars。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。
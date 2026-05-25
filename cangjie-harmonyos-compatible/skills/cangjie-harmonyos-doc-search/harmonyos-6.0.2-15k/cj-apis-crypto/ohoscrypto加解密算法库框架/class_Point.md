## class Point

```cangjie
public class Point {
    public init(x!: BigInt, y!: BigInt)
}
```

**功能：** 指定椭圆曲线上的一个点。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### prop x

```cangjie
public mut prop x: BigInt
```

**功能：** 指定椭圆曲线上，点的x坐标。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** BigInt

**读写能力：** 可读写

**起始版本：** 19

### prop y

```cangjie
public mut prop y: BigInt
```

**功能：** 指定椭圆曲线上，点的y坐标。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** BigInt

**读写能力：** 可读写

**起始版本：** 19

### init(BigInt, BigInt)

```cangjie
public init(x!: BigInt, y!: BigInt)
```

**功能：** 创建Point实例。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|BigInt|是|-| **命名参数。** 指定椭圆曲线上，点的x坐标。|
|y|BigInt|是|-| **命名参数。** 指定椭圆曲线上，点的y坐标。|
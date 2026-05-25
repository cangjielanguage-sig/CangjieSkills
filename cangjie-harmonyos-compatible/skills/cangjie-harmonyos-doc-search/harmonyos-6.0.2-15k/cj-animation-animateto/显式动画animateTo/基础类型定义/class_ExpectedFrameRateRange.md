### class ExpectedFrameRateRange

```cangjie
public class ExpectedFrameRateRange {
    public ExpectedFrameRateRange(
        public var min!: Int32,
        public var max!: Int32,
        public var expected!: Int32
    )
}
```

**功能：** 期望帧率类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var expected

```cangjie
public var expected: Int32
```

**功能：** 设置期望的最优帧率。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

#### var max

```cangjie
public var max: Int32
```

**功能：** 设置期望的最大帧率。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

#### var min

```cangjie
public var min: Int32,
```

**功能：** 设置期望的最小帧率。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

#### ExpectedFrameRateRange(Int32, Int32, Int32)

```cangjie
public ExpectedFrameRateRange(
    public var min!: Int32,
    public var max!: Int32,
    public var expected!: Int32
)
```

**功能：** 创建一个ExpectedFrameRateRange对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|min|Int32|是|-| **命名参数。** 期望的最小帧率,单位为FPS，取值范围为(0, 设备最大帧率]。|
|max|Int32|是|-| **命名参数。** 期望的最大帧率，单位为FPS，取值范围为[min, 设备最大帧率]。|
|expected|Int32|是|-| **命名参数。** 期望的最优帧率，单位为FPS，取值范围为[min, max]。|
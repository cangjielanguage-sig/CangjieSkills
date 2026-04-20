## class BlurOptions

```cangjie
public class BlurOptions {
    public var grayscale: ?VArray<Float32, $2>
    public init(grayscale: ?VArray<Float32, $2>)
}
```

**功能：** 灰阶模糊参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var grayscale

```cangjie
public var grayscale: ?VArray<Float32, $2>
```

**功能：** 灰阶模糊参数，参数取值范围[0, 127]。

**类型：** ?VArray<Float32, $2>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?VArray\<Float32, \$2>)

```cangjie
public init(grayscale: ?VArray<Float32, $2>)
```

**功能：** 构造BlurOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|grayscale|?VArray<Float32, $2>|是|-|灰阶模糊参数，参数取值范围[0, 127]。|
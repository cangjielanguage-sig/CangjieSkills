### class BlurOptions

```cangjie
public class BlurOptions {
    public BlurOptions(public var grayscale: VArray<Float32, $2>)
}
```

**功能：** 灰阶模糊参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var grayscale

```cangjie
public var grayscale: VArray<Float32, $2>
```

**功能：** 灰阶模糊参数，参数取值范围\[0, 127]。

**类型：** VArray\<Float32, $2>

**读写能力：** 可读写

**起始版本：** 12

#### BlurOptions(VArray\<Float32, $2>)

```cangjie
public BlurOptions(public var grayscale: VArray<Float32, $2>)
```

**功能：** 构造BlurOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :---- | :---- | :---- | :---- | :---- |
| grayscale | VArray\<Float32, $2> | 是 | \- | 灰阶模糊参数，参数取值范围\[0, 127]。 |
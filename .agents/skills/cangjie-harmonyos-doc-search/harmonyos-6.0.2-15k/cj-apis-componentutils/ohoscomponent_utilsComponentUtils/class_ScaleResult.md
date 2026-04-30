## class ScaleResult

```cangjie
public class ScaleResult {
    public ScaleResult(
        public let x: Float32,
        public let y: Float32,
        public let z: Float32,
        public let centerX: Float32,
        public let centerY: Float32
    )
}
```

**功能：** 组件缩放信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let centerX

```cangjie
public let centerX: Float32
```

**功能：** 设置变换中心点x轴坐标。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 19

### let centerY

```cangjie
public let centerY: Float32
```

**功能：** 设置变换中心点y轴坐标。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 19

### let x

```cangjie
public let x: Float32
```

**功能：** 设置x轴缩放倍数。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 19

### let y

```cangjie
public let y: Float32
```

**功能：** 设置y轴缩放倍数。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 19

### let z

```cangjie
public let z: Float32
```

**功能：** 设置z轴缩放倍数。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 19

### ScaleResult(Float32, Float32, Float32, Float32, Float32)

```cangjie
public ScaleResult(
    public let x: Float32,
    public let y: Float32,
    public let z: Float32,
    public let centerX: Float32,
    public let centerY: Float32
)
```

**功能：** 构建一个ScaleResult类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|是|-|x轴缩放倍数。<br>单位: px。|
|y|Float32|是|-|y轴缩放倍数。<br>单位: px。|
|z|Float32|是|-|z轴缩放倍数。<br>单位: px。|
|centerX|Float32|是|-|变换中心点x轴坐标。<br>单位: px|
|centerY|Float32|是|-|变换中心点y轴坐标。<br>单位: px|
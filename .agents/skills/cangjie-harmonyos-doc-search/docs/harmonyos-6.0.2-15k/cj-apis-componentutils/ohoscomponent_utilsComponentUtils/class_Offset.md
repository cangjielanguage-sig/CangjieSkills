## class Offset

```cangjie
public class Offset {
    public Offset(
        public let x: Float32,
        public let y: Float32
    )
}
```

**功能：** 坐标信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let x

```cangjie
public let x: Float32
```

**功能：** 设置x点坐标。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 19

### let y

```cangjie
public let y: Float32
```

**功能：** 设置y点坐标。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 19

### Offset(Float32, Float32)

```cangjie
public Offset(
    public let x: Float32,
    public let y: Float32
)
```

**功能：** 构建一个Offset类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|是|-|x点坐标。<br>单位: px。|
|y|Float32|是|-|y点坐标。<br>单位: px。|
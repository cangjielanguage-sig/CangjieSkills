## class Range

```cangjie
public class Range {
    public Range(
        public let min: Int32,
        public let max: Int32
    )
}
```

**功能：** 表示一个类型的范围。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### let max

```cangjie
public let max: Int32
```

**功能：** 范围的最大值。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let min

```cangjie
public let min: Int32
```

**功能：** 范围的最小值。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### Range(Int32, Int32)

```cangjie
public Range(
    public let min: Int32,
    public let max: Int32)
```

**功能：** 构造Range实例。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|min|Int32|是|-|范围的最小值。|
|max|Int32|是|-|范围的最大值。|
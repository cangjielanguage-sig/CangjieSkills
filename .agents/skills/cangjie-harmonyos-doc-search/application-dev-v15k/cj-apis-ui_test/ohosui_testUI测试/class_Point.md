## class Point

```cangjie
public class Point {
    public Point(
        public let x: IntNative,
        public let y: IntNative
    )
}
```

**功能：** 坐标点信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

### let x

```cangjie
public let x: IntNative
```

**功能：** 坐标点的横坐标。

**类型：** IntNative

**读写能力：** 只读

**起始版本：** 12

### let y

```cangjie
public let y: IntNative
```

**功能：** 坐标点的纵坐标。

**类型：** IntNative

**读写能力：** 只读

**起始版本：** 12

### Point(IntNative, IntNative)

```cangjie
public Point(
    public let x: IntNative,
    public let y: IntNative
)
```

**功能：** 创建Point实例。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|IntNative|是|-|坐标点的横坐标。|
|y|IntNative|是|-|坐标点的纵坐标。|
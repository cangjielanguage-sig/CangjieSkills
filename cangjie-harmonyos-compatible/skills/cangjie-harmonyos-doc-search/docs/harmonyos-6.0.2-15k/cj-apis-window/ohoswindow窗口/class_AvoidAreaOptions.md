## class AvoidAreaOptions

```cangjie
public class AvoidAreaOptions {
    public AvoidAreaOptions (
        public var areaType: AvoidAreaType,
        public var area: AvoidArea
    )
}
```

**功能：** 系统规避区变化后返回当前规避区域以及规避区域类型。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

### var areaType

```cangjie
public var areaType: AvoidAreaType
```

**功能：** 表示系统规避区变化后返回的规避区域类型。

**类型：** [AvoidAreaType](#enum-avoidareatype)

**读写能力：** 可读写

**起始版本：** 19

### var area

```cangjie
public var area: AvoidArea
```

**功能：** 表示系统规避区变化后返回的规避区域。

**类型：** [AvoidArea](#class-avoidarea)

**读写能力：** 可读写

**起始版本：** 19

### AvoidAreaOptions(AvoidAreaType, AvoidArea)

```cangjie
public AvoidAreaOptions (
    public var areaType: AvoidAreaType,
    public var area: AvoidArea
)
```

**功能：** 构建一个AvoidAreaOptions类型的对象。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|areaType|[AvoidAreaType](#enum-avoidareatype)|是|-|系统规避区变化后返回的规避区域类型。|
|area|[AvoidArea](#class-avoidarea)|是|-|系统规避区变化后返回的规避区域。|
## enum Capability

```cangjie
public enum Capability <: Equatable<Capability> & ToString {
    | CAPABILITY_RETRIEVE
    | CAPABILITY_TOUCHGUIDE
    | CAPABILITY_KEYEVENTOBSERVER
    | CAPABILITY_ZOOM
    | CAPABILITY_GESTURE
    | ...
}
```

**功能：** 辅助应用能力类型。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**父类型：**

- Equatable\<[Capability](#enum-capability)>
- ToString

### CAPABILITY_GESTURE

```cangjie
CAPABILITY_GESTURE
```

**功能：** 表示具有执行手势动作的能力。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### CAPABILITY_KEYEVENTOBSERVER

```cangjie
CAPABILITY_KEYEVENTOBSERVER
```

**功能：** 表示具有过滤按键事件的能力。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### CAPABILITY_RETRIEVE

```cangjie
CAPABILITY_RETRIEVE
```

**功能：** 表示具有检索窗口内容的能力。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### CAPABILITY_TOUCHGUIDE

```cangjie
CAPABILITY_TOUCHGUIDE
```

**功能：** 表示具有触摸探索模式的能力。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### CAPABILITY_ZOOM

```cangjie
CAPABILITY_ZOOM
```

**功能：** 表示具有控制显示放大的能力。当前版本暂不支持。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### func !=(Capability)

```cangjie
public operator func !=(other: Capability): Bool
```

**功能：** 对应用能力进行判不等。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Capability](#enum-capability)|是|-|应用能力。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|若应用能力不同，返回true，否则返回false。|

### func ==(Capability)

```cangjie
public operator func ==(other: Capability): Bool
```

**功能：** 对应用能力进行判等。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Capability](#enum-capability)|是|-|应用能力。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|若应用能力相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 将应用能力转换为字符串。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|应用能力的字符串表示。|
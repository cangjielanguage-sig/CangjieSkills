## enum FlexAlign

```cangjie
public enum FlexAlign <: Equatable<FlexAlign> {
    | Start
    | Center
    | End
    | SpaceBetween
    | SpaceAround
    | SpaceEvenly
    | ...
}
```

**功能：** Flex容器对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[FlexAlign](#enum-flexalign)>

### Start

```cangjie
Start
```

**功能：** 元素在主轴方向头部对齐，第一个元素与行首对齐，其他元素与前一个对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Center

```cangjie
Center
```

**功能：** 元素在主轴方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### End

```cangjie
End
```

**功能：** 元素在主轴方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### SpaceBetween

```cangjie
SpaceBetween
```

**功能：** Flex主轴方向均匀分配弹性元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### SpaceAround

```cangjie
SpaceAround
```

**功能：** Flex主轴方向均匀分配弹性元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### SpaceEvenly

```cangjie
SpaceEvenly
```

**功能：** Flex主轴方向均匀分配弹性元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离与相邻元素之间距离相同。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(FlexAlign)

```cangjie
public operator func ==(other: FlexAlign): Bool
```

**功能：** 判断两个FlexAlign枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FlexAlign](#enum-flexalign)|是|-|要比较的另一个FlexAlign枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(FlexAlign)

```cangjie
public operator func !=(other: FlexAlign): Bool
```

**功能：** 判断两个FlexAlign枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[FlexAlign](#enum-flexalign)|是|-|要比较的另一个FlexAlign枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|
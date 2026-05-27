### class PickerTextStyle

```cangjie
public class PickerTextStyle {
    public PickerTextStyle(
        public let color: ResourceColor,
        public let font: MyFont
    )
}
```

**功能：** 字体样式配置类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let color

```cangjie
public let color: ResourceColor
```

**功能：** 文本颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 只读

**起始版本：** 19

#### let font

```cangjie
public let font: MyFont
```

**功能：** 文本样式。

**类型：** [MyFont](#class-myfont)

**读写能力：** 只读

**起始版本：** 19

#### PickerTextStyle(ResourceColor, MyFont)

```cangjie
public PickerTextStyle(
    public let color: ResourceColor,
    public let font: MyFont
)
```

**功能：** 构造字体样式配置类型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|文本颜色。|
|font|[MyFont](#class-myfont)|是|-|文本样式。|

### class DatePickerResult

```cangjie
public class DatePickerResult {
    public DatePickerResult(
        public let year: Int64,
        public let month: Int64,
        public let day: Int64
    )
}
```

**功能：** 记录日期选择器弹窗的选择结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### let day

```cangjie
public let day: Int64
```

**功能：** 选中日期的日。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

#### let month

```cangjie
public let month: Int64
```

**功能：** 选中日期的月。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

#### let year

```cangjie
public let year: Int64
```

**功能：** 选中日期的年。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

#### DatePickerResult(Int64, Int64, Int64)

```cangjie
public DatePickerResult(
    public let year: Int64,
    public let month: Int64,
    public let day: Int64
)
```

**功能：** 构造日期选择器弹窗的选中时间结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|year|Int64|是|-|选中日期的年。|
|month|Int64|是|-|选中日期的月。<br>(0~11)，0表示1月，11表示12月。|
|day|Int64|是|-|选中日期的日。|
### class RangeParams<sup>(deprecated)</sup>

```cangjie
public class RangeParams {
    public var singlerange: Array<String>
    public var multirange: Array<Array<String>>
    public var cascaderange: Array<TextCascadePickerRangeContent>
    public init(singlerange: Array<String>)
    public init(multirange: Array<Array<String>>)
    public init(cascaderange: Array<TextCascadePickerRangeContent>)
}
```

**功能：** 数据选择器可选择范围参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var cascaderange

```cangjie
public var cascaderange: Array<TextCascadePickerRangeContent>
```

**功能：** 级联范围参数。

**类型：** Array\<[TextCascadePickerRangeContent](#class-textcascadepickerrangecontent)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var multirange

```cangjie
public var multirange: Array<Array<String>>
```

**功能：** 多范围参数。

**类型：** Array\<Array\<String>>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var singlerange

```cangjie
public var singlerange: Array<String>
```

**功能：** 单范围参数。

**类型：** Array\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Array\<String>)

```cangjie
public init(singlerange: Array<String>)
```

**功能：** 构建数据选择器可选择的范围参数结构。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|singlerange|Array\<String>|是|-|只能选择的一个数据范围。|

#### init(Array\<Array\<String>>)

```cangjie
public init(multirange: Array<Array<String>>)
```

**功能：** 构建数据选择器可选择的范围参数结构。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|multirange|Array\<Array\<String>>|是|-|可以选择的多个数据范围。|

#### init(Array\<TextCascadePickerRangeContent>)

```cangjie
public init(cascaderange: Array<TextCascadePickerRangeContent>)
```

**功能：** 构建数据选择器范围参数结构。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cascaderange|Array\<[TextCascadePickerRangeContent](#class-textcascadepickerrangecontent)>|是|-|可以选择的级联范围。|
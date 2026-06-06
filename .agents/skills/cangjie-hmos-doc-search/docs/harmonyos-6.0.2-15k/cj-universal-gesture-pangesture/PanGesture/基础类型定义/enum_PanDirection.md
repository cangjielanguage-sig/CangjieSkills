### enum PanDirection

```cangjie
public enum PanDirection {
    | None
    | Left
    | Right
    | Horizontal
    | Up
    | Down
    | Vertical
    | All
    | Computed(UInt32)
}
```

**功能：** 拖动手势方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### All

```cangjie
All
```

**功能：** 所有方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Computed(UInt32)

```cangjie
Computed(UInt32)
```

**功能：** 支持逻辑与(&)和逻辑或(|)运算。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Down

```cangjie
Down
```

**功能：** 向下拖动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Horizontal

```cangjie
Horizontal
```

**功能：** 水平方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Left

```cangjie
Left
```

**功能：** 向左拖动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### None

```cangjie
None
```

**功能：** 所有方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Right

```cangjie
Right
```

**功能：** 向右拖动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Up

```cangjie
Up
```

**功能：** 向上拖动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Vertical

```cangjie
Vertical
```

**功能：** 竖直方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### func &(PanDirection)

```cangjie
public operator func &(right: PanDirection): PanDirection
```

**功能：** 对PanDirection进行逻辑与(&)运算。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|right|[PanDirection](#enum-pandirection)|是|-|滑动方向|

**返回值：**

|类型|说明|
|:----|:----|
|[PanDirection](#enum-pandirection)|滑动方向|

#### func |(PanDirection)

```cangjie
public operator func |(right: PanDirection): PanDirection
```

**功能：** 对PanDirection进行逻辑或(|)运算。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|right|[PanDirection](#enum-pandirection)|是|-|滑动方向|

**返回值：**

|类型|说明|
|:----|:----|
|[PanDirection](#enum-pandirection)|滑动方向|
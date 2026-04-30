### func gridColOffset(Int32)

```cangjie
public func gridColOffset(offset: Int32): This
```

**功能：** 设置相对于前一个栅格子组件偏移的列数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Int32|是|-|相对于前一个栅格子组件偏移的列数。<br>取值为大于0的整数，初始值：0。|

### func gridColOffset(GridColColumnOption)

```cangjie
public func gridColOffset(offset: GridColColumnOption): This
```

**功能：** 设置相对于前一个栅格子组件偏移的列数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|[GridColColumnOption](#struct-gridcolcolumnoption)|是|-|相对于前一个栅格子组件偏移的列数。|

### func offset(Int32)

```cangjie
public func offset(offset: Int32): This
```

**功能：** 设置相对于前一个栅格子组件偏移的列数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Int32|是|-|相对于前一个栅格子组件偏移的列数。<br>取值为大于0的整数，初始值：0。|

### func offset(GridColColumnOption)

```cangjie
public func offset(offset: GridColColumnOption): This
```

**功能：** 设置相对于前一个栅格子组件偏移的列数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|[GridColColumnOption](#struct-gridcolcolumnoption)|是|-|相对于前一个栅格子组件偏移的列数。|

### func order(Int32)

```cangjie
public func order(order: Int32): This
```

**功能：** 设置元素的序号，根据栅格子组件的序号，从小到大对栅格子组件做排序。

> **说明：**
>
> - 当子组件不设置order或者设置相同的order，子组件按照代码顺序展示。当子组件部分设置order，部分不设置order时，未设置order的子组件依次排序靠前，设置了order的子组件按照数值从小到大排列。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|order|Int32|是|-|元素的序号。<br>取值为大于0的整数，初始值：0。|

### func order(GridColColumnOption)

```cangjie
public func order(order: GridColColumnOption): This
```

**功能：** 设置元素的序号，根据栅格子组件的序号，从小到大对栅格子组件做排序。

> **说明：**
>
> - 当子组件不设置order或者设置相同的order，子组件按照代码顺序展示。当子组件部分设置order，部分不设置order时，未设置order的子组件依次排序靠前，设置了order的子组件按照数值从小到大排列。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|order|[GridColColumnOption](#struct-gridcolcolumnoption)|是|-|元素的序号。|

### func span(Int32)

```cangjie
public func span(span: Int32): This
```

**功能：** 设置占用列数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|span|Int32|是|-|占用列数。<br>取值为大于0的整数，初始值：0。<br>span为0表示该元素不参与布局计算，即不会被渲染。|
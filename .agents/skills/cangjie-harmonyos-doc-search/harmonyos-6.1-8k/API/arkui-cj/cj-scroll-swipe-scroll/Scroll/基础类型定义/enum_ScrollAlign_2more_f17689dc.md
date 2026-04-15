### enum ScrollAlign

```cangjie
public enum ScrollAlign <: Equatable<ScrollAlign> {
    | Start
    | Center
    | End
    | Auto
    | ...
}
```

**功能：** 枚举对齐模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ScrollAlign](#enum-scrollalign)>

#### Start

```cangjie
Start
```

**功能：** 列表项的起始边缘与列表的起始边缘对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### Center

```cangjie
Center
```

**功能：** 列表项沿列表主轴居中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### End

```cangjie
End
```

**功能：** 列表项的结束边缘与列表的结束边缘对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### Auto

```cangjie
Auto
```

**功能：** 列表项自动对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### operator func !=(ScrollAlign)

```cangjie
public operator func !=(other: ScrollAlign): Bool
```

**功能：** 比较两个枚举值是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ScrollAlign](#enum-scrollalign)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不相等则返回true，否则返回false。|

#### operator func ==(ScrollAlign)

```cangjie
public operator func ==(other: ScrollAlign): Bool
```

**功能：** 比较两个枚举值是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ScrollAlign](#enum-scrollalign)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等则返回true，否则返回false。|

### enum ContentClipMode

```cangjie
public enum ContentClipMode <: Equatable<ContentClipMode> {
    | ContentOnly
    | Boundary
    | SafeArea
    | ...
}
```

**功能：** 枚举内容裁剪模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ContentClipMode](#enum-contentclipmode)>

#### ContentOnly

```cangjie
ContentOnly
```

**功能：** 内容裁剪模式的内容模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### Boundary

```cangjie
Boundary
```

**功能：** 内容裁剪模式的边界模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### SafeArea

```cangjie
SafeArea
```

**功能：** 内容裁剪模式的安全区域模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### operator func !=(ContentClipMode)

```cangjie
public operator func !=(other: ContentClipMode): Bool
```

**功能：** 比较两个枚举值是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ContentClipMode](#enum-contentclipmode)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不相等则返回true，否则返回false。|

#### operator func ==(ContentClipMode)

```cangjie
public operator func ==(other: ContentClipMode): Bool
```

**功能：** 比较两个枚举值是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ContentClipMode](#enum-contentclipmode)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等则返回true，否则返回false。|
## enum HorizontalAlign

```cangjie
public enum HorizontalAlign <: Equatable<HorizontalAlign> {
    | Start
    | Center
    | End
    | ...
}
```

**功能：** 水平方向对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[HorizontalAlign](#enum-horizontalalign)>

### Start

```cangjie
Start
```

**功能：** 按照语言方向起始端对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Center

```cangjie
Center
```

**功能：** 居中对齐。使用默认对齐模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### End

```cangjie
End
```

**功能：** 按照语言方向末端对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(HorizontalAlign)

```cangjie
public operator func ==(other: HorizontalAlign): Bool
```

**功能：** 判断两个HorizontalAlign枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[HorizontalAlign](#enum-horizontalalign)|是|-|要比较的另一个HorizontalAlign枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(HorizontalAlign)

```cangjie
public operator func !=(other: HorizontalAlign): Bool
```

**功能：** 判断两个HorizontalAlign枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[HorizontalAlign](#enum-horizontalalign)|是|-|要比较的另一个HorizontalAlign枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum VerticalAlign

```cangjie
public enum VerticalAlign <: Equatable<VerticalAlign> {
    | Top
    | Center
    | Bottom
    | ...
}
```

**功能：** 垂直方向上对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[VerticalAlign](#enum-verticalalign)>

### Top

```cangjie
Top
```

**功能：** 顶部对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Center

```cangjie
Center
```

**功能：** 居中对齐，默认对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Bottom

```cangjie
Bottom
```

**功能：** 底部对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(VerticalAlign)

```cangjie
public operator func ==(other: VerticalAlign): Bool
```

**功能：** 判断两个VerticalAlign枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[VerticalAlign](#enum-verticalalign)|是|-|要比较的另一个VerticalAlign枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(VerticalAlign)

```cangjie
public operator func !=(other: VerticalAlign): Bool
```

**功能：** 判断两个VerticalAlign枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[VerticalAlign](#enum-verticalalign)|是|-|要比较的另一个VerticalAlign枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|
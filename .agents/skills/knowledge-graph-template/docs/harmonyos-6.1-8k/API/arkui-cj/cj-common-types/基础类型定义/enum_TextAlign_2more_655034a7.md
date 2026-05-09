## enum TextAlign

```cangjie
public enum TextAlign <: Equatable<TextAlign> {
    | Start
    | Center
    | End
    | ...
}
```

**功能：** 文本对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[TextAlign](#enum-textalign)>

### Start

```cangjie
Start
```

**功能：** 水平对齐首部。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Center

```cangjie
Center
```

**功能：** 水平居中对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### End

```cangjie
End
```

**功能：** 水平对齐尾部。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(TextAlign)

```cangjie
public operator func ==(other: TextAlign): Bool
```

**功能：** 判断两个TextAlign枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextAlign](#enum-textalign)|是|-|要比较的另一个TextAlign枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(TextAlign)

```cangjie
public operator func !=(other: TextAlign): Bool
```

**功能：** 判断两个TextAlign枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextAlign](#enum-textalign)|是|-|要比较的另一个TextAlign枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|

## enum TextOverflow

```cangjie
public enum TextOverflow <: Equatable<TextOverflow> {
    | Clip
    | Ellipsis
    | None
    | ...
}
```

**功能：** 文本超长时的显示方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[TextOverflow](#enum-textoverflow)>

### Clip

```cangjie
Clip
```

**功能：** 文本超长时按最大行截断显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Ellipsis

```cangjie
Ellipsis
```

**功能：** 文本超长时显示不下的文本用省略号代替。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### None

```cangjie
None
```

**功能：** 文本超长时按最大行截断显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(TextOverflow)

```cangjie
public operator func ==(other: TextOverflow): Bool
```

**功能：** 判断两个TextOverflow枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextOverflow](#enum-textoverflow)|是|-|要比较的另一个TextOverflow枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(TextOverflow)

```cangjie
public operator func !=(other: TextOverflow): Bool
```

**功能：** 判断两个TextOverflow枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[TextOverflow](#enum-textoverflow)|是|-|要比较的另一个TextOverflow枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|
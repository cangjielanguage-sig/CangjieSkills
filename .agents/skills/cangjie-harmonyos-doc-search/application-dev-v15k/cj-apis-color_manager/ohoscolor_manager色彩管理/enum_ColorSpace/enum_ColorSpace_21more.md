## enum ColorSpace

```cangjie
public enum ColorSpace <: ToString {
    | UNKNOWN
    | ADOBE_RGB_1998
    | DCI_P3
    | DISPLAY_P3
    | SRGB
    | CUSTOM
    | BT709
    | BT601_EBU
    | BT601_SMPTE_C
    | BT2020_HLG
    | BT2020_PQ
    | P3_HLG
    | P3_PQ
    | ADOBE_RGB_1998_LIMIT
    | DISPLAY_P3_LIMIT
    | SRGB_LIMIT
    | BT709_LIMIT
    | BT601_EBU_LIMIT
    | BT601_SMPTE_C_LIMIT
    | BT2020_HLG_LIMIT
    | BT2020_PQ_LIMIT
    | P3_HLG_LIMIT
    | P3_PQ_LIMIT
    | LINEAR_P3
    | LINEAR_SRGB
    | LINEAR_BT709
    | LINEAR_BT2020
    | DISPLAY_SRGB
    | DISPLAY_P3_SRGB
    | DISPLAY_P3_HLG
    | DISPLAY_P3_PQ
    | ...
}
```

**功能：** 色域类型枚举。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 12

**父类型：**

- ToString

### ADOBE_RGB_1998

```cangjie
ADOBE_RGB_1998
```

**功能：** RGB色域为Adobe RGB(1998)类型；转换函数为Adobe RGB(1998)类型；编码范围为Full类型。

**起始版本：** 12

### ADOBE_RGB_1998_LIMIT

```cangjie
ADOBE_RGB_1998_LIMIT
```

**功能：** RGB色域为Adobe RGB(1998)类型；转换函数为Adobe RGB(1998)类型；编码范围为Limit类型。

**起始版本：** 19

### BT2020_HLG

```cangjie
BT2020_HLG
```

**功能：** RGB色域为BT2020类型；转换函数为HLG类型；编码范围为Full类型。

**起始版本：** 19

### BT2020_HLG_LIMIT

```cangjie
BT2020_HLG_LIMIT
```

**功能：** RGB色域为BT2020类型；转换函数为HLG类型；编码范围为Limit类型。

**起始版本：** 19

### BT2020_PQ

```cangjie
BT2020_PQ
```

**功能：** RGB色域为BT2020类型；转换函数为PQ类型；编码范围为Full类型。

**起始版本：** 19

### BT2020_PQ_LIMIT

```cangjie
BT2020_PQ_LIMIT
```

**功能：** RGB色域为BT2020类型；转换函数为PQ类型；编码范围为Limit类型。

**起始版本：** 19

### BT601_EBU

```cangjie
BT601_EBU
```

**功能：** RGB色域为BT601_P类型；转换函数为BT709类型；编码范围为Full类型。

**起始版本：** 19

### BT601_EBU_LIMIT

```cangjie
BT601_EBU_LIMIT
```

**功能：** RGB色域为BT601_P类型；转换函数为BT709类型；编码范围为Limit类型。

**起始版本：** 19

### BT601_SMPTE_C

```cangjie
BT601_SMPTE_C
```

**功能：** RGB色域为BT601_N类型；转换函数为BT709类型；编码范围为Full类型。

**起始版本：** 19

### BT601_SMPTE_C_LIMIT

```cangjie
BT601_SMPTE_C_LIMIT
```

**功能：** RGB色域为BT601_N类型；转换函数为BT709类型；编码范围为Limit类型。

**起始版本：** 19

### BT709

```cangjie
BT709
```

**功能：** RGB色域为BT709类型；转换函数为BT709类型；编码范围为Full类型。

**起始版本：** 19

### BT709_LIMIT

```cangjie
BT709_LIMIT
```

**功能：** RGB色域为BT709类型；转换函数为BT709类型；编码范围为Limit类型。

**起始版本：** 19

### CUSTOM

```cangjie
CUSTOM
```

**功能：** 用户自定义色域类型。

**起始版本：** 19

### DCI_P3

```cangjie
DCI_P3
```

**功能：** RGB色域为DCI-P3类型；转换函数为Gamma 2.6类型；编码范围为Full类型。

**起始版本：** 12

### DISPLAY_P3

```cangjie
DISPLAY_P3
```

**功能：** RGB色域为Display P3类型；转换函数为SRGB类型；编码范围为Full类型。

**起始版本：** 12

### DISPLAY_P3_HLG

```cangjie
DISPLAY_P3_HLG
```

**功能：** 与P3_HLG相同；RGB色域为Display P3类型；转换函数为HLG类型；编码范围为Full类型。

**起始版本：** 19

### DISPLAY_P3_LIMIT

```cangjie
DISPLAY_P3_LIMIT
```

**功能：** RGB色域为Display P3类型；转换函数为SRGB类型；编码范围为Limit类型。

**起始版本：** 19

### DISPLAY_P3_PQ

```cangjie
DISPLAY_P3_PQ
```

**功能：** 与P3_PQ相同；RGB色域为Display P3类型；转换函数为PQ类型；编码范围为Full类型。

**起始版本：** 19

### DISPLAY_P3_SRGB

```cangjie
DISPLAY_P3_SRGB
```

**功能：** 与DISPLAY_P3相同；RGB色域为Display P3类型；转换函数为SRGB类型；编码范围为Full类型。

**起始版本：** 19

### DISPLAY_SRGB

```cangjie
DISPLAY_SRGB
```

**功能：** 与SRGB相同；RGB色域为SRGB类型；转换函数为SRGB类型；编码范围为Full类型。

**起始版本：** 19
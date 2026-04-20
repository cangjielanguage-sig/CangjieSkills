## enum ApplicationType

```cangjie
public enum ApplicationType {
    | BROWSER
    | IMAGE
    | AUDIO
    | VIDEO
    | PDF
    | WORD
    | EXCEL
    | PPT
    | EMAIL
    | ...
}
```

**功能：** 默认应用的应用类型。

**系统能力：** SystemCapability.BundleManager.BundleFramework.DefaultApp

**起始版本：** 19

### AUDIO

```cangjie
AUDIO
```

**功能：** 默认音频播放器。

**起始版本：** 19

### BROWSER

```cangjie
BROWSER
```

**功能：** 默认浏览器。

**起始版本：** 19

### EMAIL

```cangjie
EMAIL
```

**功能：** 默认邮件。

**起始版本：** 19

### EXCEL

```cangjie
EXCEL
```

**功能：** 默认EXCEL文档查看器。

**起始版本：** 19

### IMAGE

```cangjie
IMAGE
```

**功能：** 默认图片查看器。

**起始版本：** 19

### PDF

```cangjie
PDF
```

**功能：** 默认PDF文档查看器。

**起始版本：** 19

### PPT

```cangjie
PPT
```

**功能：** 默认PPT文档查看器。

**起始版本：** 19

### VIDEO

```cangjie
VIDEO
```

**功能：** 默认视频播放器。

**起始版本：** 19

### WORD

```cangjie
WORD
```

**功能：** 默认WORD文档查看器。

**起始版本：** 19

### func getValue()

```cangjie
public func getValue(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.BundleManager.BundleFramework.DefaultApp

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的值。|
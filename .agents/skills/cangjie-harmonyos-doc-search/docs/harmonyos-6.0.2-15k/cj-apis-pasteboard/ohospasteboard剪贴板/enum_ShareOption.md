## enum ShareOption

```cangjie
public enum ShareOption {
    | INAPP
    | LOCALDEVICE
    | CROSSDEVICE
    | ...
}
```

**功能：** 可粘贴数据的范围类型枚举。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

### CROSSDEVICE

```cangjie
CROSSDEVICE
```

**功能：** 表示允许跨设备在任何应用内粘贴。

**起始版本：** 12

### INAPP

```cangjie
INAPP
```

**功能：** 表示仅允许同应用内粘贴。

**起始版本：** 12

### LOCALDEVICE

```cangjie
LOCALDEVICE
```

**功能：** 表示允许在此设备中任何应用内粘贴。

**起始版本：** 12

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|枚举的值。|
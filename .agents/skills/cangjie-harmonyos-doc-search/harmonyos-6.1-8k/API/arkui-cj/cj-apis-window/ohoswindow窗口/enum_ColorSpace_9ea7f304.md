## enum ColorSpace

```cangjie
public enum ColorSpace <: Equatable<ColorSpace> {
    | Default
    | WideGamut
    | ...
}
```

**功能：** 允许指定的颜色空间类型。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**父类型：**

- Equatable\<[ColorSpace](#enum-colorspace)>

### Default

```cangjie
Default
```

**功能：** 默认颜色空间。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### WideGamut

```cangjie
WideGamut
```

**功能：** 宽色域颜色空间。具体宽色域取决于屏幕。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### operator func !=(ColorSpace)

```cangjie
public operator func !=(other: ColorSpace): Bool
```

**功能：** 不等比较运算符。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ColorSpace](#enum-colorspace)|是|-|要比较的另一个ColorSpace实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，不相等时返回true。|

### operator func ==(ColorSpace)

```cangjie
public operator func ==(other: ColorSpace): Bool
```

**功能：** 相等比较运算符。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ColorSpace](#enum-colorspace)|是|-|要比较的另一个ColorSpace实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，相等时返回true。|
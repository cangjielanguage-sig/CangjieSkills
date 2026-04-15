## enum WebDarkMode

```cangjie
public enum WebDarkMode <: Equatable<WebDarkMode> {
    | Off
    | On
    | Auto
    | ...
}
```

**功能：** Web的深色模式，默认关闭。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**父类型：**

- Equatable\<[WebDarkMode](#enum-webdarkmode)>

### Off

```cangjie
Off
```

**功能：** Web的深色模式为关闭。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

### On

```cangjie
On
```

**功能：** Web的深色模式为开启。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

### Auto

```cangjie
Auto
```

**功能：** Web的深色模式为跟随系统。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

### operator func ==(WebDarkMode)

```cangjie
public operator func ==(other: WebDarkMode): Bool
```

**功能：** 判断两个WebDarkMode枚举是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WebDarkMode](#enum-webdarkmode)|是|-|要比较的另一个WebDarkMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(WebDarkMode)

```cangjie
public operator func !=(other: WebDarkMode): Bool
```

**功能：** 判断两个WebDarkMode枚举是否不相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WebDarkMode](#enum-webdarkmode)|是|-|要比较的另一个WebDarkMode枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|
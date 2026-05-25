## enum ToastShowMode

```cangjie
public enum ToastShowMode <: Equatable<ToastShowMode> {
    | Default
    | TopMost
    | ...
}
```

**功能：** Toast显示模式枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ToastShowMode](#enum-toastshowmode)>

### Default

```cangjie
Default
```

**功能：** Toast在应用内显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### TopMost

```cangjie
TopMost
```

**功能：** Toast在顶部显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func !=(ToastShowMode)

```cangjie
public operator func !=(other: ToastShowMode): Bool
```

**功能：** 不等比较运算符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ToastShowMode](#enum-toastshowmode)|是|-|要比较的另一个ToastShowMode实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，不相等时返回true。|

### operator func ==(ToastShowMode)

```cangjie
public operator func ==(other: ToastShowMode): Bool
```

**功能：** 相等比较运算符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ToastShowMode](#enum-toastshowmode)|是|-|要比较的另一个ToastShowMode实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，相等时返回true。|

## type ShowDialogCallBack

```cangjie
public type ShowDialogCallBack = AsyncCallback<Int32>
```

**功能：** ShowDialogCallBack回调函数

**类型：** [AsyncCallback\<Int32>](../arkinterop/cj-api-business_exception.md#type-asynccallbackt)

## type ShowActionMenuCallBack

```cangjie
public type ShowActionMenuCallBack = AsyncCallback<Int32>
```

**功能：** ShowActionMenuCallBack回调函数

**类型：** [AsyncCallback\<Int32>](../arkinterop/cj-api-business_exception.md#type-asynccallbackt)
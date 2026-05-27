### func setOrCreate\<T>(String, T) where T <: JSInteropType \<T>

```cangjie
public func setOrCreate<T>(propName: String, value: T): Bool where T <: JSInteropType<T>
```

**功能：** 设置propName对应属性的值为newValue。

> **说明：**
>
> - 如果propName已经在[LocalStorageInterOp](#class-localstorageinterop)中存在，并且newValue和propName对应属性的值不同，则设置propName对应属性的值为newValue，否则状态变量不会通知UI刷新propName对应属性的值。
> - 如果propName不存在，则创建propName属性，值为newValue。setOrCreate只可以创建单个AppStorage的键值对，如果想创建多个AppStorage键值对，可以多次调用此方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|propName|String|是|-|[LocalStorageInterOp](#class-localstorageinterop)中的属性名。|
|value|T|是|-|属性值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|属性值设置结果。|

### func size()

```cangjie
public func size(): Int64
```

**功能：** 返回[LocalStorageInterOp](#class-localstorageinterop)中的属性数量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int64|[LocalStorageInterOp](#class-localstorageinterop)中属性的数量。|
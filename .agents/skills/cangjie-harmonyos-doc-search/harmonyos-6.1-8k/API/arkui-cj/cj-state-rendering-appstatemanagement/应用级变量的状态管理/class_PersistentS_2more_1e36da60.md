## class PersistentStorage

```cangjie
public class PersistentStorage {}
```

**功能：** PersistentStorage是持久化存储UI状态，通常和AppStorage配合使用，选择AppStorage中的属性持久化到文件中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### static func deleteProp(String)

```cangjie
public static func deleteProp(key: String): Unit
```

**功能：** 删除持久化的属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|要删除的属性键名。|

### static func keys()

```cangjie
public static func keys(): Array<String>
```

**功能：** 获取所有持久化属性的键名。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|返回所有持久化属性的键名数组。|

### static func persistProp\<T>(String, T)

```cangjie
public static func persistProp<T>(key: String, defaultValue: T): Unit
```

**功能：** 持久化指定的AppStorage属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|要持久化的属性键名。|
|defaultValue|T|是|-|属性的默认值。|

### static func persistProps\<T>(Array<(String, T)>)

```cangjie
public static func persistProps<T>(props: Array<(String, T)>): Unit
```

**功能：** 持久化多个AppStorage属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|props|Array\<(String, T)>|是|-|要持久化的属性键值对数组。|

## enum ColorMode

```cangjie
public enum ColorMode <: Equatable<ColorMode> {
    | Light
    | Dark
    | ...
}
```

**功能：** 定义设备的颜色模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[ColorMode](#enum-colormode)>

### Light

```cangjie
Light
```

**功能：** 浅色模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Dark

```cangjie
Dark
```

**功能：** 深色模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func !=(ColorMode)

```cangjie
public operator func !=(other: ColorMode): Bool
```

**功能：** 不等比较运算符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ColorMode](#enum-colormode)|是|-|要比较的另一个ColorMode实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，不相等时返回true。|

### operator func ==(ColorMode)

```cangjie
public operator func ==(other: ColorMode): Bool
```

**功能：** 相等比较运算符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ColorMode](#enum-colormode)|是|-|要比较的另一个ColorMode实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|比较结果，相等时返回true。|
## Environment（设备环境查询）

开发者如果需要应用程序运行的设备的环境参数，以此来作出不同的场景判断，比如多语言，暗黑模式等，需要用到Environment设备环境查询。

Environment是ArkUI框架在应用程序启动时创建的单例对象。它为AppStorage提供了一系列描述应用程序运行状态的属性。Environment的所有属性都是不可变的（即应用不可写入），所有的属性都是简单类型。

### class Environment

```cangjie
public class Environment {}
```

**功能：** 用于获取应用程序运行设备环境参数的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### static func envProp\<T>(String, T)

```cangjie
public static func envProp<T>(key: String, defaultValue: T): Bool
```

**功能：** 将Environment的内置环境变量key存入AppStorage中。如果系统中未查询到Environment环境变量key的值，则使用默认值value，存入成功，返回true。如果AppStorage中已经有对应的key，则返回false。

所以建议在程序启动的时候调用该接口。

在没有调用envProp的情况下，就使用AppStorage读取环境变量是错误的。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|环境变量名称，支持的范围详见内置环境变量说明。|
|defaultValue|T|是|-|查询不到环境变量key，则使用defaultValue作为默认值存入AppStorage中。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果key对应的属性在AppStorage中存在，则返回false。不存在则在AppStorage中用value作为默认值创建key对应的属性，返回true。 |

#### static func keys()

```cangjie
public static func keys(): EquatableCollection<String>
```

**功能：** 返回环境变量的属性key的集合。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|EquatableCollection\<String>|返回关联的系统项集合。|

**示例：**

```cangjie
let a = Environment.envProp("accessibilityEnabled", true)
let b = Environment.envProp("languageCode", "en")
let keys = Environment.keys()
```

### enum ColorMode

```cangjie
public enum ColorMode {
    | Light
    | Dark
}
```

**功能：** 色彩模型类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Dark

```cangjie
Dark
```

**功能：** 深色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Light

```cangjie
Light
```

**功能：** 浅色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### enum LayoutDirection

```cangjie
public enum LayoutDirection {
    | Ltr
    | Rtl
}
```

**功能：** 布局方向类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Ltr

```cangjie
Ltr
```

**功能：** 从左到右。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### Rtl

```cangjie
Rtl
```

**功能：** 从右到左。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12
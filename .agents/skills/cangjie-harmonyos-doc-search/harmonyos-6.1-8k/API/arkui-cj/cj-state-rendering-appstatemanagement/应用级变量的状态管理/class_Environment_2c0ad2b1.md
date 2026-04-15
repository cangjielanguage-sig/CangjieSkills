## class Environment

```cangjie
public class Environment {}
```

**功能：** Environment是和应用的进程绑定的，由UI框架在应用程序启动时创建，为应用程序提供设备环境状态的中心存储。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### static func envProp\<T>(String, T)

```cangjie
public static func envProp<T>(key: String, defaultValue: T): Bool
```

**功能：** 创建一个与设备环境状态同步的属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|环境属性的键名。|
|defaultValue|T|是|-|属性的默认值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果创建成功则返回true，否则返回false。|

### static func keys()

```cangjie
public static func keys(): Array<String>
```

**功能：** 获取所有环境属性的键名。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|返回所有环境属性的键名数组。|
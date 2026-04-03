# ohos.resource_manager（资源管理）

资源管理模块，根据当前configuration：语言、区域、横竖屏、Mcc（移动国家码）和Mnc（移动网络码）、Device capability（设备类型）、Density（分辨率）提供获取应用资源对象读取接口。

## 导入模块

```cangjie
import kit.LocalizationKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func \_\_GenerateResource\_\_(String, String, String, Int32, String, Array\<Any>, Int32)

```cangjie
public func __GenerateResource__(
    bundleName: String,
    moudleType: String,
    moduleName: String,
    resId: Int32,
    resStr: String,
    params: Array<Any>,
    resType: Int32
): AppResource
```

**功能：** 资源管理宏使用。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bundleName|String|是|-|应用的包名称。|
|moudleType|String|是|-|应用的模块类型。|
|moduleName|String|是|-|应用的模块名称。|
|resId|Int32|是|-|资源id。|
|resStr|String|是|-|资源名称。|
|params|Array\<Any>|是|-|其他资源参数。|
|resType|Int32|是|-|资源的类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[AppResource](#class-appresource)|资源类型。|
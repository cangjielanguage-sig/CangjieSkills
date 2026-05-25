# ohos.geo_location_manager（位置服务）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

geo_location_manager模块提供GNSS定位、网络定位（蜂窝基站、WLAN、蓝牙定位技术）等基本功能。

使用位置服务时请打开设备“位置”开关。如果“位置”开关关闭并且代码未设置捕获异常，可能导致应用异常。

> **说明：**
>
> 本模块能力仅支持WGS-84坐标系。

## 导入模块

```cangjie
import kit.LocationKit.*
```

## 申请权限

请参考[申请位置权限开发指导](../../location/cj-location-permission-guidelines.md#开发步骤)

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。
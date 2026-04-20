# 获取设备的位置信息开发指导

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

## 场景概述

开发者可以调用位置相关接口，获取设备实时位置或最近的历史位置，以及监听设备的位置变化。

对于位置敏感的应用业务，建议获取设备实时位置信息。如果不需要设备实时位置信息，并且希望尽可能地节省耗电，开发者可以考虑获取最近的历史位置。

## 接口说明

获取设备的位置信息所使用的接口如下，详细说明参见：[Location Kit](../reference/LocationKit/cj-apis-geo_location_manager.md)。

本模块能力仅支持WGS-84坐标系。

| 接口名 | 功能描述 |
| -------- | -------- |
| [getCurrentLocation()](../reference/LocationKit/cj-apis-geo_location_manager.md#static-func-getcurrentlocation) | 获取当前位置。|
| [getCurrentLocation(CurrentLocationRequest)](../reference/LocationKit/cj-apis-geo_location_manager.md#static-func-getcurrentlocationcurrentlocationrequest) | 获取当前位置。|
| [getCurrentLocation(SingleLocationRequest)](../reference/LocationKit/cj-apis-geo_location_manager.md#static-func-getcurrentlocationsinglelocationrequest) | 获取当前位置。|
| [isLocationEnabled()](../reference/LocationKit/cj-apis-geo_location_manager.md#static-func-islocationenabled) | 判断位置服务是否已经开启。 |
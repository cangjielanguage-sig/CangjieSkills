## 场景概述

开发者可以调用位置相关接口，获取设备实时位置或最近的历史位置，以及监听设备的位置变化。

对于位置敏感的应用业务，建议获取设备实时位置信息。如果不需要设备实时位置信息，并且希望尽可能地节省耗电，开发者可以考虑获取最近的历史位置。

## 接口说明

获取设备的位置信息所使用的接口如下，详细说明参见：[Location Kit](../../cj-apis-geo_location_manager/.overview.md)。

本模块能力仅支持WGS-84坐标系。

| 接口名 | 功能描述 |
| -------- | -------- |
| [on(CallbackType, LocationRequest, Callback1Argument\<Location>)](../../cj-apis-geo_location_manager/.overview.md) | 开启位置变化订阅，并发起定位请求。 |
| [off(CallbackType, Callback1Argument\<Location>)](../../cj-apis-geo_location_manager/.overview.md) | 关闭位置变化订阅，并删除对应的定位请求。 |
| [getCurrentLocation()](../../cj-apis-geo_location_manager/.overview.md) | 获取当前位置。|
| [getCurrentLocation(CurrentLocationRequest)](../../cj-apis-geo_location_manager/.overview.md) | 获取当前位置。|
| [getCurrentLocation(SingleLocationRequest)](../../cj-apis-geo_location_manager/.overview.md) | 获取当前位置。|
| [getLastLocation()](../../cj-apis-geo_location_manager/.overview.md) | 获取最近一次定位结果。 |
| [isLocationEnabled()](../../cj-apis-geo_location_manager/.overview.md) | 判断位置服务是否已经开启。 |
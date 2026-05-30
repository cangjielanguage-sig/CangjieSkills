## 场景概述

使用坐标描述一个位置，虽十分准确，但不够直观，面向用户表达时不够友好。系统向开发者提供了以下两种转化能力。

- 地理编码转化：将地理描述转化为具体坐标。

- 逆地理编码转化能力：将坐标转化为地理描述。

其中地理编码包含多个属性来描述位置，包括国家、行政区划、街道、门牌号、地址描述等，这些信息更便于用户理解。

## 接口说明

进行坐标和地理编码信息的相互转化，所使用的接口说明如下，详细信息参见：[Location Kit](../../API_Reference/source_zh_cn/apis/LocationKit/cj-apis-geo_location_manager.md)。

| 接口名 | 功能描述 |
| -------- | -------- |
| [isGeocoderAvailable()](../../API_Reference/source_zh_cn/apis/LocationKit/cj-apis-geo_location_manager.md#static-func-isgeocoderavailable) | 判断地理编码与逆地理编码服务是否可用。 |
| [getAddressesFromLocation(ReverseGeoCodeRequest)](../../API_Reference/source_zh_cn/apis/LocationKit/cj-apis-geo_location_manager.md#static-func-getaddressesfromlocationreversegeocoderequest) | 调用逆地理编码服务，将坐标转换为地理描述。 |
| [getAddressesFromLocationName(GeoCodeRequest)](../../API_Reference/source_zh_cn/apis/LocationKit/cj-apis-geo_location_manager.md#static-func-getaddressesfromlocationnamegeocoderequest) | 调用地理编码服务，将地理描述转换为具体坐标。 |
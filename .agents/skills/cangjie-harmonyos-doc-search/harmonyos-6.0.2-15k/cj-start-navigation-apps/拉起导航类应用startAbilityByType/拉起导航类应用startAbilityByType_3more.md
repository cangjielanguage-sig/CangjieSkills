# 拉起导航类应用（startAbilityByType）

本章节介绍如何拉起导航类应用扩展面板。

## 导航类应用扩展面板参数说明

startAbilityByType接口中type字段为navigation，支持路线规划、导航、位置搜索三种意图场景，对应的wantParam参数如下：

> **说明：**
>
> 本文中的经纬度均采用GCJ-02坐标系统。

- 路线规划场景

  | 参数名               | 类型                   | 必填 | 说明                                                 |
  | -------------------- | ---------------------- | ---- | ---------------------------------------------------- |
  | sceneType            | Int64                 | 否   | 意图场景，表明本次请求对应的操作意图。默认为1，路线规划场景填1或不填                   |
  | originName           | String                 | 否   | 起点名称                                             |
  | originLatitude       | Float64                 | 否   | 起点纬度                                             |
  | originLongitude      | Float64                 | 否   | 起点经度                                             |
  | originPoiIds         | HashMap\<String, String> | 否   | 起点POI ID列表，当前仅支持传入花瓣地图和高德地图的POI ID|
  | destinationName      | String                 | 否   | 终点名称                                             |
  | destinationLatitude  | Float64                 | 是   | 终点纬度                                             |
  | destinationLongitude | Float64                 | 是   | 终点经度                                             |
  | destinationPoiIds    | HashMap\<String, String> | 否   | 终点POI ID列表，当前仅支持传入花瓣地图和高德地图的POI ID|
  | vehicleType          | Int64                 | 否   | 交通出行工具，取值：0-驾车，1-步行，2-骑行，3-公交 |

- 导航场景

  | 参数名               | 类型                   | 必填 | 说明              |
  | -------------------- | ---------------------- | ---- | ----------------- |
  | sceneType            | Int64                 | 是   | 意图场景，表明本次请求对应的操作意图。导航场景填2 |
  | destinationName      | String                 | 否   | 终点名称          |
  | destinationLatitude  | Float64                 | 是   | 终点纬度          |
  | destinationLongitude | Float64                 | 是   | 终点经度          |
  | destinationPoiIds    | HashMap\<String, String> | 否   | 终点POI ID列表，当前仅支持传入花瓣地图和高德地图的POI ID|

- 位置搜索场景

  | 参数名          | 类型   | 必填 | 说明                  |
  | --------------- | ------ | ---- | --------------------- |
  | sceneType       | Int64 | 是   | 意图场景，表明本次请求对应的操作意图。位置搜索场景填3 |
  | destinationName | String | 是   | 地点名称              |

## 拉起方开发步骤

1. 导入相关模块。

    ```cangjie
    import kit.AbilityKit.*
    ```

2. 构造接口参数并调用startAbilityByType接口。示例中的context的获取方式请参见[获取UIAbility的上下文信息](cj-uiability-usage.md#获取uiability的上下文信息)。

   终点POI ID列表（destinationPoiIds）和起点POI ID列表（originPoiIds）需开发者自行从各地图系统中获取，并按照对应关系传参。

    ```cangjie
    import std.collection.HashMap
    import kit.AbilityKit.{UIAbilityContext, Want, AbilityStartCallback}
    import kit.UIKit.{AsyncError, AppLog, Button, BusinessException}

    // 见获取UIAbility的上下文信息章节
    func getContext(): UIAbilityContext {
        return globalContext.getOrThrow()
    }

    let callBack = AbilityStartCallback(
        {
            code, name, message => AppLog.info("onError code ${code} name: ${name} message: ${message}")
        },
        onResult: {
            result => AppLog.info("onResult resultCode: ${result.resultCode}")
        }
    )

    @Entry
    @Component
    class EntryView {
        func build() {
            Row {
                Column {
                    Button("start type").onClick(
                        {
                            evt =>
                            let context = getContext()
                            let jsonString = ##"{"sceneType":1,"destinationLatitude":32.060844,"destinationLongitude":118.78315,"destinationName":"xx市xx路xx号","destinationPoiIds":{"1":"111","2":"222"},"originName":"xx市xx公园","originLatitude":31.060844,"originLongitude":120.78315,"originPoiIds":{"1":"333","2":"444"},"vehicleType":0}"##
                            try {
                                context.startAbilityByType("navigation", jsonString, callBack)
                            } catch (e: BusinessException) {
                                AppLog.error("startAbilityByType fail, err: ${e.message}")
                            }
                        }
                    )
                }.width(100.percent)
            }.height(100.percent)
        }
    }
    ```

    效果示例图：

    ![效果示例图](./figures/start-navigation-panel.png)
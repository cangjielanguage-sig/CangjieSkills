## SysCap开发指导

<!--RP1-->

### PCID获取

PCID，全称Product Compatibility ID，包含当前设备支持的SysCap信息。获取所有设备PCID的认证中心正在建设中，目前需要找对应设备的厂商获取该设备的PCID。

### 配置联想能力集和要求能力集

DevEco Studio会根据创建的工程所支持的设置自动配置联想能力集和要求能力集，开发者也可以自行修改。
对于联想能力集，开发者通过添加更多的系统能力，在DevEco Studio中可以使用更多的API，但要注意这些API可能在设备上不支持，使用前需要判断。
对于要求能力集，开发者修改时要十分慎重，修改不当会导致应用无法分发到目标设备上。

```json
// syscap.json
{
 "devices": {
  "general": [            // 每一个典型设备对应一个syscap支持能力集，可配置多个典型设备
   "default",
   "car"
  ],
  "custom": [             // 厂家自定义设备
   {
    "某自定义设备": [
     "SystemCapability.Communication.SoftBus.Core"
    ]
   }
  ]
 },
 "development": {             // addedSysCaps内的sycap集合与devices中配置的各设备支持的syscap集合的并集共同构成联想能力集
  "addedSysCaps": [
   "SystemCapability.Location.Location.Lite"
  ]
 },
 "production": {              // 用于生成rpcid，慎重添加，可能导致应用无法分发到目标设备上
  "addedSysCaps": [],      // devices中配置的各设备支持的syscap集合的交集，添加addedSysCaps集合再除去removedSysCaps集合，共同构成要求能力集
  "removedSysCaps": []     // 当该要求能力集为某设备的子集时，应用才可被分发到该设备上
 }
}
```
<!--RP1End-->

### 单设备应用开发

默认应用的联想能力集，要求系统能力集和设备的支持系统能力集相等，开发者修改要求能力集需要慎重。

![image-Single-device-app-dev-view](figures/image-Single-device-app-dev-view.png)

### 跨设备应用开发

默认应用的联想能力集是多个设备支持能力集的并集，要求能力集则是交集。

![image-Cross-device-app-dev-view](figures/image-Cross-device-app-dev-view.png)

### 判断API是否可以使用

当前提供了仓颉 API用于帮助判断某个API是否可以使用。

<!-- compile -->

```cangjie
import ohos.base.canIUse

if(canIUse("SystemCapability.ArkUI.ArkUI.Full")){
    Hilog.info(0, "SysCap", "支持系统能力SystemCapability.ArkUI.ArkUI.Full")
}else{
    Hilog.info(0, "SysCap", "不支持系统能力SystemCapability.ArkUI.ArkUI.Full")
}
```

### 不同设备相同能力的差异检查

即使是相同的系统能力，在不同的设备下，也会有能力的差异。

以下示例通过获取蓝牙已连接设备进行举例：

<!-- compile -->

```cangjie
import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

// 在使用接口时可通过try..catch捕获异常。如果接口的SysCap不支持当前设备，将返回801错误码。
try {
    let hdfProfile = createHfpAgProfile()
    let retArray = hdfProfile.getConnectedDevices()
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```
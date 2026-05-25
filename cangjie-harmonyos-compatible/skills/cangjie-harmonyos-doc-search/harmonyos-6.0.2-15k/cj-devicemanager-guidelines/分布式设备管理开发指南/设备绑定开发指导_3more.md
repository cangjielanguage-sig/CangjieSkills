## 设备绑定开发指导

### 场景概述

开发者发现周边不可信设备后，通过绑定API建立可信关系。

### 接口说明

bindTarget(deviceId: String, bindParam: HashMap\<String, ValueType>): String

设备绑定。详细信息请参见：[bindTarget](../../API_Reference/source_zh_cn/apis/DistributedServiceKit/cj-apis-distributed_device_manager.md#func-bindtargetstring-hashmapstring-valuetype)。

### 开发步骤

1. 申请分布式数据同步权限。

2. 发现周边不可信设备。

3. 选择不可信设备id，发起设备绑定。

    ```cangjie
    let dmInstance = createDeviceManager('ohos.samples.cjHelloWorld')
    let deviceId = 'XXXXXXXX'
    let bindParam: HashMap<String, ValueType> = HashMap<String, ValueType>(
        [
            ("bindType", Integer(1)),
            ("targetPkgName", Str("xxxx")),
            ("appName", Str("xxxx")),
            ("appOperation", Str("xxxx")),
            ("customDescription", Str("xxxx"))
        ]
    )
    try {
        let dm = dmInstance.bindTarget(deviceId, bindParam)
        AppLog.info("bindTarget result: ${dm}")
    } catch (e: BusinessException) {
        AppLog.error("bindTarget errCode: ${e.code},errMessage: ${e.message}")
    }
    ```

## 设备信息查询开发指导

### 场景概述

设备与周边设备建立可信关系后，通过设备信息查询API可以获取所有上线并且可信的设备。

### 接口说明

getAvailableDeviceList(): Array\<DeviceBasicInfo>

设备信息查询。详细信息请参见：[getAvailableDeviceList](../../API_Reference/source_zh_cn/apis/DistributedServiceKit/cj-apis-distributed_device_manager.md#func-getavailabledevicelist)。

### 开发步骤

1. 申请分布式数据同步权限。

2. 发现周边不可信设备。

3. 建立设备间的可信关系。

4. 查询周围上线并且可信的设备。

    ```cangjie
    let dmInstance = createDeviceManager('ohos.samples.cjHelloWorld')

    try {
        let deviceInfoList: Array<DeviceBasicInfo> = dmInstance.getAvailableDeviceList()
    } catch (e: BusinessException) {
        AppLog.error("getAvailableDeviceListSync errCode: ${e.code},errMessage: ${e.message}")
    }
    ```

## 设备上下线监听开发指导

### 场景概述

周边可信设备可用后会给业务报上线通知，当设备不可用时会给业务报下线通知。

### 接口说明

on(\`type\`: DeviceStatusType, callback: CallbackObject): Unit

设备上下线监听。详细信息请参见：[on(DeviceStatusType.DEVICE_STATE_CHANGE)](../../API_Reference/source_zh_cn/apis/DistributedServiceKit/cj-apis-distributed_device_manager.md#func-ondevicestatustype-callbackobject)。

### 开发步骤

1. 申请分布式数据同步权限。

2. 导入DistributedServiceKit模块，所有与设备管理相关的功能API，都是通过该模块提供的。

    ```cangjie
    import kit.DistributedServiceKit.*
    ```

3. 导入BusinessException模块，用于获取DistributedServiceKit模块相关API抛出的错误码。

    ```cangjie
    import ohos.base.*
    ```

4. 创建设备管理实例，设备管理实例是分布式设备管理方法的调用入口，并注册设备上下线回调。

    ```cangjie
    class Callback2ArgumentImpl<A, B> <: Callback2Argument<A, B> {
        Callback2ArgumentImpl(let callback: (A, B) -> Unit) {}

        public func invoke(arg1: A, arg2: B): Unit {
            callback(arg1, arg2)
        }
    }

    let deviceStateChange = Callback2ArgumentImpl<DeviceStateChange, DeviceBasicInfo> {
        deviceName: DeviceStateChange, info: DeviceBasicInfo => AppLog.info(
            "deviceStateChange on: ${deviceName}")
    }
    try {
        let dmInstance = createDeviceManager('ohos.samples.cjHelloWorld')
        dmInstance.on(DEVICE_STATE_CHANGE, deviceStateChange)
    } catch (e: BusinessException) {
        AppLog.error("createDeviceManager errCode: ${e.code},errMessage: ${e.message}")
    }
    ```
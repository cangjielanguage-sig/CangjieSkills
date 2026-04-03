### server端操作services和通知客户端信息

1. import需要的ble模块。
2. 创建gattServer实例对象。
3. 添加services信息。
4. 当向gattServer写入特征值通知gattClient。
5. 移除services信息。
6. 注销gattServer实例。
7. 示例代码:

    ```cangjie
    import kit.ConnectivityKit.*
    import ohos.base.{BusinessException, Callback1Argument}
    import std.collection.ArrayList

    const TAG: String = 'GattServerManager'

    class GattServerManager {
        public var gattServer: ?GattServer = None
        let connectState: ProfileConnectionState = ProfileConnectionState.STATE_DISCONNECTED
        let myServiceUuid: String = '00001810-0000-1000-8000-00805F9B34FB'
        let myCharacteristicUuid: String = '00001820-0000-1000-8000-00805F9B34FB'
        let myFirstDescriptorUuid: String = '00002902-0000-1000-8000-00805F9B34FB' // 2902一般用于notification或者indication
        let mySecondDescriptorUuid: String = '00002903-0000-1000-8000-00805F9B34FB'

        // 构造BLEDescriptor
        private func initDescriptor(des: String, value: Array<Byte>): BLEDescriptor {
            let descriptor: BLEDescriptor = BLEDescriptor(
                this.myServiceUuid,
                this.myCharacteristicUuid,
                des,
                value
            )
            return descriptor
        }

        // 构造BLECharacteristic
        private func initCharacteristic(): BLECharacteristic {
            let descValue: Array<UInt8> = [31, 32]
            let descriptors: Array<BLEDescriptor> = [initDescriptor(this.myFirstDescriptorUuid, [0, 0]),
                initDescriptor(this.mySecondDescriptorUuid, descValue)]
            let charValue: Array<UInt8> = [21, 22]
            let characteristic: BLECharacteristic = BLECharacteristic(
                this.myServiceUuid,
                this.myCharacteristicUuid,
                charValue,
                descriptors,
                GattProperties()
            )
            return characteristic
        }

        // 1. 订阅连接状态变化事件
        public func onGattServerStateChange() {
            if (this.gattServer.isNone()) {
                AppLog.error('no gattServer')
                return
            }
            try {
                this.gattServer?.on(BluetoothBleGattServerCallbackType.CONNECTION_STATE_CHANGE, ChangeStateCb())
            } catch (e: BusinessException) {
                AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
            }
        }

        // 2. server端注册服务时调用
        public func registerServer(peerDevice: String) { // 对端设备一般通过ble scan获取到
            let characteristics: ArrayList<BLECharacteristic> = ArrayList<BLECharacteristic>()
            let characteristic = this.initCharacteristic()
            characteristics.add(characteristic)
            let gattService: GattService = GattService(
                this.myServiceUuid,
                true,
                characteristics.toArray(),
                Array<GattService>()
            )
            AppLog.info('registerServer ' + this.myServiceUuid)
            try {
                this.gattServer = createGattServer() // 2.1 构造gattServer，后续的交互都需要使用该实例
                this.onGattServerStateChange() // 2.2 订阅连接状态
                this.gattServer?.addService(gattService)
            } catch (e: BusinessException) {
                AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
            }
        }

        // 3. 订阅来自gattClient的读取特征值请求时调用
        public func onCharacteristicRead() {
            if (this.gattServer.isNone()) {
                AppLog.info('no gattServer')
                return
            }
            AppLog.info('onCharacteristicRead')
            try {
                this.gattServer?.on(BluetoothBleGattServerCallbackType.CHARACTERISTIC_READ, ReadRequestCb())
            } catch (e: BusinessException) {
                AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
            }
        }

        // 4. 订阅来自gattClient的写入特征值请求时调用
        public func onCharacteristicWrite() {
            if (this.gattServer.isNone()) {
                AppLog.error('no gattServer')
                return
            }

            AppLog.info('onCharacteristicWrite')
            try {
                this.gattServer?.on(BluetoothBleGattServerCallbackType.CHARACTERISTIC_WRITE, WriteRequestCb())
            } catch (e: BusinessException) {
                AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
            }
        }

        // 5. 订阅来自gattClient的读取描述符请求时调用
        public func onDescriptorRead() {
            if (this.gattServer.isNone()) {
                AppLog.error('no gattServer')
                return
            }
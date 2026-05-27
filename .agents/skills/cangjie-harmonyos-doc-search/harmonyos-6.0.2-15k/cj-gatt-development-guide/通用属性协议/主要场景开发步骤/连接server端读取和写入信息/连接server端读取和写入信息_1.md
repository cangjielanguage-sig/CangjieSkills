### 连接server端读取和写入信息

1. import需要的ble模块。
2. 创建gattClient实例对象。
3. 连接gattServer。
4. 读取gattServer的特征值和描述符。
5. 向gattServer写入特征值和描述符。
6. 断开连接，销毁gattClient实例。
7. 示例代码:

    ```cangjie
    import kit.ConnectivityKit.*
    import ohos.base.{BusinessException, Callback1Argument}

    const TAG: String = 'GattClientManager'

    class GattClientManager {
        var device: ?String = None
        var gattClient: ?GattClientDevice = None
        let connectState: ProfileConnectionState = ProfileConnectionState.STATE_DISCONNECTED
        let myServiceUuid: String = '00001810-0000-1000-8000-00805F9B34FB'
        let myCharacteristicUuid: String = '00001820-0000-1000-8000-00805F9B34FB'
        let myFirstDescriptorUuid: String = '00002902-0000-1000-8000-00805F9B34FB' // 2902一般用于notification或者indication
        let mySecondDescriptorUuid: String = '00002903-0000-1000-8000-00805F9B34FB'
        var found: Bool = false

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
            let descValue: Array<UInt8> = [11, 12]
            let descriptors: Array<BLEDescriptor> = [initDescriptor(this.myFirstDescriptorUuid, [0, 0]),
                initDescriptor(this.mySecondDescriptorUuid, descValue)]
            let charValue: Array<UInt8> = [1, 2]
            let characteristic: BLECharacteristic = BLECharacteristic(
                this.myServiceUuid,
                this.myCharacteristicUuid,
                charValue,
                descriptors,
                GattProperties()
            )
            return characteristic
        }

        private func logCharacteristic(char: BLECharacteristic) {
            var message = 'logCharacteristic uuid:' + char.characteristicUuid + '\n'
            let value = char.characteristicValue
            message += 'logCharacteristic value: '
            for (i in 0..value.size) {
                message += value[i].toString() + ' '
            }
            AppLog.info(message)
        }

        private func logDescriptor(des: BLEDescriptor) {
            var message = 'logDescriptor uuid:' + des.descriptorUuid + '\n'
            let value = des.descriptorValue
            message += 'logDescriptor value: '
            for (i in 0..value.size) {
                message += value[i].toString() + ' '
            }
            AppLog.info(message)
        }

        private func checkService(services: Array<GattService>): Bool {
            for (i in 0..services.size) {
                if (services[i].serviceUuid != this.myServiceUuid) {
                    continue
                }
                for (j in 0..services[i].characteristics.size) {
                    if (services[i].characteristics[j].characteristicUuid != this.myCharacteristicUuid) {
                        continue
                    }
                    for (k in 0..services[i].characteristics[j].descriptors.size) {
                        if (services[i].characteristics[j].descriptors[k].descriptorUuid == this.myFirstDescriptorUuid) {
                            AppLog.info('find expected service from server')
                            return true
                        }
                    }
                }
            }
            AppLog.error('no expected service from server')
            return false
        }

        // 1. 订阅连接状态变化事件
        public func onGattClientStateChange() {
            if (this.gattClient.isNone()) {
                AppLog.error('no gattClient')
                return
            }
            try {
                this.gattClient?.on(BluetoothBleGattClientDeviceCallbackType.BLE_CONNECTION_STATE_CHANGE, ChangeStateCb())
            } catch (e: BusinessException) {
                AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
            }
        }
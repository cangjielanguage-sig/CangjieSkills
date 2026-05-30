// 2. client端主动连接时调用
        public func startConnect(peerDevice: String) { // 对端设备一般通过ble scan获取到
            if (this.connectState != ProfileConnectionState.STATE_DISCONNECTED) {
                AppLog.error('startConnect failed')
                return
            }
            AppLog.info('startConnect ' + peerDevice)
            this.device = peerDevice
            // 2.1 使用device构造gattClient，后续的交互都需要使用该实例
            this.gattClient = createGattClientDevice(peerDevice)
            try {
                this.onGattClientStateChange() // 2.2 订阅连接状态
                this.gattClient?.connect() // 2.3 发起连接
            } catch (e: BusinessException) {
                AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
            }
        }

        // 3. client端连接成功后，需要进行服务发现
        public func discoverServices() {
            if (this.gattClient.isNone()) {
                AppLog.info('no gattClient')
                return
            }
            AppLog.info('discoverServices')
            try {
                let result = this.gattClient?.getServices()
                this.found = this.checkService(result.getOrThrow()) // 要确保server端的服务内容有业务所需要的服务
            } catch (e: BusinessException) {
                AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
            }
        }

        // 4. 在确保拿到了server端的服务结果后，读取server端特定服务的特征值时调用
        public func readCharacteristicValue() {
            if (this.gattClient.isNone() || this.connectState != ProfileConnectionState.STATE_CONNECTED) {
                AppLog.error('no gattClient or not connected')
                return
            }
            if (!this.found) { // 要确保server端有对应的characteristic
                AppLog.error('no characteristic from server')
                return
            }

            let characteristic = this.initCharacteristic()
            AppLog.info('readCharacteristicValue')
            try {
                this.gattClient?.readCharacteristicValue(characteristic) {
                    e, outData => this.logCharacteristic(outData.getOrThrow())
                }
            } catch (e: BusinessException) {
                AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
            }
        }

        // 5. 在确保拿到了server端的服务结果后，写入server端特定服务的特征值时调用
        public func writeCharacteristicValue() {
            if (this.gattClient.isNone() || this.connectState != ProfileConnectionState.STATE_CONNECTED) {
                AppLog.error('no gattClient or not connected')
                return
            }
            if (!this.found) { // 要确保server端有对应的characteristic
                AppLog.error('no characteristic from server')
                return
            }

            let characteristic = this.initCharacteristic()
            AppLog.info('writeCharacteristicValue')
            try {
                this.gattClient?.writeCharacteristicValue(characteristic, GattWriteType.WRITE) {
                    err =>
                    if (let Some(e) <- err) {
                        AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
                        return
                    }
                    AppLog.info('writeCharacteristicValue success')
                }
            } catch (e: BusinessException) {
                AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
            }
        }

        // 6. 在确保拿到了server端的服务结果后，读取server端特定服务的描述符时调用
        public func readDescriptorValue() {
            if (this.gattClient.isNone() || this.connectState != ProfileConnectionState.STATE_CONNECTED) {
                AppLog.error('no gattClient or not connected')
                return
            }
            if (!this.found) { // 要确保server端有对应的descriptor
                AppLog.error('no descriptor from server')
                return
            }

            let descBuffer = Array<Byte>()
            let descriptor = this.initDescriptor(this.mySecondDescriptorUuid, descBuffer)
            AppLog.info('readDescriptorValue')
            try {
                this.gattClient?.readDescriptorValue(descriptor) {
                    e, outData => this.logDescriptor(outData.getOrThrow())
                }
            } catch (e: BusinessException) {
                AppLog.error('errCode: ${e.code}, errMessage: ' + e.message)
            }
        }
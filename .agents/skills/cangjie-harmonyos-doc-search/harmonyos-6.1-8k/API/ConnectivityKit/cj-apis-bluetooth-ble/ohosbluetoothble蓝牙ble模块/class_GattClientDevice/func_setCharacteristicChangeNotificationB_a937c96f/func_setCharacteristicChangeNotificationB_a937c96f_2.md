try {
    let gattClient = createGattClientDevice("XX:XX:XX:XX:XX:XX")  // 请替换为您的设备地址
    gattClient.setCharacteristicChangeNotification(characteristic, false) {
        error: ?BusinessException, c: ?Unit => if (let Some(e) <- error) {
            throw e
        }
    }
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}", "")
}
```
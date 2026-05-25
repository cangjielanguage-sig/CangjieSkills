// 设置特征值变化指示能力
try {
  // enable入参: true表示启用，false表示禁用
    gattClient?.setCharacteristicChangeIndication(characteristic, true)  {
        error: ?BusinessException, c: ?Unit => if (let Some(e) <- error) {
            Hilog.info(0, "Bluetooth", "setCharacteristicChangeIndication callback failed")
        } else {
            Hilog.info(0, "Bluetooth", "setCharacteristicChangeIndication callback successful")
        }
    }
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}", "")
}
```
/*
 * 模拟解密场景
 */
func DecryptData() {
    // 获取解密算法参数配置
    let decryptOptions = GetRsaDecryptProperties()
    let options: HuksOptions = HuksOptions(
        properties: decryptOptions,
        inData: cipherData.getOrThrow() // 加密后的密文数据
    )
    // 调用initSession获取handle，rsaKeyAlias是密钥别名，在生成密钥时进行指定的
    handle = initSession(rsaKeyAlias, options).handle
    // 调用finishSession获取解密后的数据
    finishSession(handle.getOrThrow(), options)
}

/*
 * 模拟删除密钥场景
 */
func DeleteKey() {
    let emptyOptions: HuksOptions = HuksOptions()
    // 调用deleteKeyItem删除密钥，rsaKeyAlias是密钥别名，在生成密钥时进行指定的
    deleteKeyItem(rsaKeyAlias, emptyOptions)
}
```
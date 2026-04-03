/*
 * 模拟解密场景
 */
func DecryptData() {
    // 获取解密算法参数配置
    let decryptOptions = GetAesDecryptProperties()
    let options: HuksOptions = HuksOptions(
        properties: decryptOptions,
        inData: cipherData.getOrThrow()
    )
    // 调用initSession获取handle，aesKeyAlias是密钥别名，在生成密钥时进行指定的
    handle = initSession(aesKeyAlias, options).handle
    // 调用finishSession获取解密后的数据
    let result = finishSession(handle.getOrThrow(), options)
}

/*
 * 模拟删除密钥场景
 */
func DeleteKey() {
    let emptyOptions: HuksOptions = HuksOptions()
    // 调用deleteKeyItem删除密钥，aesKeyAlias是密钥别名，在生成密钥时进行指定的
    deleteKeyItem(aesKeyAlias, emptyOptions)
}
```
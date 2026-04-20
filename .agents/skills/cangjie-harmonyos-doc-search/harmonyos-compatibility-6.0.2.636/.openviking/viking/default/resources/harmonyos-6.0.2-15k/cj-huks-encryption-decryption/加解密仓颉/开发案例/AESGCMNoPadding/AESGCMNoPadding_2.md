/*
 * 模拟删除密钥场景
 */
func DeleteKey() {
    let emptyOptions: HuksOptions = HuksOptions.NONE
    // 调用deleteKeyItem删除密钥，aesKeyAlias是密钥别名，在生成密钥时进行指定的
    deleteKeyItem(aesKeyAlias, emptyOptions)
}
```
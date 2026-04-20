// ...
    public override func onDestroy(): Unit {
        // 获取应用上下文
        let applicationContext = this.context.getApplicationContext()
        try {
            // 取消应用内生命周期回调
            applicationContext.off(ApplicationContextType.ABILITY_LIFE_CYCLE, lifecycleId)
        } catch (e: BusinessException) {
            AppLog.error("Failed to unregister applicationContext. Code is ${e.code}, message is ${e.message}")
        }
    }
}
```
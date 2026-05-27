/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// The Cangjie API is in Beta. For details on its capabilities and limitations, please refer to the README file.

package ohos.app.ability.app_recovery

import ohos.app.ability.want.WantHandle
import ohos.labels.APILevel

foreign {
    func FFIAppRecoveryEnable(restartFlag: Int32, saveOccasionFlag: Int32, saveModeFlag: Int32): Unit

    func FFIAppRecoveryRestartApp(): Unit

    func FFIAppRecoverySaveAppState(ctxId: Int64): Bool
}

/**
 * Restart current process and launch the first ability(the entry ability in most cases) of current process.
 * The previous saved state will be filled in the want.wantParams of UIAbility.onCreate interface.
 * and the param of UIAbility.onCreate will be set to AppRecovery.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public func restartApp(): Unit {
    unsafe {
        FFIAppRecoveryRestartApp()
    }
}

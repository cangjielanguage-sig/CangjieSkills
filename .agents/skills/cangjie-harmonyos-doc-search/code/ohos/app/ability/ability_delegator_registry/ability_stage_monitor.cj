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

package ohos.app.ability.ability_delegator_registry

import ohos.ffi.{FFIData, FFIDataManager}
import ohos.labels.APILevel

/**
 * Provide methods for matching monitored AbilityStage objects that meet specified conditions.
 * The most recently matched AbilityStage objects will be saved in the AbilityStageMonitor object.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.Core"
]
public class AbilityStageMonitor <: FFIData {
    /**
     * The module name of the abilityStage to monitor.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var moduleName: String
    /**
     * The source path of the abilityStage to monitor.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public var srcEntrance: String
    /**
     * AbilityStageMonitor constructor.
     *
     * @param { String } moduleName - The module name of the abilityStage to monitor.
     * @param { String } srcEntrance - The source path of the abilityStage to monitor.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.Core"
    ]
    public init(
        moduleName: String,
        srcEntrance: String
    ) {
        registerSelf()
        this.moduleName = moduleName
        this.srcEntrance = srcEntrance
    }

    ~init() {
        FFIDataManager.getInstance().releaseData(id_)
    }
}

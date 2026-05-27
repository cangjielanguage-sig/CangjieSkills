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

package ohos.ability.ability_result

import ohos.labels.APILevel
import ohos.app.ability.want.{Want, WantHandle}

/**
 * AbilityResult
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityBase"
]
public class AbilityResult {
    /**
     * Indicates the result code returned after the ability is destroyed. You can define the result
     * code to identify an error.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    public var resultCode: Int32

    /**
     * Indicates the data returned after the ability is destroyed. You can define the data returned.
     * This parameter can be null.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    public var want: Want

    /**
     * AbilityResult constructor.
     *
     * @param { Int32 } resultCode - Indicates the result code returned after the ability is destroyed.
     * @param { Want } [want] - Indicates the data returned after the ability is destroyed. The default value is Want().
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityBase"
    ]
    public init(resultCode: Int32, want!: Want = Want()) {
        this.resultCode = resultCode
        this.want = want
    }
}

@C
protected struct CJAbilityResult {
    protected CJAbilityResult(
        protected let resultCode: Int32,
        protected let wantHandle: WantHandle
    ) {}
}

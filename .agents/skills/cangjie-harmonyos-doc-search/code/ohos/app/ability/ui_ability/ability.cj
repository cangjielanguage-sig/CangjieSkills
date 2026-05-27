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

package ohos.app.ability.ui_ability

import ohos.ffi.FFIData
import std.collection.HashMap
import ohos.labels.{APILevel, Hide}

class AbilityImpl {}

/**
 * The class of an ability.
 */
@!APILevel[
    since: "22",
    syscap: "SystemCapability.Ability.AbilityRuntime.AbilityCore"
]
abstract sealed class Ability <: FFIData {
    private static let CREATORS = HashMap<String, () -> Ability>()
    private let impl_ = AbilityImpl()

    /**
     * register Ability
     *
     * @param { String } name - The module name of the Ability.
     * @param { () -> Ability } creator - The creator of the Ability.
     */
    @!APILevel[
        since: "22",
        syscap: "SystemCapability.Ability.AbilityRuntime.AbilityCore"
    ]
    @!Hide
    public static func registerCreator(name: String, creator: () -> Ability): Unit {
        let optCreator = CREATORS.get(name)
        match (optCreator) {
            case None =>
                CREATORS.add(name, creator)
                ABILITY_LOG.info("Register creator of " + name + " successfully.")
            case Some(creatorFunc) => ABILITY_LOG.error(
                "Repeated registration for Ability in " + name + ", please check.")
        }
    }

    protected static func create(name: String): Option<Ability> {
        let optCreator = CREATORS.get(name)
        match (optCreator) {
            case None =>
                ABILITY_LOG.error("No such create functions for Ability: " + name)
                Option<Ability>.None
            case Some(creator) => creator()
        }
    }
}

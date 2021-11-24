module.exports = {
    "env": {
        "browser": true,
        "es2021": true
    },
    "parserOptions": {
        "ecmaVersion": 13,
        "sourceType": "module"
    },
    "plugins": [
        "vue"
    ],
    "rules": {
    },
    "extends": [
		"wikimedia/client",
		"wikimedia/jquery",
		"wikimedia/mediawiki",
        "eslint:recommended",
        "plugin:vue/essential"
	],
	"globals": {
		"require": "readonly",
		"module": "readonly",
		"OO": "readonly"
	},
	"rules": {
		"quote-props": [ "error", "as-needed" ],
		"max-len": "off",
		"no-jquery/no-global-selector": "off"
	},
	"overrides": [
            {
                "files": [ "**/*.vue" ],
                "extends": [
                    "plugin:vue/recommended",
                    "plugin:es/no-2015"
                ],
                "plugins": [ "es" ],
                "parserOptions": {
                    "sourceType": "script",
                    "ecmaFeatures": {
                        "jsx": false
                    }
                },
                "rules": {
                    "no-implicit-globals": 0,
                    "vue/html-indent": [ "warn", "tab" ],
                    "vue/html-closing-bracket-newline": "off",
                    "vue/max-attributes-per-line": [ "warn", {
                        "singleline": 2,
                        "multiline": {
                            "max": 1,
                            "allowFirstLine": true
                        }
                    } ],
                    "vue/v-on-style": [ "error", "longform" ],
                    "vue/v-bind-style": [ "error", "longform" ],
                    "vue/v-slot-style": [ "error", "longform" ]
                }
            }
        ]
    }
    
};

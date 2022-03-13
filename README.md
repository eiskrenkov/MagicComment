# MagicComment ✨ for Sublime Text
MagicComment is a fully customizable Sublime Text plugin that automatically inserts required magic comments for you

Development is motivated by `frozen_string_literal` comment for Ruby files, but plugin can be used for literally any kind of files and any strings that you want to automatically insert

## Manual usage Demo
![Screen Recording 2022-03-14 at 01 17 57](https://user-images.githubusercontent.com/39211838/158079694-79eb9a74-91fb-4eb9-9b4f-0ae2b3a83359.gif)

## Installation

### Manual Installation
- `cd <Packages directory>` (macOS: `~/Library/Application\ Support/Sublime\ Text/Packages`)
- `git clone https://github.com/eiskrenkov/MagicComment.git`

## Usage
- **On file save** (enabled by default, can be disabled in settings)
- **Key Bindings** - Default binging is `CMD+CTRL+C` (can be reconfigured)
- **Command Palette** - `CMD+P` and type `MagicComment` (or just `comment`) and select `MagicComment: Insert Comments`

## Default Configuration
Remember, that you can always reconfigure it, just open _Sublime Text menu_ -> _Preferences_ -> _Package Settings_ -> _MagicComment_ -> _Settings_

### General
- `run_on_save`
    - Type: `Boolean`
    - Default: `true`

### Comments
- `text` - Text of the comment to insert
    - Type: `String`
    - Default: `true`

- `line` - Number of the line you wish to insert the comment
    - Type: `Integer`
    - Default: `1`

- `blank_lines` - Amount of blank lines to insert after the comment
    - Type: `Integer`
    - Default: `0`

- `files` - Object, containing files specific settings
    - Type: `Object`

- `files` -> `include` - List of file names and extensions to insert comment for
    - Type: `Array` of `String`
    - Default: `[]`

- `files` -> `exclude` - List of file names and extensions that you want to ignore
    - Type: `Array` of `String`
    - Default: `[]`

> Note, that **Include** and **Exclude** arrays support wildcards for file extensions via '*'. E.g *.rb mathes all Ruby files, *.py - all Python files and so on

### Example configuration for `#frozen_string_literal: true` for `.rb` files
```json
{
    "text": "# frozen_string_literal: true",
    "line": 1,
    "blank_lines": 1,
    "files": {
        "include": ["*.rb", "Gemfile", "Rakefile", "config.ru"],
        "exclude": ["schema.rb"]
    }
}
```

## Contribution
Issues and pull requests are highly welcome!

[Package Control]: https://packagecontrol.io

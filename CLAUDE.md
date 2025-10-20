# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an Alacritty terminal emulator configuration repository located at `/Users/tony/.config/alacritty` on macOS. It contains the main configuration file, theme collections, and testing utilities for the Alacritty terminal.

## Configuration Structure

### Main Configuration File

**File:** `alacritty.toml`

**Current settings:**
- Font: JetBrainsMono Nerd Font (size 16)
- Theme: Imported from `themes/themes/coolnight.toml`
- Cursor: Always blinking, unfocused hollow
- Terminal: xterm-256color
- Window: Maximized startup, 10px horizontal padding
- Option key: Configured as Alt for both keys (macOS)
- Scrollback: 2000 lines

**Legacy reference:** `alacritty.org` contains the comprehensive default configuration with all available options and documentation (read-only reference).

### Theme System

**Location:** `themes/` directory

**Structure:**
- `themes/themes/` - 100+ individual theme files (.yaml/.toml)
- `themes/schemes.yaml` - Color scheme definitions
- `themes/README.md` - Theme documentation and catalog

**Current theme:** coolnight.toml

**Switching themes:** Edit the `import` line in `alacritty.toml`:
```toml
import = ["~/.config/alacritty/themes/themes/{theme-name}.toml"]
```

## Testing Utilities

### smoke-test.sh
Quick visual test for font rendering (normal, bold, italic, underline) and special characters.

**Usage:**
```bash
./smoke-test.sh
```

### test-fonts.sh
Comprehensive Nerd Fonts icon test script (v3.1.1) that displays unicode ranges for various icon sets including Powerline, Devicons, Font Awesome, Octicons, Material Design Icons, and Weather Icons.

**Usage:**
```bash
./test-fonts.sh [columns]  # default columns=16
```

## Configuration Pattern

Alacritty uses TOML format for configuration (migrated from YAML as seen in git history). The configuration supports:
- Importing external files for themes/shared configs
- Section-based organization (`[general]`, `[font]`, `[cursor]`, `[window]`, etc.)
- Home directory paths using `~/`

## Common Modifications

**Font changes:** Edit `[font]` section in `alacritty.toml`:
```toml
[font]
normal.family = "Your Font Name"
size = 16
```

**Theme changes:** Modify the `import` line in `[general]` section

**Window behavior:** Edit `[window]` section (padding, opacity, startup_mode, decorations)

**Cursor styling:** Edit `[cursor]` and `[cursor.style]` sections

## Git History Notes

Based on recent commits, this config is actively maintained with frequent font size adjustments for different screen sizes. The repository recently:
- Migrated from YAML to TOML format
- Switched to JetBrainsMono Nerd Font (from MesloLGS)
- Changed to coolnight theme
- Adjusted font sizes between 14-18 based on display needs
